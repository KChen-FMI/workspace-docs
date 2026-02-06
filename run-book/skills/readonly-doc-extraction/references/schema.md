# Recommended Extraction Schema (Regulation)

Use this schema for **read-only extraction** from regulation PDFs. Store output as JSON in a new file; do not modify source documents.

```json
{
  "doc_id": "",
  "title": "",
  "doc_type": "規程",
  "effective_dates": ["YYYY-MM-DD"],
  "revision_history": [
    {"date": "YYYY-MM-DD", "type": "施行|改正施行|更新", "note": ""}
  ],
  "scope_assets": [],
  "roles": [
    {"role": "", "assigned_to": ""},
    {"role": "", "assigned_by": ""}
  ],
  "responsibilities": [],
  "prohibitions": [],
  "reporting_triggers": [],
  "required_actions": [],
  "reviewer_notes": "",
  "evidence_links": []
}
```

Notes:
- `effective_dates` should include the **first** enforcement date if multiple exist.
- `revision_history` should capture lines from 附則 / 改正履歴.
- `reviewer_notes` is for human reviewer comments or judgments.
- `evidence_links` should include the input file path.
