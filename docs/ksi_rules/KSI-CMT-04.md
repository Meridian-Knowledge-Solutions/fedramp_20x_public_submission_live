# KSI-CMT-04: Have a documented change management procedure

*Generated on 2025-06-10 12:33:14 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-04`
**Description:** Have a documented change management procedure
**Justification:** Validates comprehensive change management documentation capabilities from pilot to enterprise maturity levels through procedures, policies, governance, automation, and compliance evidence
**Last Validation:** ✅ 2025-06-10T12:33:14.268019
**Result:** ✅ Documented change management procedure - expand process controls (10%): ✅ Change management documentation found: configuration_management_policy_and_procedures.pdf, weekly_change_management_meeting_final.png

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CMT-04/ for comprehensive change management documentation

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CMT-04/ for comprehensive change management documentation

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_04`

**Documentation:** ENHANCED CMT-04: Have a documented change management procedure

Validates comprehensive change management documentation capabilities scaling from pilot to enterprise:
- Documentation Foundation: Basic change management procedures and policies
- Process Management: Templates, approval processes, and emergency procedures
- Advanced Governance: Change advisory board, risk assessment, and communication plans
- Automation Integration: Change tracking tools, workflow automation, and metrics
- Enterprise Governance: Organization-wide standards, continuous improvement, and compliance

Preserves current passing status while enabling maturity growth measurement.

### Rule Implementation
```python
def evaluate_KSI_CMT_04(cli_output):
    """
    ENHANCED CMT-04: Have a documented change management procedure
    
    Validates comprehensive change management documentation capabilities scaling from pilot to enterprise:
    - Documentation Foundation: Basic change management procedures and policies
    - Process Management: Templates, approval processes, and emergency procedures
    - Advanced Governance: Change advisory board, risk assessment, and communication plans
    - Automation Integration: Change tracking tools, workflow automation, and metrics
    - Enterprise Governance: Organization-wide standards, continuous improvement, and compliance
    
    Preserves current passing status while enabling maturity growth measurement.
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-04")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-04/ not found"
    findings = []
    change_management_score = 0  # Enhanced scoring for maturity measurement
    max_score = 20              # Enhanced scoring system for maturity measurement
    required_docs = [
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have a documented change management procedure

**Implementation Justification:** Validates comprehensive change management documentation capabilities from pilot to enterprise maturity levels through procedures, policies, governance, automation, and compliance evidence

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*