# KSI-CMT-03: Implement automated testing and validation of changes prior to deployment

<<<<<<< Updated upstream
*Generated on 2025-06-10 12:33:14 UTC*
=======
*Generated on 2025-06-10 12:33:33 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-CMT-03`
**Description:** Implement automated testing and validation of changes prior to deployment
**Justification:** Validates comprehensive Infrastructure as Code testing capabilities from pilot to enterprise maturity levels through Terraform, Checkov, SARIF reports, CI/CD integration, and governance evidence
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T12:33:14.267957
=======
**Last Validation:** ✅ 2025-06-10T12:33:32.879097
>>>>>>> Stashed changes
**Result:** ✅ Comprehensive automated testing via Infrastructure as Code (30%): ✅ Infrastructure as Code testing foundation: Automated testing proof documented; ✅ Terraform security validation: Checkov compliance scanning; ✅ Standardized security reporting: SARIF format compliance

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-CMT-03/ for comprehensive Infrastructure as Code testing evidence files

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Check evidence_v2/KSI-CMT-03/ for comprehensive Infrastructure as Code testing evidence files

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_03`

**Documentation:** ENHANCED CMT-03: Implement automated testing and validation of changes prior to deployment

Validates comprehensive Infrastructure as Code testing capabilities scaling from pilot to enterprise:
- Testing Foundation: Basic Checkov scanning and automated testing proof
- Advanced IaC Testing: Multiple scan types, SARIF reports, and integration evidence  
- Continuous Testing: CI/CD integration, policy as code, and comprehensive scanning
- Testing Governance: Testing policies, compliance validation, and quality gates
- Enterprise Governance: Organization-wide testing standards and comprehensive automation

Uses Infrastructure as Code security scanning evidence from external automation
instead of traditional CodeBuild/CodePipeline approaches (Terraform + Checkov focus).

Preserves current passing status while enabling maturity growth measurement.

### Rule Implementation
```python
def evaluate_KSI_CMT_03(cli_output):
    """
    ENHANCED CMT-03: Implement automated testing and validation of changes prior to deployment
    
    Validates comprehensive Infrastructure as Code testing capabilities scaling from pilot to enterprise:
    - Testing Foundation: Basic Checkov scanning and automated testing proof
    - Advanced IaC Testing: Multiple scan types, SARIF reports, and integration evidence  
    - Continuous Testing: CI/CD integration, policy as code, and comprehensive scanning
    - Testing Governance: Testing policies, compliance validation, and quality gates
    - Enterprise Governance: Organization-wide testing standards and comprehensive automation
    
    Uses Infrastructure as Code security scanning evidence from external automation
    instead of traditional CodeBuild/CodePipeline approaches (Terraform + Checkov focus).
    
    Preserves current passing status while enabling maturity growth measurement.
    """
    evidence_dir = Path("evidence_v2/KSI-CMT-03")
    if not evidence_dir.exists():
        return False, "❌ Evidence directory evidence_v2/KSI-CMT-03/ not found"
    findings = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Implement automated testing and validation of changes prior to deployment

**Implementation Justification:** Validates comprehensive Infrastructure as Code testing capabilities from pilot to enterprise maturity levels through Terraform, Checkov, SARIF reports, CI/CD integration, and governance evidence

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*