# KSI-TPR-02: Regularly confirm services handling federal information are FedRAMP authorized and securely configured

*Generated on 2025-06-10 19:20:15 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-02`
**Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured
**Justification:** Validates FedRAMP authorization verification and secure configuration of federal information handling services with maturity-based assessment
**Last Validation:** ❌ 2025-06-10T19:20:15.300749
**Result:** Exception during evaluation: 'str' object has no attribute 'get'

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws organizations list-accounts --output json`
   **Purpose:** Check for organizational structure and account boundaries for federal information (graceful failure for single accounts)

2. **Command:** `aws config describe-configuration-recorders --output json`
   **Purpose:** Check for AWS Config compliance monitoring (Production tier: continuous monitoring)

3. **Command:** `aws config describe-compliance-by-config-rule --output json`
   **Purpose:** Check for active compliance rules monitoring FedRAMP requirements (Production tier)

4. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Check for audit logging capabilities for federal information access (Foundation tier)

5. **Command:** `aws sts get-caller-identity --output json`
   **Purpose:** Verify account identity and structure for federal information boundaries

6. **Command:** `aws iam list-roles --max-items 50 --output json`
   **Purpose:** Check for FedRAMP-related service roles and automated compliance roles (Advanced tier)

7. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-TPR-02/ for fedramp_authorization_verification.xlsx, service_security_configurations.pdf, federal_data_flow_analysis.pdf, and automation scripts

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws organizations list-accounts --output json`
  - **Purpose:** Check for organizational structure and account boundaries for federal information (graceful failure for single accounts)
- **Command:** `aws config describe-configuration-recorders --output json`
  - **Purpose:** Check for AWS Config compliance monitoring (Production tier: continuous monitoring)
- **Command:** `aws config describe-compliance-by-config-rule --output json`
  - **Purpose:** Check for active compliance rules monitoring FedRAMP requirements (Production tier)
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Check for audit logging capabilities for federal information access (Foundation tier)
- **Command:** `aws sts get-caller-identity --output json`
  - **Purpose:** Verify account identity and structure for federal information boundaries
- **Command:** `aws iam list-roles --max-items 50 --output json`
  - **Purpose:** Check for FedRAMP-related service roles and automated compliance roles (Advanced tier)

### 📄 Manual Evidence
- Check evidence_v2/KSI-TPR-02/ for fedramp_authorization_verification.xlsx, service_security_configurations.pdf, federal_data_flow_analysis.pdf, and automation scripts

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

**Implementation Justification:** Validates FedRAMP authorization verification and secure configuration of federal information handling services with maturity-based assessment

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 7 commands failed execution | ⚠️ No usable output

**Commands Executed:** 7
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*