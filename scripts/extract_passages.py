#!/usr/bin/env python3
"""
Theory-guided passage extraction for the OrgSciWrongdoing corpus.

For every source document and every coding scheme in ../coding_schemes/*.md,
Claude Haiku 5.5 (Amazon Bedrock, Converse API) extracts extended verbatim
passages that fit the scheme's categories and gives each an inductive label.
Results are written to ../analysis_output/<scheme>.md (and a .csv twin):

    # Category
    ## Inductive label
    > quote
    *Case — source document, p. N*

Caching
  * Extracted document text is cached on disk (.extraction_cache/text), so PDFs
    are converted only once.
  * Each document (or chunk of a very long document) is sent as a Bedrock
    prompt-cache prefix; the five theories are then run back-to-back against
    that cached prefix, so the document is paid for in full only once.
  * Every model response is cached on disk (.extraction_cache/responses), so
    an interrupted run resumes where it stopped and re-rendering is free.
    A response is redone automatically if its coding scheme file changes.

Credentials: standard AWS settings (AWS_PROFILE / AWS_ACCESS_KEY_ID +
AWS_SECRET_ACCESS_KEY [+ AWS_SESSION_TOKEN] / AWS_BEARER_TOKEN_BEDROCK) and
AWS_REGION (or AWS_DEFAULT_REGION).

Examples
  python3 scripts/extract_passages.py --dry-run          # list docs, sizes, no API calls
  python3 scripts/extract_passages.py --case Ford_Pinto  # one case, all theories
  python3 scripts/extract_passages.py --theory strain    # one theory, all cases
  python3 scripts/extract_passages.py                    # everything
  python3 scripts/extract_passages.py --render-only --harmonize
"""
from __future__ import annotations

import argparse
import bisect
import csv
import datetime as dt
import fnmatch
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# --------------------------------------------------------------------------- paths & defaults

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMES = ROOT / "coding_schemes"
DEFAULT_OUT = ROOT / "analysis_output"
DEFAULT_CACHE = ROOT / ".extraction_cache"

DOC_EXTS = {".pdf", ".txt", ".htm", ".html", ".json", ".csv", ".md"}
SKIP_DIRS = {"coding_schemes", "analysis_output", "scripts", ".extraction_cache"}

PAGE_MARK = "[[PAGE {n}]]"
PAGE_RE = re.compile(r"\[\[PAGE (\d+)\]\]")

PROMPT_VERSION = "v1"  # bump to invalidate cached responses after prompt edits
TEXT_VERSION = "t2"    # bump to re-extract cached document text
MIN_CACHE_CHARS = 4000  # Bedrock ignores/refuses cache points under ~512 tokens

print_lock = threading.Lock()


def log(*a):
    with print_lock:
        print(*a, flush=True)


def sha(s: str | bytes, n: int = 16) -> str:
    if isinstance(s, str):
        s = s.encode("utf-8")
    return hashlib.sha1(s).hexdigest()[:n]


def slug(s: str, n: int = 60) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")[:n]


# --------------------------------------------------------------------------- coding schemes

class Scheme:
    def __init__(self, path: Path):
        self.path = path
        self.slug = path.stem
        self.raw = path.read_text(encoding="utf-8")
        self.hash = sha(self.raw + PROMPT_VERSION)
        m = re.search(r"^#\s+(.+)$", self.raw, re.M)
        self.title = m.group(1).strip() if m else self.slug
        # one-level categories = every "## " heading
        self.categories: list[str] = []
        self.descriptions: dict[str, str] = {}
        parts = re.split(r"^##\s+(.+)$", self.raw, flags=re.M)
        for i in range(1, len(parts), 2):
            name = parts[i].strip()
            self.categories.append(name)
            self.descriptions[name] = parts[i + 1].strip()
        if not self.categories:
            raise ValueError(f"No '## Category' headings found in {path}")

    def match_category(self, name: str) -> str | None:
        if not name:
            return None
        if name in self.descriptions:
            return name
        low = name.strip().lower()
        for c in self.categories:
            if c.lower() == low:
                return c
        for c in self.categories:  # tolerate numbering / small drift
            if c.lower() in low or low in c.lower():
                return c
        return None


