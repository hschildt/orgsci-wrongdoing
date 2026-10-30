# Passage extraction with Claude Haiku 5.5 on Amazon Bedrock

`extract_passages.py` codes every source document in the case folders against each coding scheme in `coding_schemes/`, one scheme at a time, and writes one Markdown file per theory to `analysis_output/`:

```
# Category
## Inductive label
> verbatim extended passage
*Case — source document, p. N*
```

A CSV with the same passages (plus page, verification status and a one-line context note) is written next to each Markdown file, for use as a dataset.

## Setup

```bash
cd ".../OrgSciWrongdoing"
python3 -m pip install -r scripts/requirements.txt
# PDF text: poppler's pdftotext is used if present (macOS: brew install poppler); otherwise pypdf
```

Credentials come from your normal AWS terminal settings: `AWS_PROFILE`, or `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` (/ `AWS_SESSION_TOKEN`), or a Bedrock API key in `AWS_BEARER_TOKEN_BEDROCK`. Set the region with `AWS_REGION` (EU calls must originate from `eu-central-1` or `eu-west-3`; eu-north-1 is only a routing destination). The model defaults to the matching cross-region profile, `eu.anthropic.claude-haiku-4-5-20251001-v1:0` for EU regions (`us.` for US, `global.` otherwise). Override with `--model` or `BEDROCK_MODEL_ID`. (Haiku 5.5 is not enabled for this AWS account; don't pass `--effort` with Haiku 4.5.)

## Running

```bash
python3 scripts/extract_passages.py --dry-run                  # text extraction + size report, no API calls
python3 scripts/extract_passages.py --case Ford_Pinto          # trial run on the smallest case
python3 scripts/extract_passages.py                            # everything
python3 scripts/extract_passages.py --theory attention         # one theory only
python3 scripts/extract_passages.py --doc "*Powers_Report*"    # one document
python3 scripts/extract_passages.py --render-only --harmonize  # merge near-duplicate labels and rebuild outputs
```

Useful options: `--workers N` (documents in parallel, default 2), `--effort low|medium|high` (model effort), `--max-chars` (chunk size for very long documents, default 400,000 characters ≈ 100k tokens), `--ocr` (OCR scanned PDFs with tesseract), `--drop-unverified`, `--force`.

## How caching works

1. **Text cache.** Each document is converted to text once (PDF pages are marked `[[PAGE n]]` so quotes get page numbers) and stored in `.extraction_cache/text/`.
2. **Prompt cache.** The document is the cached prefix of each request; the five theories run back-to-back against it, so after the first theory the document is read from Bedrock's prompt cache at a fraction of the price.
3. **Response cache.** Every model answer is stored in `.extraction_cache/responses/<theory>/`. Re-running skips work already done, so an interrupted run simply resumes. Editing a coding scheme invalidates only that scheme's responses; editing a source file invalidates only that file.

## Quality checks built in

- Every quote is checked against the source text. Exact matches print normally; near-verbatim matches (e.g. differences in PDF hyphenation) are marked `≈`; quotes not found are marked `⚠` (or dropped with `--drop-unverified`).
- Page numbers come from where the quote is actually found in the PDF, not from the model.
- Non-English passages (the Bundestag report) are quoted in German with an English gloss.
- Passages duplicated by chunk overlap are removed.

## Notes on the corpus

- Ten PDFs are image scans with no usable text layer, including the VW plea agreement with its Statement of Facts, the Liang and IAV pleas, both EPA Notices of Violation and the four Watkins trial exhibits. Their OCR text is already in `.extraction_cache/ocr/` (keyed by file content), so the script uses it automatically. For new scanned files, run with `--ocr` after `brew install tesseract poppler`; otherwise scans are skipped with a warning. The Watkins handwritten notes OCR poorly.
- Very long documents (Bundestag report, the House hearings) are split into parts; each part is coded separately.
- The coding scheme files are the single source of truth: categories are the `## ` headings, and everything under a heading is sent to the model as that category's definition. Add, rename or edit categories there and rerun.
