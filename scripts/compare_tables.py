#!/usr/bin/env python3
"""
Comparison tables from the extracted passages: one table set per theory (cases
side by side) and one per case (theories side by side).

Reads analysis_output/<scheme>.csv (written by extract_passages.py) and runs
three fixed steps on Claude (Amazon Bedrock, Converse API). Every step uses a
set prompt and a forced tool call with a JSON schema, so the model can only
fill in the defined fields: no free-text answer and no reasoning outside the
fields. Each answer is checked in Python (required fields, allowed values, word
limits, passage IDs, consistency with the step-1 records) and sent back once
for correction if it breaks a rule; if it still fails it is trimmed to fit and
flagged with ⚠ in the tables.

  Step 1  cell    theory x case x category, from that cell's passages only:
                  presence, mechanism, actors, period, supporting passage IDs
  Step 2  theory  per theory, from the step-1 records of all cases: common
                  pattern and key difference per category, a one-line summary
  Step 3  case    per case, from the step-1 records of all theories: fit of
                  each theory, what it explains and leaves unexplained,
                  strongest category, complementary theory pairs

Coverage scores and case rankings are computed in Python, not by the model.

Output in analysis_output/comparisons/:
  theory_<scheme>.md   case_<case>.md   cells.csv

Model answers are cached in .extraction_cache/compare/, so re-running only
redoes cells whose passages or prompts changed.

Examples
  python3 scripts/compare_tables.py --dry-run             # cell sizes, no API calls
  python3 scripts/compare_tables.py --case Ford_Pinto     # one case, all theories
  python3 scripts/compare_tables.py                       # everything
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract_passages as ep  # noqa: E402
from extract_passages import log, sha  # noqa: E402

# --------------------------------------------------------------------------- paths & defaults

DEFAULT_IN = ep.DEFAULT_OUT
DEFAULT_OUT = ep.DEFAULT_OUT / "comparisons"
DEFAULT_CACHE = ep.DEFAULT_CACHE / "compare"

COMPARE_VERSION = "c2"  # bump to invalidate cached answers after prompt edits

PRESENCE = ["strong", "moderate", "weak", "absent"]
PRESENCE_SCORE = {"strong": 3, "moderate": 2, "weak": 1, "absent": 0}
MARK = {"strong": "●●●", "moderate": "●●○", "weak": "●○○", "absent": "○○○"}
FIT = ["high", "medium", "low"]
VERIFIED_RANK = {"exact": 0, "approx": 1, "unverified": 2}
QUOTE_CHARS = 1200  # longest quote sent to the model

# --------------------------------------------------------------------------- set prompts

SYSTEM_PROMPT = """You assist an organization scholar who compares corporate wrongdoing cases \
(Enron, VW Dieselgate, Ford Pinto, Purdue Pharma/OxyContin, Boeing 737 MAX) through theories of \
organizational wrongdoing. You fill in structured records from the evidence you are given and from \
nothing else: no outside knowledge of the cases. You answer only by calling the tool you are given. \
Every field is short and factual. You never add reasoning, caveats or commentary."""

STEP1_PROMPT = """THEORY: {theory}
CATEGORY: {category}
CATEGORY DEFINITION:
{definition}

CASE: {case}
{n} passages from {ndocs} documents were coded to this category for this case{sampled}:

{passages}

Call record_cell. Fill each field by these rules:
1. presence: "strong" if several passages from more than one document show the category directly; \
"moderate" if the evidence is direct but limited to a few passages or one document; "weak" if it is \
only indirect or in passing; "absent" if the passages do not actually show this category.
2. mechanism: one sentence on how this category operated in this case, using only what the passages \
say. If presence is "absent", write "No evidence in the passages."
3. actors: the people, units or organizations the passages name as involved (up to 4; empty if none).
4. period: when it happened, as stated in the passages, or "not stated".
5. evidence_ids: the passage IDs that best support the mechanism, strongest first. Empty only if \
presence is "absent"."""

STEP2_PROMPT = """THEORY: {theory}
CORE IDEA: {core}

Step-1 records for this theory, grouped by category (case | presence | mechanism):

{cells}

Call record_theory_comparison. Fill each field by these rules, using only the records above:
1. rows: exactly one row per category, in this order: {categories}.
   - common_pattern: what the cases with strong or moderate presence share in this category; \