def load_schemes(folder: Path, filters: list[str]) -> list[Scheme]:
    files = sorted(p for p in folder.glob("*.md") if not p.name.lower().startswith("readme"))
    schemes = [Scheme(p) for p in files]
    if filters:
        schemes = [s for s in schemes if any(f.lower() in s.slug.lower() or f.lower() in s.title.lower() for f in filters)]
    return schemes


# --------------------------------------------------------------------------- documents & text cache

class Doc:
    def __init__(self, path: Path, corpus: Path):
        self.path = path
        self.rel = path.relative_to(corpus).as_posix()
        self.case = self.rel.split("/")[0]
        self.name = path.name
        st = path.stat()
        self.key = sha(self.rel) + "_" + slug(path.stem, 50)
        self.fingerprint = sha(f"{self.rel}|{st.st_size}|{int(st.st_mtime)}")
        self.text: str | None = None
        self.note = ""

    @property
    def label(self) -> str:
        return f"{self.case} — {self.name}"


def discover_docs(corpus: Path, cases: list[str], doc_globs: list[str]) -> list[Doc]:
    docs = []
    for top in sorted(corpus.iterdir()):
        if not top.is_dir() or top.name.startswith(".") or top.name in SKIP_DIRS:
            continue
        if cases and not any(c.lower() in top.name.lower() for c in cases):
            continue
        for p in sorted(top.rglob("*")):
            if not p.is_file() or p.suffix.lower() not in DOC_EXTS:
                continue
            if any(part.startswith(".") for part in p.relative_to(corpus).parts):
                continue
            d = Doc(p, corpus)
            if doc_globs and not any(fnmatch.fnmatch(d.rel, g) or fnmatch.fnmatch(d.name, g) for g in doc_globs):
                continue
            docs.append(d)
    return docs


def pdf_to_text(path: Path, ocr: bool, cache: Path) -> tuple[str, str]:
    """Return (text with [[PAGE n]] markers, note)."""
    pages: list[str] = []
    if shutil.which("pdftotext"):
        out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(path), "-"],
                             capture_output=True, text=True, errors="replace")
        pages = out.stdout.split("\f")
    else:
        try:
            from pypdf import PdfReader  # type: ignore
        except ImportError:
            raise RuntimeError("Install poppler (pdftotext) or `pip install pypdf` to read PDFs")
        pages = [(pg.extract_text() or "") for pg in PdfReader(str(path)).pages]
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    n = max(len(pages), 1)
    chars = sum(len(p.strip()) for p in pages)
    note = ""
    if chars / n < 400:  # little or no text layer: probably a scan
        # OCR text is cached by file content, so it survives renames, syncing and moves
        ocr_txt = cache / "ocr" / (sha(path.read_bytes(), 24) + ".txt")
        if ocr_txt.exists():
            return ocr_txt.read_text(encoding="utf-8"), "OCR"
        if ocr and shutil.which("tesseract") and shutil.which("pdftoppm"):
            log(f"   OCR: {path.name} ({n} pages, slow)…")
            pages = ocr_pdf_pages(path, cache)
            text = "\n".join(f"\n{PAGE_MARK.format(n=i + 1)}\n{p.strip()}" for i, p in enumerate(pages))
            ocr_txt.parent.mkdir(parents=True, exist_ok=True)
            ocr_txt.write_text(text, encoding="utf-8")
            return text, "OCR"
        note = (f"SCANNED: little or no text layer ({chars} chars / {n} pages); "
                f"run with --ocr (needs tesseract + poppler: brew install tesseract poppler)")
    text = "\n".join(f"\n{PAGE_MARK.format(n=i + 1)}\n{p.strip()}" for i, p in enumerate(pages))
    return text, note


def ocr_pdf_pages(path: Path, cache: Path) -> list[str]:
    tmp = cache / "ocr" / ("tmp_" + sha(str(path)))
    tmp.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pdftoppm", "-r", "300", "-gray", "-png", str(path), str(tmp / "pg")], check=True)
    imgs = sorted(tmp.glob("pg-*.png"), key=lambda p: int(re.search(r"(\d+)\.png$", p.name).group(1)))
    pages = []
    for img in imgs:
        out = subprocess.run(["tesseract", str(img), "-", "--psm", "1"], capture_output=True, text=True)
        pages.append(out.stdout)
        try:
            img.unlink()
        except OSError:
            pass
    shutil.rmtree(tmp, ignore_errors=True)
    return pages


