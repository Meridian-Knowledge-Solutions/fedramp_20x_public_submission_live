# KSI-TPR-03: Identify and prioritize mitigation of potential supply chain risks

*Generated on 2025-06-06 11:15:22 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-03`
**Description:** Identify and prioritize mitigation of potential supply chain risks
**Justification:** Manual evidence required - supply chain risk assessment and mitigation planning
**Last Validation:** ❌ 2025-06-06T11:15:22.137577
**Result:** ❌ No supply chain risk assessment and mitigation found in evidence_v2/KSI-TPR-03/

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-TPR-03/ for supply_chain_risk_assessment.pdf, risk_mitigation_plan.pdf, and vendor_risk_matrix.xlsx

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-TPR-03/ for supply_chain_risk_assessment.pdf, risk_mitigation_plan.pdf, and vendor_risk_matrix.xlsx

## 🧠 Validation Logic

**Function:** `evaluate_KSI_TPR_03`

**Documentation:** KSI-TPR-03: Identify and prioritize mitigation of potential supply chain risks

Expected: Manual evidence - supply chain risk assessment and mitigation

### Rule Implementation
```python
def evaluate_KSI_TPR_03(cli_output):
    """
    KSI-TPR-03: Identify and prioritize mitigation of potential supply chain risks
    
    Expected: Manual evidence - supply chain risk assessment and mitigation
    """
    evidence_dir = Path("evidence_v2/KSI-TPR-03")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-TPR-03/ not found"
    required_docs = [
        "supply_chain_risk_assessment.pdf",
        "risk_mitigation_plan.pdf",
        "vendor_risk_matrix.xlsx"
    ]
    optional_docs = [
        "supply_chain_threat_analysis.pdf",
        "third_party_risk_register.pdf",
        "vendor_security_scorecards.xlsx",
        "supply_chain_incident_response.pdf"
    ]
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Identify and prioritize mitigation of potential supply chain risks

**Implementation Justification:** Manual evidence required - supply chain risk assessment and mitigation planning

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*