"None" if fewer than two cases have strong or moderate presence.
   - key_difference: the main way the cases differ in this category.
   - most_pronounced: a case with the highest presence in this category; among ties, the one \
with the clearest mechanism.
   - least_pronounced: a case with the lowest presence in this category.
2. summary: one sentence on what this theory shows across the cases."""

STEP3_PROMPT = """CASE: {case}

Step-1 records for this case, grouped by theory (category | presence | mechanism):

{cells}

Call record_case_comparison. Fill each field by these rules, using only the records above:
1. rows: exactly one row per theory, in this order: {theories}.
   - fit: "high" if at least half of the theory's categories are strong or moderate and their \
mechanisms connect into an account of the wrongdoing; "low" if fewer than a third are strong or \
moderate; otherwise "medium".
   - explains: what part of the wrongdoing this theory accounts for in this case.
   - leaves_unexplained: the most important part it does not account for, as shown by the other \
theories' records.
   - strongest_category: the theory's category with the clearest evidence in this case, written \
exactly as listed.
2. complementarities: up to 3 pairs of different theories whose records fit together, each with \
one sentence on how."""


def words(n: int, what: str) -> dict:
    return {"type": "string", "description": f"{what} (max {n} words)"}


PROSE_TARGET, PROSE_MAX = 40, 100  # free-text fields: the length asked for, and the hard limit


def prose(what: str) -> dict:
    return {"type": "string", "description": f"{what} (about {PROSE_TARGET} words; max {PROSE_MAX} words)"}


def step1_tool(ids: list[str]) -> dict:
    return {"name": "record_cell",
            "description": "Record how one category of a theory appears in one case.",
            "schema": {"type": "object", "properties": {
                "presence": {"type": "string", "enum": PRESENCE},
                "mechanism": prose("One sentence"),
                "actors": {"type": "array", "maxItems": 4, "items": words(6, "Actor")},
                "period": words(12, "When, or 'not stated'"),
                "evidence_ids": {"type": "array", "maxItems": 3, "items": {"type": "string", "enum": ids}},
            }, "required": ["presence", "mechanism", "actors", "period", "evidence_ids"]}}


def step2_tool(categories: list[str], cases: list[str]) -> dict:
    row = {"type": "object", "properties": {
        "category": {"type": "string", "enum": categories},
        "common_pattern": prose("Shared pattern, or 'None'"),
        "key_difference": prose("Main difference"),
        "most_pronounced": {"type": "string", "enum": cases},
        "least_pronounced": {"type": "string", "enum": cases},
    }, "required": ["category", "common_pattern", "key_difference", "most_pronounced", "least_pronounced"]}
    return {"name": "record_theory_comparison",
            "description": "Record how one theory's categories compare across cases.",
            "schema": {"type": "object", "properties": {
                "rows": {"type": "array", "minItems": len(categories), "maxItems": len(categories), "items": row},
                "summary": prose("One sentence"),
            }, "required": ["rows", "summary"]}}


def step3_tool(theories: list[str]) -> dict:
    row = {"type": "object", "properties": {
        "theory": {"type": "string", "enum": theories},
        "fit": {"type": "string", "enum": FIT},
        "explains": prose("What it accounts for"),
        "leaves_unexplained": prose("What it misses"),
        "strongest_category": words(12, "Category name exactly as listed"),
    }, "required": ["theory", "fit", "explains", "leaves_unexplained", "strongest_category"]}
    pair = {"type": "object", "properties": {
        "theories": {"type": "array", "minItems": 2, "maxItems": 2, "items": {"type": "string", "enum": theories}},
        "link": prose("One sentence"),
    }, "required": ["theories", "link"]}
    return {"name": "record_case_comparison",
            "description": "Record how the theories compare within one case.",
            "schema": {"type": "object", "properties": {
                "rows": {"type": "array", "minItems": len(theories), "maxItems": len(theories), "items": row},
                "complementarities": {"type": "array", "maxItems": 3, "items": pair},
            }, "required": ["rows", "complementarities"]}}


# --------------------------------------------------------------------------- answer checking

WORD_LIMIT_RE = re.compile(r"max (\d+) words")


def word_limit(s: dict) -> int | None:
    m = WORD_LIMIT_RE.search(s.get("description", ""))
    return int(m.group(1)) if m else None


def leaked(v: dict, name: str):
    """A field the model packed into another field's string, as `"name": ...` or `<parameter name="name">...`."""
    pat = re.compile(rf'(?:<parameter name="{re.escape(name)}">|"{re.escape(name)}"\s*:)\s*')
    for x in v.values():
        if isinstance(x, str) and (m := pat.search(x)):
            try:
                return json.JSONDecoder().raw_decode(x, m.end())[0]
            except json.JSONDecodeError:
                pass
    return None