def html_to_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    return re.sub(r"\n\s*\n\s*(\n\s*)+", "\n\n", raw).strip()


def get_text(doc: Doc, cache: Path, ocr: bool) -> str:
    tfile = cache / "text" / f"{doc.key}.{doc.fingerprint}.{TEXT_VERSION}.txt"
    nfile = tfile.with_suffix(".note")
    if tfile.exists():
        doc.note = nfile.read_text() if nfile.exists() else ""
        return tfile.read_text(encoding="utf-8")
    ext = doc.path.suffix.lower()
    note = ""
    if ext == ".pdf":
        text, note = pdf_to_text(doc.path, ocr, cache)
    else:
        raw = doc.path.read_text(encoding="utf-8", errors="replace")
        if ext in (".htm", ".html"):
            text = html_to_text(raw)
        elif ext == ".json":
            try:
                text = json.dumps(json.loads(raw), indent=1, ensure_ascii=False)
            except json.JSONDecodeError:
                text = raw
        else:
            text = raw
    tfile.parent.mkdir(parents=True, exist_ok=True)
    for old in tfile.parent.glob(f"{doc.key}.*"):
        try:
            old.unlink()
        except OSError:
            pass
    tfile.write_text(text, encoding="utf-8")
    if note:
        nfile.write_text(note)
    doc.note = note
    return text


def chunk_text(text: str, max_chars: int, overlap: int) -> list[tuple[int, int]]:
    """Split into (start, end) spans, preferring page or paragraph boundaries."""
    if len(text) <= max_chars:
        return [(0, len(text))]
    spans, start = [], 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            window = text[start + max_chars // 2:end]
            cut = -1
            for pat in ("\n[[PAGE ", "\n\n", "\n", ". "):
                cut = window.rfind(pat)
                if cut != -1:
                    break
            if cut != -1:
                end = start + max_chars // 2 + cut + 1
        spans.append((start, end))
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return spans


# --------------------------------------------------------------------------- quote verification

_TRANS = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'", "“": '"', "”": '"',
                        "„": '"', "–": "-", "—": "-", "−": "-", " ": " ", "­": "",
                        "ﬁ": "fi", "ﬂ": "fl"})


def normalize_with_map(text: str) -> tuple[str, list[int]]:
    """Lowercase, unify quotes/dashes, collapse whitespace, drop page markers and
    line-break hyphenation. Returns normalized string and map to original index."""
    text = PAGE_RE.sub(lambda m: " " * len(m.group(0)), text)
    out, idx = [], []
    prev_space = True
    i, n = 0, len(text)
    while i < n:
        ch = text[i].translate(_TRANS).lower()
        if ch == "-" and i + 1 < n and text[i + 1] == "\n" and out and out[-1].isalpha():
            j = i + 1  # "organi-\nzation" -> "organization"
            while j < n and text[j].isspace():
                j += 1
            if j < n and text[j].islower():
                i = j
                continue
        if not ch or ch.isspace():
            if not prev_space:
                out.append(" ")
                idx.append(i)
                prev_space = True
            i += 1
            continue
        for c in ch:
            out.append(c)
            idx.append(i)
        prev_space = False
        i += 1
    return "".join(out), idx


def normalize(s: str) -> str:
    return normalize_with_map(s)[0].strip()


