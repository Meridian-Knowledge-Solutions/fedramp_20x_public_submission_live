# KSI-CMT-05: Evaluate the risk and potential impact of any change

*Generated on 2025-06-10 04:03:19 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-05`
**Description:** Evaluate the risk and potential impact of any change
**Justification:** Manual evidence required - risk assessment procedures and impact analysis documentation
**Last Validation:** ✅ 2025-06-10T04:03:18.705278
**Result:** ✅ Risk and impact evaluation procedures: ✅ Required documentation: Change Impact Analysis Template (KSI-CMT-05).pdf, Risk Assessment Procedure for Change Management (KSI-CMT-05).pdf

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
        "Change Impact Analysis Template (KSI-CMT-05).pdf",
        "Risk Assessment Procedure for Change Management (KSI-CMT-05).pdf"
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

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*