def coerce(v, s: dict):
    """Haiku sometimes sends a list or object as a JSON string, at times with other fields
    appended to it; parse it back."""
    t = s.get("type")
    if t in ("array", "object") and isinstance(v, str):
        try:
            v = json.loads(v)
        except json.JSONDecodeError:
            try:
                v = json.JSONDecoder().raw_decode(v.lstrip())[0]  # keep the leading value
            except json.JSONDecodeError:
                return v
    if t == "object" and isinstance(v, dict):
        v = {**{k: x for k in s.get("properties", {}) if k not in v and (x := leaked(v, k)) is not None}, **v}
        return {k: coerce(x, s["properties"][k]) if k in s.get("properties", {}) else x for k, x in v.items()}
    if t == "array" and isinstance(v, list):
        return [coerce(x, s["items"]) for x in v]
    return v


def validate(v, s: dict, path: str = "input") -> list[str]:
    t = s.get("type")
    if t == "object":
        if not isinstance(v, dict):
            return [f"{path}: must be an object"]
        errs = [f"{path}.{k}: missing" for k in s.get("required", []) if k not in v]
        for k, sub in s.get("properties", {}).items():
            if k in v:
                errs += validate(v[k], sub, f"{path}.{k}")
        return errs
    if t == "array":
        if not isinstance(v, list):
            return [f"{path}: must be a list"]
        errs = []
        if len(v) < s.get("minItems", 0):
            errs.append(f"{path}: needs at least {s['minItems']} items, got {len(v)}")
        if "maxItems" in s and len(v) > s["maxItems"]:
            errs.append(f"{path}: at most {s['maxItems']} items, got {len(v)}")
        for i, x in enumerate(v):
            errs += validate(x, s["items"], f"{path}[{i}]")
        return errs
    if t == "string":
        if not isinstance(v, str):
            return [f"{path}: must be text"]
        if "enum" in s and v not in s["enum"]:
            return [f"{path}: {v!r} is not one of {s['enum']}"]
        n = word_limit(s)
        if n and len(v.split()) > n:
            return [f"{path}: {len(v.split())} words, the limit is {n}"]
    return []


def trim(v, s: dict):
    """Last resort after a failed correction: cut the answer down to the schema."""
    t = s.get("type")
    if t == "object" and isinstance(v, dict):
        v = {**{k: [] for k, p in s.get("properties", {}).items() if k not in v and p.get("type") == "array"}, **v}
        return {k: trim(x, s["properties"][k]) if k in s.get("properties", {}) else x for k, x in v.items()}
    if t == "array" and not isinstance(v, list):
        return []
    if t == "array" and isinstance(v, list):
        items = [trim(x, s["items"]) for x in v]
        items = [x for x in items if not validate(x, s["items"])]
        return items[:s.get("maxItems", len(items))]
    if t == "string" and isinstance(v, str):
        n = word_limit(s)
        if n and len(v.split()) > n:
            return " ".join(v.split()[:n]) + "…"
    return v


# --------------------------------------------------------------------------- model calls