class Verifier:
    def __init__(self, text: str):
        self.norm, self.idx = normalize_with_map(text)
        self.page_pos = [m.start() for m in PAGE_RE.finditer(text)]
        self.page_num = [int(m.group(1)) for m in PAGE_RE.finditer(text)]

    def page_at(self, orig_index: int):
        k = bisect.bisect_right(self.page_pos, orig_index) - 1
        return self.page_num[k] if k >= 0 else None

    def check(self, quote: str):
        """Return (status, page) with status in exact | approx | unverified."""
        q = normalize(quote)
        if not q:
            return "unverified", None
        pos = self.norm.find(q)
        if pos != -1:
            return "exact", self.page_at(self.idx[pos])
        words = q.split()
        if len(words) < 6:
            return "unverified", None
        w = 6
        grams = [" ".join(words[i:i + w]) for i in range(0, len(words) - w + 1, 3)]
        hits = [self.norm.find(g) for g in grams]
        found = [h for h in hits if h != -1]
        if grams and len(found) / len(grams) >= 0.7:
            return "approx", self.page_at(self.idx[found[0]])
        return "unverified", None


# --------------------------------------------------------------------------- prompts

SYSTEM_PROMPT = """You are a careful research assistant for an organization scholar who studies corporate wrongdoing \
(Enron, VW Dieselgate, Ford Pinto, Purdue Pharma/OxyContin, Boeing 737 MAX). You code primary documents \
(court records, regulatory and investigative reports, testimony, journalism) against theory-based coding schemes. \
You extract evidence; you never invent, paraphrase or embellish quotations. You answer with JSON only."""


def doc_block(doc: Doc, part: int, nparts: int, text: str) -> str:
    return (f'<document case="{doc.case}" source="{doc.rel}" part="{part} of {nparts}">\n'
            f"{text}\n</document>")


def task_prompt(scheme: Scheme, part: int, nparts: int) -> str:
    cats = "\n".join(f"- {c}" for c in scheme.categories)
    partnote = (f" This is part {part} of {nparts} of a long document; code only this part."
                if nparts > 1 else "")
    return f"""<coding_scheme>
{scheme.raw}
</coding_scheme>

TASK
Read the document above and extract every passage that provides substantive evidence for a category of the \
coding scheme "{scheme.title}".{partnote}

Categories (use these names exactly):
{cats}

Rules
1. Quotes must be VERBATIM: copy the text exactly as it appears in the document, in its original language and \
spelling. Do not paraphrase, translate, correct, or join non-adjacent text, and do not use ellipses. Leave out \
the [[PAGE n]] markers.
2. Extract EXTENDED passages: enough surrounding text that the passage can be understood on its own, usually \
3-10 sentences (about 60-350 words). Prefer one coherent longer passage over several fragments.
3. Assign each passage to the single best-fitting category. If it clearly evidences two categories you may list \
it twice, once per category.
4. Give each passage an INDUCTIVE LABEL: a short (2-7 words), concrete, data-near phrase saying what is going on \
in this specific passage, like a first-order code (for example "Software detects the test cycle" or "Board \
waives ethics code for CFO"), not the category name. Reuse an identical label for passages expressing the same idea.
5. Be thorough but selective: include passages with clear evidential value for the category's definition and \
respect its exclusions. Skip boilerplate, tables of contents, indexes, lists of exhibits and passages that only \
mention a topic. Returning few or no passages is fine. Return at most about 40 passages.
6. "page": the number in the nearest [[PAGE n]] marker before the passage, or null if there are no markers.
7. "context": one sentence saying who is speaking or writing, when, and why the passage fits the category.
8. "english_gloss": if the quote is not in English, a brief English translation; otherwise "".

Output ONLY this JSON object, with no other text:
{{"passages": [{{"category": "...", "label": "...", "quote": "...", "page": 12, "context": "...", "english_gloss": ""}}]}}"""


# --------------------------------------------------------------------------- Bedrock client

