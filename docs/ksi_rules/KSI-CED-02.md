# KSI-CED-02: Require role-specific training for high risk roles, including at least roles with privileged access

*Generated on 2025-06-09 08:28:57 UTC*

## 📖 Overview

**KSI ID:** `KSI-CED-02`
**Description:** Require role-specific training for high risk roles, including at least roles with privileged access
**Justification:** Manual evidence required - role-specific training curricula, privileged access training records, and specialized cybersecurity training documentation
**Last Validation:** ✅ 2025-06-09T08:28:57.293331
**Result:** ✅ Role-specific training including privileged access: fedramp_role_based.png, cyber_security_training.png, security_training_roster.png

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CED-02/ for privileged_access_training.pdf, role_specific_training_matrix.xlsx, admin_security_training_records.pdf, and specialized_cybersecurity_curriculum.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CED-02/ for privileged_access_training.pdf, role_specific_training_matrix.xlsx, admin_security_training_records.pdf, and specialized_cybersecurity_curriculum.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CED_02`

**Documentation:** KSI-CED-02: Require role-specific training for high risk roles, including privileged access

Expected: Manual evidence - role-specific training documentation

### Rule Implementation
```python
def evaluate_KSI_CED_02(cli_output):
    """
    KSI-CED-02: Require role-specific training for high risk roles, including privileged access
    
    Expected: Manual evidence - role-specific training documentation
    """
    evidence_dir = Path("evidence_v2/KSI-CED-02")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CED-02/ not found"
    role_training_files = [
        "fedramp_role_based.png",
        "cyber_security_training.png",
        "security_training_roster.png"
    ]
    found_files = []
    for doc in role_training_files:
        if (evidence_dir / doc).exists():
            found_files.append(doc)
    all_files = list(evidence_dir.glob("*"))
    role_evidence = [f.name for f in all_files if any(keyword in f.name.lower() 
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Require role-specific training for high risk roles, including at least roles with privileged access

**Implementation Justification:** Manual evidence required - role-specific training curricula, privileged access training records, and specialized cybersecurity training documentation

**FedRAMP 20x Category:** Cybersecurity Education

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*