class Runner:
    def __init__(self, model: str, region: str, max_tokens: int, temperature: float | None, cache: Path, force: bool):
        self.client = ep.Bedrock(model, region, max_tokens, None).client
        self.model, self.max_tokens, self.temperature = model, max_tokens, temperature
        self.cache, self.force = cache, force
        self.calls = 0

    def _converse(self, messages: list, spec: dict) -> dict:
        inference = {"maxTokens": self.max_tokens}
        if self.temperature is not None:
            inference["temperature"] = self.temperature
        kwargs = dict(modelId=self.model, system=[{"text": SYSTEM_PROMPT}], messages=messages,
                      inferenceConfig=inference,
                      toolConfig={"tools": [spec], "toolChoice": {"tool": {"name": spec["toolSpec"]["name"]}}})
        for attempt in range(6):
            try:
                self.calls += 1
                return self.client.converse(**kwargs)
            except Exception as e:  # throttling beyond botocore's own retries
                name = type(e).__name__
                if attempt < 5 and any(k in name + str(e) for k in ("Throttl", "TooManyRequests", "ServiceUnavailable", "ModelNotReady", "timed out")):
                    wait = 30 * (attempt + 1)
                    log(f"   {name}; retrying in {wait}s")
                    time.sleep(wait)
                    continue
                raise

    def run(self, step: str, label: str, prompt: str, tool: dict, check=None) -> dict:
        schema = tool["schema"]
        spec = {"toolSpec": {"name": tool["name"], "description": tool["description"], "inputSchema": {"json": schema}}}
        key = sha(json.dumps([COMPARE_VERSION, self.model, SYSTEM_PROMPT, prompt, spec], sort_keys=True))
        path = self.cache / step / f"{key}.json"
        if path.exists() and not self.force:
            return json.loads(path.read_text(encoding="utf-8"))

        messages = [{"role": "user", "content": [{"text": prompt}]}]
        for attempt in range(2):
            resp = self._converse(messages, spec)
            content = resp["output"]["message"]["content"]
            use = next((b["toolUse"] for b in content if "toolUse" in b), None)
            if use is None:
                raise RuntimeError(f"{label}: no tool call in the answer (stop={resp.get('stopReason')})")
            out = coerce(use["input"], schema)
            errs = validate(out, schema) or (check(out) if check else [])
            if not errs:
                break
            log(f"   {label}: answer broke {len(errs)} rule(s); asking for a correction" if attempt == 0 else
                f"   ⚠ {label}: still broke {len(errs)} rule(s) after correction; trimming and flagging")
            # Bedrock needs a toolResult for every toolUse; only the first call is read
            reject = "Rejected. Fix these problems and call the tool again, once:\n- " + "\n- ".join(errs)
            messages += [{"role": "assistant", "content": content},
                         {"role": "user", "content": [{"toolResult": {
                             "toolUseId": b["toolUse"]["toolUseId"], "status": "error",
                             "content": [{"text": reject if b["toolUse"] is use else "Ignored: only one call is read."}]}}
                             for b in content if "toolUse" in b]}]
        if errs:
            out = trim(out, schema)
            out["_flags"] = errs
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        return out


# --------------------------------------------------------------------------- passages

def core_idea(scheme: ep.Scheme) -> str:
    m = re.search(r"\*\*Core idea\.\*\*\s*(.+)", scheme.raw)
    return m.group(1).strip() if m else scheme.title


def load_cells(scheme: ep.Scheme, in_dir: Path, include_unverified: bool) -> dict[tuple[str, str], list[dict]]:
    path = in_dir / f"{scheme.slug}.csv"
    if not path.exists():
        sys.exit(f"Missing {path}; run extract_passages.py first")
    cells: dict[tuple[str, str], list[dict]] = defaultdict(list)
    seen = set()
    with path.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            cat = scheme.match_category(r["category"])
            if not cat or (r["verified"] == "unverified" and not include_unverified):
                continue
            k = (r["case"], cat, ep.normalize(r["quote"]))
            if k in seen:
                continue
            seen.add(k)
            r["category"] = cat
            cells[(r["case"], cat)].append(r)
    return cells


def select(rows: list[dict], cap: int) -> list[dict]:
    """Up to `cap` passages, best-verified first, spread evenly across documents."""
    by_doc: dict[str, list[dict]] = defaultdict(list)
    for r in sorted(rows, key=lambda r: (VERIFIED_RANK.get(r["verified"], 3), int(r["page"] or 0))):
        by_doc[r["document"]].append(r)
    queues = sorted(by_doc.values(), key=len, reverse=True)
    picked: list[dict] = []
    while len(picked) < cap and any(queues):
        for q in queues:
            if q and len(picked) < cap:
                picked.append(q.pop(0))
    return picked


