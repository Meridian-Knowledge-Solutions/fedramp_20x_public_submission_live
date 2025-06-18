# KSI-TPR-04: Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

*Generated on 2025-06-18 04:28:40 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-04`
**Description:** Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring
**Justification:** Validates vulnerability monitoring through Inspector, Security Hub, and contractual requirements documentation
**Last Validation:** ✅ 2025-06-18T04:28:40.213636
**Result:** ✅ Third-party software vulnerability monitoring established: ✅ Active third-party vulnerability monitoring: 20 component vulnerabilities detected; ✅ Manual evidence validation completed (vulnerability monitoring documentation verified)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws inspector2 list-findings --max-results 20 --output json`
   **Purpose:** Check Inspector findings for third-party component vulnerabilities

2. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-TPR-04/ for vulnerability_monitoring_contracts.pdf, upstream_vulnerability_procedures.pdf, and third_party_notification_agreements.pdf

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws inspector2 list-findings --max-results 20 --output json`
  - **Purpose:** Check Inspector findings for third-party component vulnerabilities

### 📄 Manual Evidence
- Check evidence_v2/KSI-TPR-04/ for vulnerability_monitoring_contracts.pdf, upstream_vulnerability_procedures.pdf, and third_party_notification_agreements.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_TPR_04`

**Documentation:** FINAL FIX: KSI-TPR-04: Monitor third party software information resources for upstream vulnerabilities,
with contractual notification requirements or active monitoring services

FIX: Handle Inspector command failures + recognize evidence_check responses

### Rule Implementation
```python
def evaluate_KSI_TPR_04(cli_output):
    """
    FINAL FIX: KSI-TPR-04: Monitor third party software information resources for upstream vulnerabilities,
    with contractual notification requirements or active monitoring services
    
    FIX: Handle Inspector command failures + recognize evidence_check responses
    """
    evidence_dir = Path("evidence_v2/KSI-TPR-04")
    inspector_findings = None
    inspector_service_available = False
    inspector_command_failed = False
    evidence_check_passed = False
    if "commands" in cli_output:
        for cmd in cli_output["commands"]:
            cli_command = cmd.get("cli_command", "")
            raw_output = cmd.get("raw_output", {})
            command_status = cmd.get("status", "")
            if "inspector" in cli_command and "list-findings" in cli_command:
                if command_status == "failure":
                    inspector_command_failed = True
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

**Implementation Justification:** Validates vulnerability monitoring through Inspector, Security Hub, and contractual requirements documentation

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*