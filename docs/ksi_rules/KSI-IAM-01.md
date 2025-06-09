# KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

*Generated on 2025-06-09 08:59:31 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-01`
**Description:** Enforce phishing-resistant MFA for all user authentication
**Justification:** Validates MFA enforcement across traditional IAM and Identity Center with detailed user authentication analysis
**Last Validation:** ✅ 2025-06-09T08:59:31.451034
**Result:** ✅ Comprehensive MFA via Identity Center (centrally enforced): ✅ Identity Center: 1 active instance(s); ✅ Identity Center MFA: Centrally enforced (user enumeration requires permissions); Traditional IAM users: 3; Traditional IAM MFA devices: 1

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-users --output json`
   **Purpose:** Get traditional IAM users for MFA analysis

2. **Command:** `aws iam list-mfa-devices --output json`
   **Purpose:** Check traditional IAM MFA devices

3. **Command:** `aws sso-admin list-instances --output json`
   **Purpose:** Get Identity Center instances and Identity Store IDs

4. **Command:** `aws identitystore list-users --identity-store-id d-9067ccc0ff --output json`
   **Purpose:** Get Identity Center users for accurate user count

5. **Command:** `aws identitystore describe-user --identity-store-id d-9067ccc0ff --user-id $(aws identitystore list-users --identity-store-id d-9067ccc0ff --query 'Users[0].UserId' --output text) --output json`
   **Purpose:** Get detailed user authentication info to check for MFA device data

6. **Command:** `aws sso-admin describe-instance-access-control-attribute-configuration --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --output json`
   **Purpose:** Check Identity Center access control configuration for MFA requirements

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-users --output json`
  - **Purpose:** Get traditional IAM users for MFA analysis
- **Command:** `aws iam list-mfa-devices --output json`
  - **Purpose:** Check traditional IAM MFA devices
- **Command:** `aws sso-admin list-instances --output json`
  - **Purpose:** Get Identity Center instances and Identity Store IDs
- **Command:** `aws identitystore list-users --identity-store-id d-9067ccc0ff --output json`
  - **Purpose:** Get Identity Center users for accurate user count
- **Command:** `aws identitystore describe-user --identity-store-id d-9067ccc0ff --user-id $(aws identitystore list-users --identity-store-id d-9067ccc0ff --query 'Users[0].UserId' --output text) --output json`
  - **Purpose:** Get detailed user authentication info to check for MFA device data
- **Command:** `aws sso-admin describe-instance-access-control-attribute-configuration --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --output json`
  - **Purpose:** Check Identity Center access control configuration for MFA requirements

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_01`

**Documentation:** KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

Enhanced to get accurate Identity Center user counts and give proper credit

### Rule Implementation
```python
def evaluate_KSI_IAM_01(cli_output):
    """
    KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication
    
    Enhanced to get accurate Identity Center user counts and give proper credit
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    iam_users = []
    mfa_devices = []
    sso_instances = []
    identity_center_users = []
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        command_status = cmd.get("status", "")
        if "iam list-users" in cli_command:
            iam_users = raw_output.get("Users", [])
        elif "iam list-mfa-devices" in cli_command:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce phishing-resistant MFA for all user authentication

**Implementation Justification:** Validates MFA enforcement across traditional IAM and Identity Center with detailed user authentication analysis

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/6 commands failed execution | 👤 3 IAM users found | 🔐 1 MFA devices detected | ✅ Command output received

**Commands Executed:** 6
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*