def passage_block(pid: str, r: dict) -> str:
    quote = r["quote"] if len(r["quote"]) <= QUOTE_CHARS else r["quote"][:QUOTE_CHARS] + "…"
    gloss = f"\n(English: {r['english_gloss']})" if r.get("english_gloss") else ""
    page = f", p. {r['page']}" if r.get("page") else ""
    return f"[{pid}] {Path(r['document']).stem}{page}\n{quote}{gloss}"


# --------------------------------------------------------------------------- steps

def step1_cell(run: Runner, scheme: ep.Scheme, case: str, category: str, rows: list[dict], cap: int) -> dict:
    ndocs = len({r["document"] for r in rows})
    base = {"n": len(rows), "ndocs": ndocs}
    if not rows:
        return {**base, "presence": "absent", "mechanism": "No passages coded.", "actors": [],
                "period": "not stated", "evidence_ids": [], "evidence": []}
    picked = select(rows, cap)
    ids = [f"P{i + 1}" for i in range(len(picked))]
    prompt = STEP1_PROMPT.format(
        theory=scheme.title, category=category, definition=scheme.descriptions[category], case=case,
        n=len(rows), ndocs=ndocs,
        sampled=f" ({len(picked)} shown, spread across documents)" if len(picked) < len(rows) else "",
        passages="\n\n".join(passage_block(i, r) for i, r in zip(ids, picked)))

    def check(out):
        if out["presence"] != "absent" and not out["evidence_ids"]:
            return ["evidence_ids: give at least one passage ID unless presence is \"absent\""]
        return []

    out = run.run("cell", f"{scheme.slug} / {case} / {category}", prompt, step1_tool(ids), check)
    out.update(base)
    out["evidence"] = [picked[ids.index(i)] for i in out["evidence_ids"] if i in ids]
    return out


def cells_text(records: list[tuple[str, str, dict]]) -> str:
    """records: (group, item, cell) -> grouped lines 'item | presence | mechanism'."""
    lines, last = [], None
    for group, item, c in records:
        if group != last:
            lines.append(f"\n## {group}")
            last = group
        lines.append(f"- {item} | {c['presence']} | {c['mechanism']}")
    return "\n".join(lines).strip()


def step2_theory(run: Runner, scheme: ep.Scheme, cases: list[str], cells: dict) -> dict:
    cats = scheme.categories
    prompt = STEP2_PROMPT.format(
        theory=scheme.title, core=core_idea(scheme), categories="; ".join(cats),
        cells=cells_text([(cat, case, cells[(scheme.slug, case, cat)]) for cat in cats for case in cases]))

    def check(out):
        errs = []
        got = [r["category"] for r in out["rows"]]
        if sorted(got) != sorted(cats):
            errs.append(f"rows: need each category exactly once, got {got}")
        for i, r in enumerate(out["rows"]):
            scores = {case: PRESENCE_SCORE[cells[(scheme.slug, case, r["category"])]["presence"]] for case in cases}
            if scores[r["most_pronounced"]] != max(scores.values()):
                errs.append(f"rows[{i}].most_pronounced: {r['most_pronounced']} does not have the highest presence for {r['category']}")
            if scores[r["least_pronounced"]] != min(scores.values()):
                errs.append(f"rows[{i}].least_pronounced: {r['least_pronounced']} does not have the lowest presence for {r['category']}")
        return errs

    return run.run("theory", scheme.slug, prompt, step2_tool(cats, cases), check)


def strong_share(scheme: ep.Scheme, case: str, cells: dict) -> float:
    pres = [cells[(scheme.slug, case, c)]["presence"] for c in scheme.categories]
    return sum(p in ("strong", "moderate") for p in pres) / len(pres)


