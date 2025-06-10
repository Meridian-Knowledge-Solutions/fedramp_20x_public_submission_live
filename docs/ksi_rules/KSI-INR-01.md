# KSI-INR-01: Report incidents according to FedRAMP requirements and cloud service provider policies

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-10 13:17:42 UTC*
=======
*Generated on 2025-06-10 13:18:11 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:23 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:26 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:59 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:19:04 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-INR-01`
**Description:** Report incidents according to FedRAMP requirements and cloud service provider policies
**Justification:** Manual evidence required - incident reporting procedures, FedRAMP compliance documentation, and reporting policy alignment
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T13:17:42.449206
=======
**Last Validation:** ✅ 2025-06-10T13:18:11.041043
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:23.539321
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:26.129359
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:58.714505
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:19:04.384183
>>>>>>> Stashed changes
**Result:** ⚠️ Basic incident reporting (ensure FedRAMP compliance): ✅ Core reporting procedures: quick_reference_irp_guide.pdf, incident_reponse_policy.pdf, contingency_plan.pdf; ✅ Enhanced compliance procedures: IR.zip; ❌ No specific FedRAMP incident reporting compliance found (required)

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
        "quick_reference_irp_guide.pdf",
        "incident_reponse_policy.pdf",
        "contingency_plan.pdf"
    ]
    optional_docs = [
        "IR.zip",
    ]
    found_required = []
    found_optional = []
    for doc in required_docs:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Report incidents according to FedRAMP requirements and cloud service provider policies

**Implementation Justification:** Manual evidence required - incident reporting procedures, FedRAMP compliance documentation, and reporting policy alignment

**FedRAMP 20x Category:** Incident Reporting

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*