# KSI-TPR-02: Regularly confirm services handling federal information are FedRAMP authorized and securely configured

<<<<<<< Updated upstream
<<<<<<< Updated upstream
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
=======
*Generated on 2025-06-10 12:34:10 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 12:34:14 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-TPR-02`
**Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured
**Justification:** Validates FedRAMP authorization verification and secure configuration of federal information handling services
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T12:33:14.281535
=======
**Last Validation:** ✅ 2025-06-10T12:33:32.893625
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:33:41.783070
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:33:51.386527
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:34:09.977638
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:34:14.228275
>>>>>>> Stashed changes
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

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*