def step3_case(run: Runner, case: str, schemes: list[ep.Scheme], cells: dict) -> dict:
    titles = [s.title for s in schemes]
    by_title = {s.title: s for s in schemes}
    prompt = STEP3_PROMPT.format(
        case=case, theories="; ".join(titles),
        cells=cells_text([(s.title, cat, cells[(s.slug, case, cat)]) for s in schemes for cat in s.categories]))

    def check(out):
        errs = []
        got = [r["theory"] for r in out["rows"]]
        if sorted(got) != sorted(titles):
            errs.append(f"rows: need each theory exactly once, got {got}")
        for i, r in enumerate(out["rows"]):
            s = by_title[r["theory"]]
            cat = next((c for c in s.categories if c.lower() == r["strongest_category"].strip().lower()), None)
            if cat is None:
                errs.append(f"rows[{i}].strongest_category: must be one of {s.categories}")
            elif cells[(s.slug, case, cat)]["presence"] == "absent":
                errs.append(f"rows[{i}].strongest_category: {cat} is absent in this case")
            share = strong_share(s, case, cells)
            if r["fit"] == "high" and share < 0.5:
                errs.append(f"rows[{i}].fit: \"high\" needs at least half the categories strong or moderate ({share:.0%} are)")
            if r["fit"] == "low" and share >= 1 / 3:
                errs.append(f"rows[{i}].fit: \"low\" needs fewer than a third strong or moderate ({share:.0%} are)")
        for i, p in enumerate(out["complementarities"]):
            if len(set(p["theories"])) != 2:
                errs.append(f"complementarities[{i}].theories: must name two different theories")
        return errs

    return run.run("case", case, prompt, step3_tool(titles), check)


# --------------------------------------------------------------------------- rendering

def cell_md(s: str) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def pretty(case: str) -> str:
    return case.replace("_", " ")


def coverage(scheme: ep.Scheme, case: str, cells: dict) -> float:
    pres = [cells[(scheme.slug, case, c)]["presence"] for c in scheme.categories]
    return sum(PRESENCE_SCORE[p] for p in pres) / (3 * len(pres))


class Evidence:
    """Numbers the quotes cited in one output file: E1, E2, ..."""

    def __init__(self):
        self.items: list[dict] = []
        self.index: dict[tuple, int] = {}

    def refs(self, c: dict) -> str:
        out = []
        for r in c.get("evidence", []):
            k = (r["document"], r["page"], r["quote"])
            if k not in self.index:
                self.items.append(r)
                self.index[k] = len(self.items)
            out.append(f"E{self.index[k]}")
        return ", ".join(out)

    def md(self) -> list[str]:
        lines = ["## Evidence", ""]
        for i, r in enumerate(self.items, 1):
            mark = {"approx": " ≈", "unverified": " ⚠ not found in source"}.get(r["verified"], "")
            page = f", p. {r['page']}" if r.get("page") else ""
            q = r["quote"] if len(r["quote"]) <= 500 else r["quote"][:500] + "…"
            lines += [f"**E{i}.** {pretty(r['case'])}, *{Path(r['document']).stem}*{page}{mark}", "", f"> {q}", ""]
        return lines


def flag(c: dict) -> str:
    return " ⚠" if c.get("_flags") else ""


def detail_table(rows: list[tuple[str, dict]], first: str, ev: Evidence) -> list[str]:
    lines = [f"| {first} | Presence | Mechanism | Actors | Period | Evidence |", "|---|---|---|---|---|---|"]
    for name, c in rows:
        lines.append(f"| {cell_md(name)} | {MARK[c['presence']]} {c['presence']} (n={c['n']}, {c['ndocs']} docs) "
                     f"| {cell_md(c['mechanism'])}{flag(c)} | {cell_md('; '.join(c['actors']))} "
                     f"| {cell_md(c['period'])} | {ev.refs(c)} |")
    return lines


def header(title: str, model: str, source: str) -> list[str]:
    return [f"# {title}", "",
            f"*Generated {dt.date.today().isoformat()} by compare_tables.py with {model}, from {source}. "
            "Presence: ●●● strong, ●●○ moderate, ●○○ weak, ○○○ absent; n = passages coded. "
            "Coverage = presence points ÷ maximum, computed in Python. ⚠ = answer trimmed after failing a rule check.*", ""]


