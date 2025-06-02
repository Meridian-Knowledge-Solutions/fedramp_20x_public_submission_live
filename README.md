# FedRAMP 20x Public Submission – Meridian LMS

This repository is a public-facing, continuously updated demonstration of Meridian LMS’s participation in the FedRAMP 20x pilot.

It includes **live CLI-based evidence**, **machine-readable assertion logic**, and a **real-time trust dashboard**, all aligned with GSA’s 20x reproducibility and transparency goals.

---

## 🔍 Overview

This submission demonstrates:

- ✅ **Automated evidence generation** using AWS CLI  
- ✅ **Machine-interpretable validation rules** for each KSI  
- ✅ **Commit-traceable artifacts** with Git SHA and timestamps  
- ✅ **Clear assertion results**, visible in a public dashboard  
- ✅ **JSON schema-backed assertions** to support external analysis  
- ✅ **Rule documentation** for 3PAO and GSA evaluation  

---

## 📊 Live Dashboard

🔗 https://meridian-knowledge-solutions.github.io/fedramp_20x_public_submission_live/

This dashboard shows:

- ✅ Pass/fail status for each KSI  
- 💬 Reason for each result (`assertion_reason`)  
- 🔗 Git commit SHA and timestamp (evidence trace)  
- 💻 AWS CLI command used  
- 📄 Optional: [Failed KSI Report](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/raw/main/failed_ksi_report_readable.md)

---

## 📁 Key Files

| Path                                | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `unified_ksi_validations.json`      | Source of truth: all validations, reasons, evidence paths    |
| `evidence_commit_metadata.json`     | Git SHA + timestamp for every `raw_output.json` evidence file |
| `index.html`                        | Rendered dashboard (hosted via GitHub Pages)                 |
| `failed_ksi_report_readable.md`     | Markdown summary of failed KSIs for reviewers                |
| `docs/ksi_rules/`                   | Per-KSI rule documentation (auto-generated)                  |
| `unified_ksi_validations.schema.json` | JSON Schema for validation output format                  |

---

## 🛠 CLI Validation and Evidence Flow

- GitHub Actions run daily and collect CLI output for each KSI  
- Each CLI command output is stored in `evidence_v2/KSI-*/raw_output.json`  
- `generate_continuous_results_full.py` evaluates each KSI using logic in `cli_assertion_rules_full.py`  
- `generate_unified_validations.py` builds the dashboard JSON from results  
- `generate_failed_ksi_report.py` creates a readable Markdown report of failures  
- `generate_ksi_rule_docs.py` builds rule documentation for every KSI  

---

## ✅ Assertion Structure (JSON)

Each assertion includes:

- `ksi_id`: The key security indicator (e.g. `KSI-IAM-03`)  
- `cli_command`: The AWS CLI used to collect evidence  
- `assertion`: `true` / `false` result  
- `assertion_reason`: Why it passed or failed  
- `evidence_path`: Path to `raw_output.json`  
- `commit_sha`: SHA of the Git commit for traceability  
- `validation_timestamp`: ISO UTC timestamp  
- `cli_output_interpretation`: Plain-language summary of CLI results  

---

## 🧪 Sample Validation Result

```json
{
  "ksi_id": "KSI-SVC-03",
  "validation_id": "KSI-SVC-03",
  "cli_command": "aws kms list-keys",
  "assertion": true,
  "assertion_reason": "✅ KMS keys returned with encryption enabled",
  "evidence_path": "evidence_v2/KSI-SVC-03/raw_output.json",
  "commit_sha": "f3c1a6b",
  "validation_timestamp": "2025-06-04T02:00:00Z",
  "cli_output_interpretation": "✅ CLI command ran successfully with output."
}
```

---

## 📖 Per-KSI Rule Documentation

Each KSI has a corresponding Markdown document generated automatically in:

📁 `docs/ksi_rules/KSI-*.md`

These include:

- CLI command used  
- Logic summary  
- Pass/fail criteria  
- Justification  
- Last evaluated timestamp  
- Output snippet  

---

## 🔍 Evidence Trust Model

All evidence:

- Is collected via GitHub Actions  
- Is committed to GitHub with traceable SHA + timestamp  
- Includes validation reason and raw output  
- Is backed by assertion logic in Python  
- Fails gracefully if any link is missing  

> "Trust = CLI → Evidence → Validation → Dashboard"

---

## 🔧 JSON Schema

📁 `unified_ksi_validations.schema.json`  
Defines structure and data types for every assertion. Supports external tooling and validation pipelines.

---

## 📄 Markdown Reports

📉 [Failed KSI Report (auto-generated)](https://github.com/Meridian-Knowledge-Solutions/fedramp_20x_public_submission_live/raw/main/failed_ksi_report_readable.md)  
Includes CLI command, reason, and output snippet for each failed KSI.

---

## 📬 For GSA and 3PAO Reviewers

This repo exists to:

- Demonstrate **practical, real-time 20x validation**  
- Showcase **transparent, machine-verifiable assertions**  
- Offer **usable artifacts** for external audits  
- Respond directly to GSA’s request for community-driven trust models  

---

## 📩 Contact

Email: [fedramp@meridianks.com](mailto:fedramp@meridianks.com)  
GitHub Issues welcome for community discussion.

---

## 📛 License

This repo is for demonstration and pilot purposes only.  
All content subject to change during FedRAMP 20x pilot.  
Contact us for reuse or derivative licensing.
