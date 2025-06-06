# KSI-TPR-04: Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

*Generated on 2025-06-06 06:57:45 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-04`
**Description:** Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring
**Justification:** Validates vulnerability monitoring through Inspector, Security Hub, and contractual requirements documentation
**Last Validation:** ❌ 2025-06-06T06:57:45.552952
**Result:** ❌ No comprehensive third-party vulnerability monitoring: ❌ No Inspector vulnerability monitoring data; ❌ No contractual vulnerability notification agreements found

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws inspector2 list-findings --filter-criteria '{"component":[{"comparison":"EQUALS","value":"*"}]}' --max-results 20 --output json`
   **Purpose:** Check Inspector findings for third-party component vulnerabilities

2. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-TPR-04/ for vulnerability_monitoring_contracts.pdf, upstream_vulnerability_procedures.pdf, and third_party_notification_agreements.pdf

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws inspector2 list-findings --filter-criteria '{"component":[{"comparison":"EQUALS","value":"*"}]}' --max-results 20 --output json`
  - **Purpose:** Check Inspector findings for third-party component vulnerabilities

### 📄 Manual Evidence
- Check evidence_v2/KSI-TPR-04/ for vulnerability_monitoring_contracts.pdf, upstream_vulnerability_procedures.pdf, and third_party_notification_agreements.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_TPR_04`

**Documentation:** Fixed rule for KSI-TPR-04: Monitor third party software information resources for upstream vulnerabilities
Expected: Inspector findings + Vulnerability monitoring contracts

### Rule Implementation
```python
def evaluate_KSI_TPR_04(cli_output):
    """
    Fixed rule for KSI-TPR-04: Monitor third party software information resources for upstream vulnerabilities
    Expected: Inspector findings + Vulnerability monitoring contracts
    """
    evidence_dir = Path("evidence_v2/KSI-TPR-04")
    inspector_findings = None
    if "commands" in cli_output:
        for cmd in cli_output["commands"]:
            cli_command = cmd.get("cli_command", "")
            raw_output = cmd.get("raw_output", {})
            if not isinstance(raw_output, dict):
                continue
            if "list-findings" in cli_command and "inspector" in cli_command:
                inspector_findings = raw_output.get("findings", [])
    manual_evidence = []
    if evidence_dir.exists():
        monitoring_files = [
            "vulnerability_monitoring_contracts.pdf",
            "upstream_vulnerability_procedures.pdf",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

**Implementation Justification:** Validates vulnerability monitoring through Inspector, Security Hub, and contractual requirements documentation

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 📄 Manual evidence validation

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*