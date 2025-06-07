# KSI-INR-03: Generate after action reports and regularly incorporate lessons learned into operations

*Generated on 2025-06-07 20:27:06 UTC*

## 📖 Overview

**KSI ID:** `KSI-INR-03`
**Description:** Generate after action reports and regularly incorporate lessons learned into operations
**Justification:** Manual evidence required - after action reports, lessons learned documentation, and operational improvement tracking
**Last Validation:** ✅ 2025-06-07T20:27:06.615975
**Result:** ⚠️ Basic after action reporting (increase lessons learned implementation): ✅ Core after action documentation: Sample After Action Reports and Implementation Examples.pdf; ✅ Recent after action reports: 2 AARs within last year; ⚠️ Limited evidence of lessons learned implementation into operations

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-INR-03/ for after_action_reports.pdf, lessons_learned_database.xlsx, operational_improvements_tracking.pdf, and incident_response_improvements.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-INR-03/ for after_action_reports.pdf, lessons_learned_database.xlsx, operational_improvements_tracking.pdf, and incident_response_improvements.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_INR_03`

**Documentation:** KSI-INR-03: Generate after action reports and regularly incorporate lessons learned into operations

Expected: Manual evidence - after action reports and lessons learned integration

### Rule Implementation
```python
def evaluate_KSI_INR_03(cli_output):
    """
    KSI-INR-03: Generate after action reports and regularly incorporate lessons learned into operations
    
    Expected: Manual evidence - after action reports and lessons learned integration
    """
    evidence_dir = Path("evidence_v2/KSI-INR-03")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-INR-03/ not found"
    required_docs = [
        "After Action Report and Lessons Learned Framework (KSI-INR-03)",
        "Sample After Action Reports and Implementation Examples.pdf"
    ]
    optional_docs = [
        "incident_response_improvements.pdf",
        "post_incident_review_templates.pdf",
        "lessons_learned_implementation_log.xlsx",
        "process_improvement_recommendations.pdf",
        "training_updates_from_incidents.pdf",
        "policy_updates_from_lessons_learned.pdf"
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Generate after action reports and regularly incorporate lessons learned into operations

**Implementation Justification:** Manual evidence required - after action reports, lessons learned documentation, and operational improvement tracking

**FedRAMP 20x Category:** Incident Reporting

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*