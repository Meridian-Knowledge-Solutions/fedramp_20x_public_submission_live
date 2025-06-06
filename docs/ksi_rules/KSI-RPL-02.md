# KSI-RPL-02: Develop and maintain a recovery plan that aligns with defined recovery objectives

<<<<<<< Updated upstream
*Generated on 2025-06-06 08:21:01 UTC*
=======
*Generated on 2025-06-06 08:22:08 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-RPL-02`
**Description:** Develop and maintain a recovery plan that aligns with defined recovery objectives
**Justification:** Manual evidence required - disaster recovery plans, incident response procedures, and recovery playbooks
<<<<<<< Updated upstream
**Last Validation:** ❌ 2025-06-06T08:21:01.667878
**Result:** ❌ No comprehensive recovery plan found in evidence_v2/KSI-RPL-02/
=======
**Last Validation:** ✅ 2025-06-06T08:22:08.663858
**Result:** ⚠️ Basic recovery plans (expand procedures and maintenance): ✅ Recovery planning documentation: incident_reponse_policy.pdf; ✅ Plan maintenance: 3 files updated within last year
>>>>>>> Stashed changes

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-RPL-02/ for disaster_recovery_plan.pdf, incident_response_plan.pdf, recovery_procedures_playbook.pdf, and business_continuity_plan.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-RPL-02/ for disaster_recovery_plan.pdf, incident_response_plan.pdf, recovery_procedures_playbook.pdf, and business_continuity_plan.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_RPL_02`

**Documentation:** KSI-RPL-02: Develop and maintain a recovery plan that aligns with the defined recovery objectives

Expected: Manual evidence - disaster recovery and incident response plans

### Rule Implementation
```python
def evaluate_KSI_RPL_02(cli_output):
    """
    KSI-RPL-02: Develop and maintain a recovery plan that aligns with the defined recovery objectives
    
    Expected: Manual evidence - disaster recovery and incident response plans
    """
    evidence_dir = Path("evidence_v2/KSI-RPL-02")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-RPL-02/ not found"
    required_docs = [
        "disaster_recovery_plan.pdf",
        "incident_response_plan.pdf",
        "recovery_procedures_playbook.pdf"
    ]
    optional_docs = [
        "business_continuity_plan.pdf",
        "emergency_response_procedures.pdf",
        "crisis_communication_plan.pdf",
        "recovery_team_contact_list.pdf",
        "escalation_procedures.pdf",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Develop and maintain a recovery plan that aligns with defined recovery objectives

**Implementation Justification:** Manual evidence required - disaster recovery plans, incident response procedures, and recovery playbooks

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*