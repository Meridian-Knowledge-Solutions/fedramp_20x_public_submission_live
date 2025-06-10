# KSI-PIY-06: Have dedicated staff and budget for security with executive support

<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-10 13:17:42 UTC*
=======
*Generated on 2025-06-10 13:18:11 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 13:18:23 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-PIY-06`
**Description:** Have dedicated staff and budget for security with executive support
**Justification:** Manual evidence required - organizational structure, budget allocation, and executive endorsement
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T13:17:42.456950
=======
**Last Validation:** ✅ 2025-06-10T13:18:11.049259
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T13:18:23.546651
>>>>>>> Stashed changes
**Result:** ⚠️ Basic security organization (expand documentation): ✅ Security organization documentation: security_budget_allocation_and_roles.pdf

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-PIY-06/ for security_org_chart.pdf, security_budget_allocation.pdf, and executive_security_charter.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-PIY-06/ for security_org_chart.pdf, security_budget_allocation.pdf, and executive_security_charter.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_PIY_06`

**Documentation:** KSI-PIY-06: Have a dedicated staff and budget for security with executive support, 
commensurate with the size, complexity, scope, and risk of the service offering

Expected: Manual evidence - organizational and budget documentation

### Rule Implementation
```python
def evaluate_KSI_PIY_06(cli_output):
    """
    KSI-PIY-06: Have a dedicated staff and budget for security with executive support, 
    commensurate with the size, complexity, scope, and risk of the service offering
    
    Expected: Manual evidence - organizational and budget documentation
    """
    evidence_dir = Path("evidence_v2/KSI-PIY-06")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-PIY-06/ not found"
    required_docs = [
        "security_org_chart.pdf",
        "security_budget_allocation.pdf",
        "executive_security_charter.pdf"
    ]
    optional_docs = [
        "security_job_descriptions.pdf",
        "security_training_budget.pdf",
        "executive_security_commitment.pdf",
        "security_resource_justification.pdf"
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have dedicated staff and budget for security with executive support

**Implementation Justification:** Manual evidence required - organizational structure, budget allocation, and executive endorsement

**FedRAMP 20x Category:** Policy and Inventory

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*