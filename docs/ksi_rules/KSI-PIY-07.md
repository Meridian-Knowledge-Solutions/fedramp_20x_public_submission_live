# KSI-PIY-07: Document risk management decisions for software supply chain security

*Generated on 2025-06-06 06:36:35 UTC*

## 📖 Overview

**KSI ID:** `KSI-PIY-07`
**Description:** Document risk management decisions for software supply chain security
**Justification:** Manual evidence required - supply chain risk management documentation and decisions
**Last Validation:** ❌ 2025-06-06T06:36:35.354321
**Result:** ❌ No supply chain risk management documentation found in evidence_v2/KSI-PIY-07/

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-PIY-07/ for supply_chain_risk_management.pdf, vendor_security_assessments.pdf, and software_supply_chain_policy.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-PIY-07/ for supply_chain_risk_management.pdf, vendor_security_assessments.pdf, and software_supply_chain_policy.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_PIY_07`

**Documentation:** KSI-PIY-07: Document risk management decisions for software supply chain security

Expected: Manual evidence - supply chain risk management documentation

### Rule Implementation
```python
def evaluate_KSI_PIY_07(cli_output):
    """
    KSI-PIY-07: Document risk management decisions for software supply chain security
    
    Expected: Manual evidence - supply chain risk management documentation
    """
    evidence_dir = Path("evidence_v2/KSI-PIY-07")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-PIY-07/ not found"
    required_docs = [
        "supply_chain_risk_management.pdf",
        "vendor_security_assessments.pdf",
        "software_supply_chain_policy.pdf"
    ]
    optional_docs = [
        "third_party_risk_register.pdf",
        "supplier_security_requirements.pdf",
        "open_source_risk_analysis.pdf",
        "software_composition_analysis.pdf"
    ]
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Document risk management decisions for software supply chain security

**Implementation Justification:** Manual evidence required - supply chain risk management documentation and decisions

**FedRAMP 20x Category:** Policy and Inventory

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*