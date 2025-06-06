# KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

*Generated on 2025-06-06 05:34:53 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-01`
**Description:** Enforce phishing-resistant MFA for all user authentication
**Justification:** Validates that all IAM users have MFA enabled with phishing-resistant methods (hardware tokens, WebAuthn)
**Last Validation:** ❌ 2025-06-06T05:34:53.038313
**Result:** ❌ Only virtual MFA found (1 devices) - phishing-resistant MFA required

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-users --output json`
   **Purpose:** Get all IAM users

2. **Command:** `aws iam list-mfa-devices --output json`
   **Purpose:** Get all MFA devices to check types and assignments

3. **Command:** `aws iam list-virtual-mfa-devices --output json`
   **Purpose:** Get virtual MFA devices (less secure than hardware)

4. **Command:** `aws iam get-account-password-policy --output json`
   **Purpose:** Check password policy requirements

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-users --output json`
  - **Purpose:** Get all IAM users
- **Command:** `aws iam list-mfa-devices --output json`
  - **Purpose:** Get all MFA devices to check types and assignments
- **Command:** `aws iam list-virtual-mfa-devices --output json`
  - **Purpose:** Get virtual MFA devices (less secure than hardware)
- **Command:** `aws iam get-account-password-policy --output json`
  - **Purpose:** Check password policy requirements

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_01`

**Documentation:** KSI-IAM-01: Enforce multi-factor authentication (MFA) using methods that are 
difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication

Expected: IAM Users + MFA Devices

### Rule Implementation
```python
def evaluate_KSI_IAM_01(cli_output):
    """
    KSI-IAM-01: Enforce multi-factor authentication (MFA) using methods that are 
    difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication
    
    Expected: IAM Users + MFA Devices
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    users = None
    mfa_devices = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-users" in cli_command:
            users = raw_output.get("Users", [])
        elif "list-mfa-devices" in cli_command:
            mfa_devices = raw_output.get("MFADevices", [])
    if not users:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce phishing-resistant MFA for all user authentication

**Implementation Justification:** Validates that all IAM users have MFA enabled with phishing-resistant methods (hardware tokens, WebAuthn)

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/4 commands failed execution | 👤 3 IAM users found | 🔐 1 MFA devices detected | ✅ Command output received

**Commands Executed:** 4
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*