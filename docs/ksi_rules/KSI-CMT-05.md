# KSI-CMT-05: Evaluate the risk and potential impact of any change

*Generated on 2025-06-15 03:24:19 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-05`
**Description:** Evaluate the risk and potential impact of any change
**Justification:** Validates comprehensive risk and impact evaluation capabilities from pilot to enterprise maturity levels through assessment procedures, quantitative analysis, governance, automation, and compliance evidence
**Last Validation:** ✅ 2025-06-15T03:24:19.389555
**Result:** ✅ Risk and impact evaluation procedures - expand analysis methods (10%): ✅ Risk evaluation documentation found: Change Impact Analysis Template (KSI-CMT-05).pdf, Risk Assessment Procedure for Change Management (KSI-CMT-05).pdf

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CMT-05/ for comprehensive risk and impact evaluation documentation

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CMT-05/ for comprehensive risk and impact evaluation documentation

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_05`

**Documentation:** ENHANCED CMT-05: Evaluate the risk and potential impact of any change

Validates comprehensive risk and impact evaluation capabilities scaling from pilot to enterprise:
- Risk Assessment Foundation: Basic risk procedures and impact analysis templates
- Advanced Risk Management: Risk matrices, registers, and quantitative analysis methods
- Risk Governance: Risk committees, escalation procedures, and stakeholder communication
- Risk Automation: Risk assessment tools, automated scoring, and integrated workflows
- Enterprise Risk Management: Organization-wide standards, continuous monitoring, and compliance

Preserves current passing status while enabling maturity growth measurement.

### Rule Implementation
```python
def evaluate_KSI_CMT_05(cli_output):
    """
    ENHANCED CMT-05: Evaluate the risk and potential impact of any change
    
    Validates comprehensive risk and impact evaluation capabilities scaling from pilot to enterprise:
    - Risk Assessment Foundation: Basic risk procedures and impact analysis templates
    - Advanced Risk Management: Risk matrices, registers, and quantitative analysis methods
    - Risk Governance: Risk committees, escalation procedures, and stakeholder communication
    - Risk Automation: Risk assessment tools, automated scoring, and integrated workflows
    - Enterprise Risk Management: Organization-wide standards, continuous monitoring, and compliance
    
    Preserves current passing status while enabling maturity growth measurement.
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-05")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-05/ not found"
    findings = []
    risk_evaluation_score = 0  # Enhanced scoring for maturity measurement
    max_score = 20            # Enhanced scoring system for maturity measurement
    required_docs = [
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Evaluate the risk and potential impact of any change

**Implementation Justification:** Validates comprehensive risk and impact evaluation capabilities from pilot to enterprise maturity levels through assessment procedures, quantitative analysis, governance, automation, and compliance evidence

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*