class Bedrock:
    def __init__(self, model: str, region: str, max_tokens: int, effort: str | None):
        import boto3
        from botocore.config import Config
        cfg = dict(read_timeout=1800, connect_timeout=30, retries={"max_attempts": 10, "mode": "adaptive"})
        key_id, secret = os.environ.get("AWS_ACCESS_KEY_ID"), os.environ.get("AWS_SECRET_ACCESS_KEY")
        if key_id and secret:
            # Use the access keys explicitly and force SigV4, so a stray
            # AWS_BEARER_TOKEN_BEDROCK or AWS_PROFILE cannot take precedence.
            session = boto3.session.Session(aws_access_key_id=key_id, aws_secret_access_key=secret,
                                            aws_session_token=os.environ.get("AWS_SESSION_TOKEN"),
                                            region_name=region)
            self.client = session.client("bedrock-runtime", config=Config(signature_version="v4", **cfg))
            log(f"Auth: access key {key_id[:4]}…{key_id[-4:]}\n")
        else:
            self.client = boto3.client("bedrock-runtime", region_name=region, config=Config(**cfg))
            log("Auth: default AWS credential chain\n")
        self.model, self.max_tokens, self.effort = model, max_tokens, effort
        self.usage = {"inputTokens": 0, "outputTokens": 0, "cacheReadInputTokens": 0, "cacheWriteInputTokens": 0}
        self.calls = 0
        self._lock = threading.Lock()

    def call(self, doc_text: str, task: str) -> tuple[str, str, dict]:
        user_content = [{"text": doc_text}] if doc_text else []
        if len(doc_text) >= MIN_CACHE_CHARS:
            user_content.append({"cachePoint": {"type": "default"}})
        user_content.append({"text": task})
        kwargs = dict(modelId=self.model,
                      system=[{"text": SYSTEM_PROMPT}],
                      messages=[{"role": "user", "content": user_content}],
                      inferenceConfig={"maxTokens": self.max_tokens})
        if self.effort:
            kwargs["additionalModelRequestFields"] = {"output_config": {"effort": self.effort}}
        for attempt in range(6):
            try:
                resp = self.client.converse(**kwargs)
                break
            except Exception as e:  # throttling beyond botocore's own retries
                name = type(e).__name__
                if attempt < 5 and any(k in name + str(e) for k in ("Throttl", "TooManyRequests", "ServiceUnavailable", "ModelNotReady", "timed out")):
                    wait = 30 * (attempt + 1)
                    log(f"   {name}; retrying in {wait}s")
                    time.sleep(wait)
                    continue
                raise
        usage = resp.get("usage", {})
        with self._lock:
            self.calls += 1
            for k in self.usage:
                self.usage[k] += usage.get(k, 0) or 0
        text = "".join(b.get("text", "") for b in resp["output"]["message"]["content"] if "text" in b)
        return text, resp.get("stopReason", ""), usage


def parse_json(text: str) -> dict:
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t)
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        a, b = t.find("{"), t.rfind("}")
        if a != -1 and b > a:
            return json.loads(t[a:b + 1])
        raise


# --------------------------------------------------------------------------- analysis

def response_path(cache: Path, scheme: Scheme, doc: Doc, part: int, nparts: int, max_chars: int) -> Path:
    return cache / "responses" / scheme.slug / f"{doc.key}__{doc.fingerprint}__c{max_chars}__p{part}of{nparts}.json"