def render_theory(scheme: ep.Scheme, cases: list[str], cells: dict, comp: dict, out_dir: Path, model: str) -> Path:
    ev = Evidence()
    lines = header(f"{scheme.title}: comparison across cases", model, f"analysis_output/{scheme.slug}.csv")
    lines += ["## Presence by category", "",
              "| Category | " + " | ".join(pretty(c) for c in cases) + " |", "|---|" + "---|" * len(cases)]
    for cat in scheme.categories:
        lines.append(f"| {cell_md(cat)} | " + " | ".join(
            f"{MARK[cells[(scheme.slug, c, cat)]['presence']]} {cells[(scheme.slug, c, cat)]['n']}" for c in cases) + " |")
    cov = {c: coverage(scheme, c, cells) for c in cases}
    lines.append("| **Coverage** | " + " | ".join(f"**{cov[c]:.0%}**" for c in cases) + " |")
    ranking = sorted(cases, key=lambda c: -cov[c])
    lines += ["", "Ranking by coverage: " + " > ".join(f"{pretty(c)} ({cov[c]:.0%})" for c in ranking), ""]

    lines += ["## Cross-case pattern", "", f"{comp['summary']}{flag(comp)}", "",
              "| Category | Common pattern | Key difference | Most pronounced | Least pronounced |", "|---|---|---|---|---|"]
    rows = {r["category"]: r for r in comp["rows"]}
    for cat in scheme.categories:
        r = rows.get(cat)
        if r:
            lines.append(f"| {cell_md(cat)} | {cell_md(r['common_pattern'])} | {cell_md(r['key_difference'])} "
                         f"| {pretty(r['most_pronounced'])} | {pretty(r['least_pronounced'])} |")
    lines += ["", "## Category detail", ""]
    for cat in scheme.categories:
        lines += [f"### {cat}", ""]
        lines += detail_table([(pretty(c), cells[(scheme.slug, c, cat)]) for c in cases], "Case", ev)
        lines.append("")
    lines += ev.md()
    path = out_dir / f"theory_{scheme.slug}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def render_case(case: str, schemes: list[ep.Scheme], cells: dict, comp: dict, out_dir: Path, model: str) -> Path:
    ev = Evidence()
    lines = header(f"{pretty(case)}: comparison across theories", model, "analysis_output/*.csv")
    lines += ["## Theory fit", "",
              "| Theory | Fit | Coverage | What it explains | What it leaves unexplained | Strongest category |",
              "|---|---|---|---|---|---|"]
    rows = {r["theory"]: r for r in comp["rows"]}
    for s in schemes:
        r = rows.get(s.title)
        if r:
            lines.append(f"| {cell_md(s.title)} | {r['fit']} | {coverage(s, case, cells):.0%} | {cell_md(r['explains'])} "
                         f"| {cell_md(r['leaves_unexplained'])} | {cell_md(r['strongest_category'])} |")
    if comp.get("_flags"):
        lines += ["", "⚠ This table was trimmed after failing a rule check: " + "; ".join(comp["_flags"])]
    lines += ["", "## Complementarities", ""]
    lines += [f"- **{' + '.join(p['theories'])}**: {p['link']}" for p in comp["complementarities"]] or ["- None recorded."]
    lines += ["", "## Category detail", ""]
    for s in schemes:
        lines += [f"### {s.title}", ""]
        lines += detail_table([(cat, cells[(s.slug, case, cat)]) for cat in s.categories], "Category", ev)
        lines.append("")
    lines += ev.md()
    path = out_dir / f"case_{case}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_cells_csv(schemes: list[ep.Scheme], cases: list[str], cells: dict, out_dir: Path) -> Path:
    path = out_dir / "cells.csv"
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["theory", "case", "category", "presence", "n_passages", "n_documents",
                    "mechanism", "actors", "period", "evidence", "flags"])
        for s in schemes:
            for case in cases:
                for cat in s.categories:
                    c = cells[(s.slug, case, cat)]
                    ev = "; ".join(f"{Path(r['document']).stem} p. {r['page']}" for r in c["evidence"])
                    w.writerow([s.slug, case, cat, c["presence"], c["n"], c["ndocs"], c["mechanism"],
                                "; ".join(c["actors"]), c["period"], ev, "; ".join(c.get("_flags", []))])
    return path


