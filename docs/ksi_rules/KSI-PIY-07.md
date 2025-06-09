# KSI-PIY-07: Document risk management decisions for software supply chain security

*Generated on 2025-06-09 04:29:09 UTC*

## 📖 Overview

**KSI ID:** `KSI-PIY-07`
**Description:** Document risk management decisions for software supply chain security
**Justification:** Manual evidence required - supply chain risk management documentation and decisions
**Last Validation:** ✅ 2025-06-09T04:29:09.614132
**Result:** ⚠️ Basic supply chain risk management (expand coverage): ✅ Enhanced supply chain controls: Software Supply Chain Risk Management Framework (KSI-PIY-07).pdf, weekly_change_management_meeting_final.png; ✅ Supply chain risk documentation: Software Supply Chain Risk Management Framework (KSI-PIY-07).pdf

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
        "Software Supply Chain Risk Management Framework (KSI-PIY-07).pdf",
        "weekly_change_management_meeting_final.png"
    ]
    found_required = []
    found_optional = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Document risk management decisions for software supply chain security

**Implementation Justification:** Manual evidence required - supply chain risk management documentation and decisions

**FedRAMP 20x Category:** Policy and Inventory

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*