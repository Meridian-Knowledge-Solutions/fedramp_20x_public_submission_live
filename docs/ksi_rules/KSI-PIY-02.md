# KSI-PIY-02: Have policies outlining the security objectives of all information resources

*Generated on 2025-06-06 09:11:10 UTC*

## 📖 Overview

**KSI ID:** `KSI-PIY-02`
**Description:** Have policies outlining the security objectives of all information resources
**Justification:** Manual evidence required - security policies and objectives documentation
**Last Validation:** ✅ 2025-06-06T09:11:09.823991
**Result:** ✅ Security policies outlining objectives: ✅ Core security policies: personnel_security_policy.pdf, data_classification_handling_policy.pdf, security_policy_collection_repository.zip

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-PIY-02/ for security_policy.pdf, information_security_objectives.pdf, and resource_security_standards.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-PIY-02/ for security_policy.pdf, information_security_objectives.pdf, and resource_security_standards.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_PIY_02`

**Documentation:** KSI-PIY-02: Have policies outlining the security objectives of all information resources

Expected: Manual evidence - security policies and objectives

### Rule Implementation
```python
def evaluate_KSI_PIY_02(cli_output):
    """
    KSI-PIY-02: Have policies outlining the security objectives of all information resources
    
    Expected: Manual evidence - security policies and objectives
    """
    evidence_dir = Path("evidence_v2/KSI-PIY-02")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-PIY-02/ not found"
    required_docs = [
        "personnel_security_policy.pdf",
        "data_classification_handling_policy.pdf",
        "security_policy_collection_repository.zip"
    ]
    optional_docs = [
        "data_classification_policy.pdf",
        "access_control_policy.pdf",
        "incident_response_policy.pdf",
        "security_governance_framework.pdf"
    ]
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have policies outlining the security objectives of all information resources

**Implementation Justification:** Manual evidence required - security policies and objectives documentation

**FedRAMP 20x Category:** Policy and Inventory

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*