def analyze_span(bed: Bedrock, scheme: Scheme, doc: Doc, text: str, part: int, nparts: int, depth: int = 0) -> list[dict]:
    raw, stop, usage = bed.call(doc_block(doc, part, nparts, text), task_prompt(scheme, part, nparts))
    if stop == "max_tokens" and len(text) > 40_000 and depth < 3:
        log(f"   output limit hit on {doc.name} [{scheme.slug}] part {part}; splitting in two")
        spans = chunk_text(text, len(text) // 2 + 1, 2000)
        out = []
        for s, e in spans:
            out += analyze_span(bed, scheme, doc, text[s:e], part, nparts, depth + 1)
        return out
    try:
        return parse_json(raw).get("passages", [])
    except Exception:
        log(f"   could not parse JSON for {doc.name} [{scheme.slug}] (stop={stop}); retrying once")
        raw, stop, usage = bed.call(doc_block(doc, part, nparts, text),
                                    task_prompt(scheme, part, nparts) + "\n\nReturn valid JSON only.")
        return parse_json(raw).get("passages", [])


def process_doc(doc: Doc, schemes: list[Scheme], bed: Bedrock, args) -> None:
    text = doc.text
    spans = chunk_text(text, args.max_chars, args.overlap)
    nparts = len(spans)
    for part, (s, e) in enumerate(spans, 1):
        for scheme in schemes:  # back-to-back so the cached document prefix is reused
            rp = response_path(args.cache, scheme, doc, part, nparts, args.max_chars)
            if rp.exists() and not args.force:
                try:
                    if json.loads(rp.read_text())["scheme_hash"] == scheme.hash:
                        continue
                except Exception:
                    pass
            t0 = time.time()
            try:
                passages = analyze_span(bed, scheme, doc, text[s:e], part, nparts)
            except Exception as ex:
                log(f"!! {doc.rel} [{scheme.slug}] part {part}/{nparts}: {type(ex).__name__}: {ex}")
                continue
            rp.parent.mkdir(parents=True, exist_ok=True)
            rp.write_text(json.dumps({"doc": doc.rel, "case": doc.case, "scheme": scheme.slug,
                                      "scheme_hash": scheme.hash, "model": bed.model, "part": part,
                                      "nparts": nparts, "created": dt.datetime.now().isoformat(timespec="seconds"),
                                      "passages": passages}, ensure_ascii=False, indent=1))
            log(f"   {doc.case}/{doc.name} [{scheme.slug}] part {part}/{nparts}: "
                f"{len(passages)} passages ({time.time() - t0:.0f}s)")


# --------------------------------------------------------------------------- label harmonization (optional)

def harmonize(bed: Bedrock, scheme: Scheme, rows: list[dict], cache: Path) -> dict[tuple[str, str], str]:
    mapping: dict[tuple[str, str], str] = {}
    for cat in scheme.categories:
        labels: dict[str, int] = {}
        for r in rows:
            if r["category"] == cat:
                labels[r["label"]] = labels.get(r["label"], 0) + 1
        if len(labels) < 2:
            continue
        key = sha(json.dumps(sorted(labels), ensure_ascii=False) + cat + PROMPT_VERSION)
        f = cache / "harmonize" / scheme.slug / f"{slug(cat, 40)}__{key}.json"
        if f.exists():
            m = json.loads(f.read_text())
        else:
            listing = "\n".join(f"- {l} ({n})" for l, n in sorted(labels.items()))
            task = (f'Coding scheme: "{scheme.title}". Category: "{cat}".\n'
                    f"Definition: {scheme.descriptions[cat]}\n\n"
                    f"These inductive labels (first-order codes, with passage counts) were assigned "
                    f"independently across documents:\n{listing}\n\n"
                    "Merge labels that express the same idea into one shared label (2-7 words, concrete, data-near). "
                    "Keep labels that capture distinct ideas separate; do not merge just to reduce the number. "
                    'Output ONLY JSON mapping every original label to its final label: {"mapping": {"original": "final", ...}}')
            raw, _, _ = bed.call("", task)
            m = parse_json(raw).get("mapping", {})
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps(m, ensure_ascii=False, indent=1))
        for orig, final in m.items():
            mapping[(cat, orig)] = final
    return mapping


# --------------------------------------------------------------------------- rendering

def collect(scheme: Scheme, docs: list[Doc], args) -> list[dict]:
    by_rel = {d.rel: d for d in docs}
    rows, seen = [], set()
    folder = args.cache / "responses" / scheme.slug
    if not folder.exists():
        return rows
    verifiers: dict[str, Verifier] = {}
    for f in sorted(folder.glob("*.json")):
        data = json.loads(f.read_text())
        doc = by_rel.get(data["doc"])
        if doc is None or data.get("scheme_hash") != scheme.hash:
            continue
        if f"__{doc.fingerprint}__" not in f.name or f"__c{args.max_chars}__" not in f.name:
            continue  # stale: source file changed or different chunking
        if doc.rel not in verifiers:
            verifiers[doc.rel] = Verifier(doc.text)
        ver = verifiers[doc.rel]
        for p in data.get("passages", []):
            quote = (p.get("quote") or "").strip()
            cat = scheme.match_category(p.get("category", ""))
            if not quote or not cat:
                continue
            k = (cat, normalize(quote)[:200], doc.rel)
            if k in seen:  # duplicates from chunk overlap
                continue
            seen.add(k)
            status, page = ver.check(quote)
            if page is None:
                page = p.get("page")
            rows.append({"case": doc.case, "document": doc.rel, "doc_name": doc.name, "page": page,
                         "category": cat, "label": (p.get("label") or "Unlabelled").strip(),
                         "original_label": (p.get("label") or "").strip(), "quote": quote,
                         "english_gloss": (p.get("english_gloss") or "").strip(),
                         "context": (p.get("context") or "").strip(), "verified": status})
    return rows


