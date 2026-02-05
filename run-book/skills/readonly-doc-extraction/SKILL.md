---
name: readonly-doc-extraction
description: Read-only extraction of regulation-style PDFs into a structured JSON schema without modifying the source files. Use when asked to extract policy/regulation content from PDFs and save results as a new JSON file.
---

# Readonly Doc Extraction

## Overview
Extract regulation-style PDF content into a consistent JSON schema **without editing the source PDF**.  
This skill is **rule-based only** and does **not** use LLMs or external APIs.

## Workflow
1. Identify the input PDF path and a target output JSON path.
2. Use the extraction script to produce JSON in the recommended schema.
3. Verify required fields are present; do not edit the source file.

## Quick Start
Use the script in `scripts/extract_regulation_pdf.py`:

```bash
python C:/Users/kchen/.codex/skills/readonly-doc-extraction/scripts/extract_regulation_pdf.py \
  --input "PATH/TO/REGULATION.pdf" \
  --output "PATH/TO/REGULATION.extracted.json" \
  --doc-id "07-0120"
```

## Output Schema
See `references/schema.md` for the canonical JSON format.

## Guardrails
- **Read-only**: do not modify the input document.
- **No LLM / No API**: keep extraction local and deterministic.
- Always write to a **new** `.extracted.json` file.
- Preserve evidence link to the original PDF path.
