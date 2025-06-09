# KSI-CMT-04: Have a documented change management procedure

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-04`
**Description:** Have a documented change management procedure
**Justification:** Manual evidence required - documented procedures and policies
**Last Validation:** ✅ 2025-06-09T21:56:37.300455
**Result:** ✅ Documented change management procedure: ✅ Change management documentation found: configuration_management_policy_and_procedures.pdf, weekly_change_management_meeting_final.png

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CMT-04/ for change_management_procedure.pdf and related documentation

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CMT-04/ for change_management_procedure.pdf and related documentation

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_04`

**Documentation:** KSI-CMT-04: Have a documented change management procedure

Expected: Manual evidence - documentation files

### Rule Implementation
```python
def evaluate_KSI_CMT_04(cli_output):
    """
    KSI-CMT-04: Have a documented change management procedure
    
    Expected: Manual evidence - documentation files
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-04")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-04/ not found"
    required_docs = [
        "change_management_procedure.pdf",
        "change_management_policy.pdf", 
        "change_request_template.pdf"
    ]
    optional_docs = [
        "change_approval_process.pdf",
        "emergency_change_procedure.pdf",
        "change_calendar.pdf"
    ]
    found_required = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have a documented change management procedure

**Implementation Justification:** Manual evidence required - documented procedures and policies

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*