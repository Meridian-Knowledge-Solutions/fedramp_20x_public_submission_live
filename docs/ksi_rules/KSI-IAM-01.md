# KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

*Generated on 2025-06-09 09:09:47 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-01`
**Description:** Enforce phishing-resistant MFA for all user authentication
**Justification:** Validates MFA enforcement across traditional IAM and Identity Center by checking actual permission set policies for MFA requirements
**Last Validation:** ✅ 2025-06-09T09:09:47.698195
**Result:** ✅ Comprehensive MFA enforcement (6 users protected): ✅ Identity Center: 1 active instance(s); ✅ Identity Center users: 5; ✅ Centralized MFA enforcement for all 5 Identity Center users; Traditional IAM users: 3; Traditional IAM MFA devices: 1

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

5. **Command:** `aws sso-admin list-permission-sets --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --output json`
   **Purpose:** Get permission sets to check for MFA enforcement policies

6. **Command:** `aws sso-admin describe-permission-set --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --permission-set-arn $(aws sso-admin list-permission-sets --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --query 'PermissionSets[0]' --output text) --output json`
   **Purpose:** Check first permission set details for MFA requirements

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
- **Command:** `aws sso-admin list-permission-sets --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --output json`
  - **Purpose:** Get permission sets to check for MFA enforcement policies
- **Command:** `aws sso-admin describe-permission-set --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --permission-set-arn $(aws sso-admin list-permission-sets --instance-arn arn:aws:sso:::instance/ssoins-72233f35277a1dff --query 'PermissionSets[0]' --output text) --output json`
  - **Purpose:** Check first permission set details for MFA requirements

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_01`

**Documentation:** KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

Recognizes Identity Center centralized MFA enforcement with accurate user counts

### Rule Implementation
```python
def evaluate_KSI_IAM_01(cli_output):
    """
    KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication
    
    Recognizes Identity Center centralized MFA enforcement with accurate user counts
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
        if "iam list-users" in cli_command and command_status == "success":
            iam_users = raw_output.get("Users", [])
        elif "iam list-mfa-devices" in cli_command and command_status == "success":
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce phishing-resistant MFA for all user authentication

**Implementation Justification:** Validates MFA enforcement across traditional IAM and Identity Center by checking actual permission set policies for MFA requirements

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 6 commands executed successfully | 👤 3 IAM users found | 🔐 1 MFA devices detected | ✅ Command output received

**Commands Executed:** 6
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*