# --------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", type=Path, default=DEFAULT_IN, help="folder with the <scheme>.csv passage files")
    ap.add_argument("--schemes", type=Path, default=ep.DEFAULT_SCHEMES)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    ap.add_argument("--theory", action="append", default=[], help="only schemes whose file name/title contains this (repeatable)")
    ap.add_argument("--case", action="append", default=[], help="only cases containing this (repeatable)")
    ap.add_argument("--region", default=None)
    ap.add_argument("--model", default=None, help="Bedrock model / inference profile id (default: same as extract_passages.py)")
    ap.add_argument("--max-passages", type=int, default=80, help="passages sent per theory x case x category")
    ap.add_argument("--include-unverified", action="store_true", help="also use quotes not found in the source")
    ap.add_argument("--max-tokens", type=int, default=4000, help="max output tokens per call")
    ap.add_argument("--temperature", type=float, default=0.0, help="use a negative value to leave it unset (some models reject it)")
    ap.add_argument("--workers", type=int, default=4, help="calls in parallel")
    ap.add_argument("--force", action="store_true", help="ignore cached model answers")
    ap.add_argument("--dry-run", action="store_true", help="report cell sizes, no API calls")
    args = ap.parse_args()

    schemes = ep.load_schemes(args.schemes, args.theory)
    if not schemes:
        sys.exit(f"No coding schemes found in {args.schemes}")
    passages = {}
    for s in schemes:
        for (case, cat), rows in load_cells(s, args.input, args.include_unverified).items():
            passages[(s.slug, case, cat)] = rows
    cases = sorted({k[1] for k in passages})
    if args.case:
        cases = [c for c in cases if any(f.lower() in c.lower() for f in args.case)]
    if not cases:
        sys.exit("No matching cases in the passage files")
    keys = [(s, case, cat) for s in schemes for case in cases for cat in s.categories]
    ncalls = sum(1 for s, case, cat in keys if passages.get((s.slug, case, cat)))
    log(f"{len(schemes)} theor{'y' if len(schemes) == 1 else 'ies'}, {len(cases)} case(s): " + ", ".join(cases))
    log(f"{len(keys)} cells, {ncalls} with passages: {ncalls} step-1 calls + {len(schemes)} step-2 + {len(cases)} step-3 (cached answers are skipped)")

    if args.dry_run:
        for s in schemes:
            log(f"\n{s.title}")
            for cat in s.categories:
                log(f"  {cat[:45]:45} " + "  ".join(f"{pretty(c)[:10]:>10} {len(passages.get((s.slug, c, cat), [])):4}" for c in cases))
        return

    region = args.region or ep.default_region()
    model = args.model or ep.default_model(region)
    log(f"Model {model} in {region}\n")
    run = Runner(model, region, args.max_tokens, args.temperature if args.temperature >= 0 else None,
                 args.cache, args.force)
    t0 = time.time()

    # step 1: one record per theory x case x category
    cells: dict[tuple[str, str, str], dict] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(step1_cell, run, s, case, cat, passages.get((s.slug, case, cat), []), args.max_passages):
                (s.slug, case, cat) for s, case, cat in keys}
        for i, fut in enumerate(as_completed(futs), 1):
            k = futs[fut]
            cells[k] = fut.result()
            if i % 20 == 0 or i == len(futs):
                log(f"   step 1: {i}/{len(futs)} cells")

    # steps 2 and 3: comparisons built only from the step-1 records
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        theory_futs = {pool.submit(step2_theory, run, s, cases, cells): s for s in schemes}
        case_futs = {pool.submit(step3_case, run, case, schemes, cells): case for case in cases}
        theory_comp = {theory_futs[f].slug: f.result() for f in as_completed(theory_futs)}
        case_comp = {case_futs[f]: f.result() for f in as_completed(case_futs)}
    log("   steps 2-3 done")

    args.out.mkdir(parents=True, exist_ok=True)
    for s in schemes:
        log(f"wrote {render_theory(s, cases, cells, theory_comp[s.slug], args.out, model).relative_to(ep.ROOT)}")
    for case in cases:
        log(f"wrote {render_case(case, schemes, cells, case_comp[case], args.out, model).relative_to(ep.ROOT)}")
    log(f"wrote {write_cells_csv(schemes, cases, cells, args.out).relative_to(ep.ROOT)}")
    nflag = sum(bool(c.get("_flags")) for c in cells.values()) + sum(bool(c.get("_flags")) for c in [*theory_comp.values(), *case_comp.values()])
    log(f"\n{run.calls} API calls in {(time.time() - t0) / 60:.1f} min; {nflag} answer(s) flagged ⚠")


if __name__ == "__main__":
    main()
