# KSI-TPR-02: Regularly confirm services handling federal information are FedRAMP authorized and securely configured

*Generated on 2025-06-09 08:59:31 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-02`
**Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured
**Justification:** Validates FedRAMP authorization verification and secure configuration of federal information handling services
**Last Validation:** ✅ 2025-06-09T08:59:31.454553
**Result:** ✅ Services handling federal information verified FedRAMP authorized: ✅ Organizational structure: 14 accounts for federal information boundary management; ✅ FedRAMP verification documentation: FedRAMP_Low_Boundary_Diagram.pdf

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws organizations list-accounts --output json`
   **Purpose:** Check for organizational structure and account boundaries for federal information

2. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-TPR-02/ for fedramp_authorization_verification.xlsx, service_security_configurations.pdf, and federal_data_flow_analysis.pdf

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws organizations list-accounts --output json`
  - **Purpose:** Check for organizational structure and account boundaries for federal information

### 📄 Manual Evidence
- Check evidence_v2/KSI-TPR-02/ for fedramp_authorization_verification.xlsx, service_security_configurations.pdf, and federal_data_flow_analysis.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_TPR_02`

**Documentation:** KSI-TPR-02: Regularly confirm that services handling federal information or are likely 
to impact the confidentiality, integrity, or availability of federal information are 
FedRAMP authorized and securely configured

Expected: Organization accounts + FedRAMP verification documentation

### Rule Implementation
```python
def evaluate_KSI_TPR_02(cli_output):
    """
    KSI-TPR-02: Regularly confirm that services handling federal information or are likely 
    to impact the confidentiality, integrity, or availability of federal information are 
    FedRAMP authorized and securely configured
    
    Expected: Organization accounts + FedRAMP verification documentation
    """
    evidence_dir = Path("evidence_v2/KSI-TPR-02")
    org_accounts = None
    if "commands" in cli_output:
        for cmd in cli_output["commands"]:
            cli_command = cmd.get("cli_command", "")
            raw_output = cmd.get("raw_output", {})
            if "list-accounts" in cli_command:
                org_accounts = raw_output.get("Accounts", [])
    manual_evidence = []
    if evidence_dir.exists():
        fedramp_files = [
            "fedramp_authorization_verification.xlsx",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured

**Implementation Justification:** Validates FedRAMP authorization verification and secure configuration of federal information handling services

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | 📄 Manual evidence validation

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*