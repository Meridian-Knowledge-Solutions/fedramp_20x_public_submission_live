# KSI-INR-01: Report incidents according to FedRAMP requirements and cloud service provider policies

*Generated on 2025-06-06 05:52:21 UTC*

## 📖 Overview

**KSI ID:** `KSI-INR-01`
**Description:** Report incidents according to FedRAMP requirements and cloud service provider policies
**Justification:** Manual evidence required - incident reporting procedures, FedRAMP compliance documentation, and reporting policy alignment
**Last Validation:** ❌ 2025-06-06T05:52:21.557314
**Result:** ❌ No comprehensive incident reporting procedures found in evidence_v2/KSI-INR-01/

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-INR-01/ for incident_reporting_procedures.pdf, fedramp_incident_reporting_policy.pdf, incident_notification_templates.pdf, and regulatory_compliance_procedures.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-INR-01/ for incident_reporting_procedures.pdf, fedramp_incident_reporting_policy.pdf, incident_notification_templates.pdf, and regulatory_compliance_procedures.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_INR_01`

**Documentation:** KSI-INR-01: Report incidents according to FedRAMP requirements and cloud service provider policies

Expected: Manual evidence - incident reporting procedures and FedRAMP compliance

### Rule Implementation
```python
def evaluate_KSI_INR_01(cli_output):
    """
    KSI-INR-01: Report incidents according to FedRAMP requirements and cloud service provider policies
    
    Expected: Manual evidence - incident reporting procedures and FedRAMP compliance
    """
    evidence_dir = Path("evidence_v2/KSI-INR-01")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-INR-01/ not found"
    required_docs = [
        "incident_reporting_procedures.pdf",
        "fedramp_incident_reporting_policy.pdf",
        "incident_notification_templates.pdf"
    ]
    optional_docs = [
        "regulatory_compliance_procedures.pdf",
        "incident_escalation_matrix.pdf",
        "stakeholder_notification_procedures.pdf",
        "incident_severity_classification.pdf",
        "external_reporting_requirements.pdf",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Report incidents according to FedRAMP requirements and cloud service provider policies

**Implementation Justification:** Manual evidence required - incident reporting procedures, FedRAMP compliance documentation, and reporting policy alignment

**FedRAMP 20x Category:** Incident Reporting

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*