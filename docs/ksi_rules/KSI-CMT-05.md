# KSI-CMT-05: Evaluate the risk and potential impact of any change

*Generated on 2025-06-06 11:48:54 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-05`
**Description:** Evaluate the risk and potential impact of any change
**Justification:** Manual evidence required - risk assessment procedures and impact analysis documentation
**Last Validation:** ❌ 2025-06-06T11:48:54.165592
**Result:** ❌ No risk and impact evaluation documentation found in evidence_v2/KSI-CMT-05/

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CMT-05/ for risk_assessment_procedure.pdf and change_impact_analysis_template.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CMT-05/ for risk_assessment_procedure.pdf and change_impact_analysis_template.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_05`

**Documentation:** KSI-CMT-05: Evaluate the risk and potential impact of any change

Expected: Manual evidence - risk assessment documentation

### Rule Implementation
```python
def evaluate_KSI_CMT_05(cli_output):
    """
    KSI-CMT-05: Evaluate the risk and potential impact of any change
    
    Expected: Manual evidence - risk assessment documentation
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-05")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-05/ not found"
    required_docs = [
        "risk_assessment_procedure.pdf",
        "change_impact_analysis_template.pdf",
        "risk_evaluation_matrix.pdf"
    ]
    optional_docs = [
        "change_risk_register.pdf",
        "impact_assessment_examples.pdf",
        "rollback_procedures.pdf"
    ]
    found_required = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Evaluate the risk and potential impact of any change

**Implementation Justification:** Manual evidence required - risk assessment procedures and impact analysis documentation

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*