# KSI-CED-01: Ensure all employees receive security awareness training

*Generated on 2025-06-12 03:16:25 UTC*

## 📖 Overview

**KSI ID:** `KSI-CED-01`
**Description:** Ensure all employees receive security awareness training
**Justification:** Manual evidence required - security awareness training programs, completion records, and training materials
**Last Validation:** ✅ 2025-06-12T03:16:24.774420
**Result:** ✅ Security awareness training evidence: cyber_security_training.png, security_training_roster.png, fedramp_role_based.png

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CED-01/ for security_awareness_training_program.pdf, employee_training_records.xlsx, training_completion_certificates.pdf, and annual_training_schedule.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CED-01/ for security_awareness_training_program.pdf, employee_training_records.xlsx, training_completion_certificates.pdf, and annual_training_schedule.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CED_01`

**Documentation:** KSI-CED-01: Ensure all employees receive security awareness training

Expected: Manual evidence - training documentation

### Rule Implementation
```python
def evaluate_KSI_CED_01(cli_output):
    """
    KSI-CED-01: Ensure all employees receive security awareness training
    
    Expected: Manual evidence - training documentation
    """
    evidence_dir = Path("evidence_v2/KSI-CED-01")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CED-01/ not found"
    training_files = [
        "cyber_security_training.png",
        "security_training_roster.png", 
        "fedramp_role_based.png"
    ]
    found_files = []
    for doc in training_files:
        if (evidence_dir / doc).exists():
            found_files.append(doc)
    all_files = list(evidence_dir.glob("*"))
    training_evidence = [f.name for f in all_files if any(keyword in f.name.lower() 
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Ensure all employees receive security awareness training

**Implementation Justification:** Manual evidence required - security awareness training programs, completion records, and training materials

**FedRAMP 20x Category:** Cybersecurity Education

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*