def render(scheme: Scheme, rows: list[dict], out_dir: Path, model: str, ndocs: int, drop_unverified: bool) -> Path:
    if drop_unverified:
        rows = [r for r in rows if r["verified"] != "unverified"]
    lines = [f"<!-- {scheme.title} | generated {dt.date.today()} | {model} | {ndocs} documents | {len(rows)} passages -->",
             f"*{scheme.title}: passages extracted from {ndocs} documents with {model}, {dt.date.today()}. "
             f"Passages marked ⚠ were not found verbatim in the source and need checking.*", ""]
    for cat in scheme.categories:
        crow = [r for r in rows if r["category"] == cat]
        lines += [f"# {cat}", ""]
        if not crow:
            lines += ["*No passages extracted.*", ""]
            continue
        groups: dict[str, list[dict]] = {}
        for r in crow:
            groups.setdefault(r["label"], []).append(r)
        for label, items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
            lines += [f"## {label}", ""]
            for r in sorted(items, key=lambda r: (r["case"], r["document"], str(r["page"] or ""))):
                q = re.sub(r"\s*\n\s*", " ", r["quote"]).strip()
                lines.append(f"> {q}")
                if r["english_gloss"]:
                    lines += [">", f"> *[EN] {r['english_gloss']}*"]
                src = f"{r['case']} — {r['doc_name']}" + (f", p. {r['page']}" if r["page"] else "")
                flag = "" if r["verified"] == "exact" else (" · ≈ near-verbatim" if r["verified"] == "approx" else " · ⚠ not found verbatim")
                lines += ["", f"*{src}{flag}*", ""]
    md = out_dir / f"{scheme.slug}.md"
    md.write_text("\n".join(lines), encoding="utf-8")
    with open(out_dir / f"{scheme.slug}.csv", "w", newline="", encoding="utf-8") as fh:
        cols = ["case", "document", "page", "category", "label", "original_label", "verified", "quote", "english_gloss", "context"]
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return md


# --------------------------------------------------------------------------- main

def default_region() -> str:
    r = os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION")
    if not r:
        try:
            import boto3
            r = boto3.session.Session().region_name
        except Exception:
            r = None
    return r or "eu-central-1"


# Haiku 5.5 is not enabled for this AWS account (AccessDenied from every region).
HAIKU_4_5 = "anthropic.claude-haiku-4-5-20251001-v1:0"


