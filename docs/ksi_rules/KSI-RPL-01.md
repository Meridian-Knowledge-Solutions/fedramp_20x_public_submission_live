# KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-10 12:33:14 UTC*
=======
*Generated on 2025-06-10 12:33:33 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 12:33:42 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 12:33:51 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-RPL-01`
**Description:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)
**Justification:** Manual evidence required - documented RTO/RPO definitions and business impact analysis
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T12:33:14.279095
=======
**Last Validation:** ✅ 2025-06-10T12:33:32.890894
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:33:41.780677
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:33:51.383976
>>>>>>> Stashed changes
**Result:** ⚠️ Basic RTO/RPO definitions (expand business impact analysis): ✅ Core RTO/RPO documentation: rto_rpo_definitions.pdf, combined_tabletop_test_report_template.pdf

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-RPL-01/ for rto_rpo_definitions.pdf, business_impact_analysis.pdf, and recovery_objectives_matrix.xlsx

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-RPL-01/ for rto_rpo_definitions.pdf, business_impact_analysis.pdf, and recovery_objectives_matrix.xlsx

## 🧠 Validation Logic

**Function:** `evaluate_KSI_RPL_01`

**Documentation:** KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

Expected: Manual evidence - RTO/RPO definitions and business impact analysis

### Rule Implementation
```python
def evaluate_KSI_RPL_01(cli_output):
    """
    KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)
    
    Expected: Manual evidence - RTO/RPO definitions and business impact analysis
    """
    evidence_dir = Path("evidence_v2/KSI-RPL-01")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-RPL-01/ not found"
    required_docs = [
        "rto_rpo_definitions.pdf",
        "combined_tabletop_test_report_template.pdf"
    ]
    optional_docs = [
        "service_level_agreements.pdf",
        "criticality_assessment.pdf",
        "recovery_time_analysis.pdf",
        "data_loss_tolerance_matrix.xlsx",
        "business_continuity_requirements.pdf"
    ]
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)

**Implementation Justification:** Manual evidence required - documented RTO/RPO definitions and business impact analysis

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*