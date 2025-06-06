# KSI-RPL-04: Regularly test the capability to recover from incidents and contingencies

*Generated on 2025-06-06 07:53:43 UTC*

## 📖 Overview

**KSI ID:** `KSI-RPL-04`
**Description:** Regularly test the capability to recover from incidents and contingencies
**Justification:** Manual evidence required - recovery testing procedures, test results, and lessons learned documentation
**Last Validation:** ❌ 2025-06-06T07:53:43.079769
**Result:** ❌ No regular recovery testing capability found in evidence_v2/KSI-RPL-04/

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-RPL-04/ for recovery_testing_procedures.pdf, disaster_recovery_test_results.xlsx, tabletop_exercise_reports.pdf, and recovery_lessons_learned.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-RPL-04/ for recovery_testing_procedures.pdf, disaster_recovery_test_results.xlsx, tabletop_exercise_reports.pdf, and recovery_lessons_learned.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_RPL_04`

**Documentation:** KSI-RPL-04: Regularly test the capability to recover from incidents and contingencies

Expected: Manual evidence - recovery testing procedures and results

### Rule Implementation
```python
def evaluate_KSI_RPL_04(cli_output):
    """
    KSI-RPL-04: Regularly test the capability to recover from incidents and contingencies
    
    Expected: Manual evidence - recovery testing procedures and results
    """
    evidence_dir = Path("evidence_v2/KSI-RPL-04")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-RPL-04/ not found"
    required_docs = [
        "recovery_testing_procedures.pdf",
        "disaster_recovery_test_results.xlsx",
        "tabletop_exercise_reports.pdf"
    ]
    optional_docs = [
        "recovery_lessons_learned.pdf",
        "backup_restoration_tests.pdf",
        "failover_testing_results.xlsx",
        "incident_simulation_reports.pdf",
        "recovery_time_validation.pdf",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Regularly test the capability to recover from incidents and contingencies

**Implementation Justification:** Manual evidence required - recovery testing procedures, test results, and lessons learned documentation

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*