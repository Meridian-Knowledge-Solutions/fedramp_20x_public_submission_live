# KSI-RPL-02: Develop and maintain a recovery plan that aligns with defined recovery objectives

*Generated on 2025-06-07 21:03:45 UTC*

## 📖 Overview

**KSI ID:** `KSI-RPL-02`
**Description:** Develop and maintain a recovery plan that aligns with defined recovery objectives
**Justification:** Manual evidence required - disaster recovery plans, incident response procedures, and recovery playbooks
**Last Validation:** ✅ 2025-06-07T21:03:44.994539
**Result:** ⚠️ Good recovery planning (enhance maintenance procedures): ✅ Core recovery plans: incident_reponse_policy.pdf, contingency_planning_policy.pdf; ✅ Plan maintenance: 3 files updated within last year

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
        "incident_reponse_policy.pdf",
        "contingency_planning_policy.pdf",
    ]
    optional_docs = [
        "business_continuity_plan.pdf",
        "emergency_response_procedures.pdf",
        "crisis_communication_plan.pdf",
        "recovery_team_contact_list.pdf",
        "escalation_procedures.pdf",
        "vendor_recovery_contacts.pdf"
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Develop and maintain a recovery plan that aligns with defined recovery objectives

**Implementation Justification:** Manual evidence required - disaster recovery plans, incident response procedures, and recovery playbooks

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*