def default_model(region: str) -> str:
    if os.environ.get("BEDROCK_MODEL_ID"):
        return os.environ["BEDROCK_MODEL_ID"]
    geo = region.split("-")[0]
    return f"{geo}.{HAIKU_4_5}" if geo in ("eu", "us") else f"global.{HAIKU_4_5}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", type=Path, default=ROOT, help="folder holding the case folders (default: repo root)")
    ap.add_argument("--schemes", type=Path, default=DEFAULT_SCHEMES)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    ap.add_argument("--theory", action="append", default=[], help="only schemes whose file name/title contains this (repeatable)")
    ap.add_argument("--case", action="append", default=[], help="only case folders containing this (repeatable)")
    ap.add_argument("--doc", action="append", default=[], help="only documents matching this glob (repeatable)")
    ap.add_argument("--region", default=None)
    ap.add_argument("--model", default=None, help="Bedrock model / inference profile id (default: <geo>.anthropic.claude-haiku-4-5-20251001-v1:0)")
    ap.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"], default=None,
                    help="model effort level (default: model default)")
    ap.add_argument("--max-chars", type=int, default=400_000, help="split documents longer than this (~100k tokens)")
    ap.add_argument("--overlap", type=int, default=3000)
    ap.add_argument("--max-tokens", type=int, default=32_000, help="max output tokens per call")
    ap.add_argument("--workers", type=int, default=2, help="documents processed in parallel")
    ap.add_argument("--ocr", action="store_true", help="OCR scanned PDFs with ocrmypdf if installed")
    ap.add_argument("--force", action="store_true", help="ignore cached model responses")
    ap.add_argument("--dry-run", action="store_true", help="extract & cache text, report sizes, no API calls")
    ap.add_argument("--render-only", action="store_true", help="only rebuild output files from cached responses")
    ap.add_argument("--harmonize", action="store_true", help="merge near-duplicate labels within each category (extra API calls)")
    ap.add_argument("--drop-unverified", action="store_true", help="leave out quotes not found in the source")
    args = ap.parse_args()

    args.region = args.region or default_region()
    args.model = args.model or default_model(args.region)
    corpus = args.corpus.resolve()
    schemes = load_schemes(args.schemes, args.theory)
    docs = discover_docs(corpus, args.case, args.doc)
    if not schemes:
        sys.exit(f"No coding schemes found in {args.schemes}")
    if not docs:
        sys.exit(f"No documents found under {corpus}")
    log(f"{len(schemes)} coding scheme(s): " + ", ".join(s.slug for s in schemes))
    log(f"{len(docs)} document(s) in {corpus}")
    log(f"Model {args.model} in {args.region}\n")

    # 1. text extraction (cached)
    usable, total_chars, total_calls = [], 0, 0
    for d in docs:
        try:
            d.text = get_text(d, args.cache, args.ocr)
        except Exception as e:
            log(f"!! cannot read {d.rel}: {e}")
            continue
        if d.note.startswith("SCANNED") or len(normalize(PAGE_RE.sub(" ", d.text))) < 200:
            log(f"-- skipping {d.rel}: no usable text {('(' + d.note + ')') if d.note else ''}")
            continue
        n = len(chunk_text(d.text, args.max_chars, args.overlap))
        total_chars += len(d.text)
        total_calls += n * len(schemes)
        if args.dry_run:
            log(f"   {len(d.text):>9,} chars  {n} part(s)  {d.rel}" + (f"   [{d.note}]" if d.note else ""))
        usable.append(d)
    log(f"\n{len(usable)} usable documents, {total_chars:,} characters (~{total_chars // 4:,} tokens)"
        + ("" if args.render_only else f", up to {total_calls} model calls (cached responses are skipped)."))
    if args.dry_run:
        return

    bed = None
    if not args.render_only or args.harmonize:
        try:
            bed = Bedrock(args.model, args.region, args.max_tokens, args.effort)
        except ImportError:
            sys.exit("boto3 is not installed: pip install -r scripts/requirements.txt")

    # 2. model calls, one document per worker, all theories back-to-back per document
    if not args.render_only:
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
            futs = {pool.submit(process_doc, d, schemes, bed, args): d for d in usable}
            for i, fut in enumerate(as_completed(futs), 1):
                d = futs[fut]
                try:
                    fut.result()
                except Exception as e:
                    log(f"!! {d.rel}: {type(e).__name__}: {e}")
                log(f"[{i}/{len(usable)}] done: {d.rel}")
        u = bed.usage
        log(f"\n{bed.calls} calls in {(time.time() - t0) / 60:.1f} min. Tokens: input {u['inputTokens']:,}, "
            f"cache write {u['cacheWriteInputTokens']:,}, cache read {u['cacheReadInputTokens']:,}, output {u['outputTokens']:,}")

    # 3. render one file per theory
    args.out.mkdir(parents=True, exist_ok=True)
    for scheme in schemes:
        rows = collect(scheme, usable, args)
        if args.harmonize and rows:
            mp = harmonize(bed, scheme, rows, args.cache)
            for r in rows:
                r["label"] = mp.get((r["category"], r["original_label"]), r["label"])
        md = render(scheme, rows, args.out, args.model, len({r["document"] for r in rows}), args.drop_unverified)
        bad = sum(r["verified"] == "unverified" for r in rows)
        log(f"wrote {md.relative_to(args.out.parent) if args.out.parent in md.parents else md}: "
            f"{len(rows)} passages, {len({r['label'] for r in rows})} labels, {bad} unverified")


if __name__ == "__main__":
    main()
