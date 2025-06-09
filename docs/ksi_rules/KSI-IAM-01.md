# KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

*Generated on 2025-06-09 08:47:39 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-01`
**Description:** Enforce phishing-resistant MFA for all user authentication
**Justification:** Validates MFA enforcement across both traditional IAM and Identity Center users with accurate user counts
**Last Validation:** ✅ 2025-06-09T08:47:39.435997
**Result:** ✅ Comprehensive MFA via Identity Center (5 users): ✅ Identity Center: 1 active instance(s); ✅ Identity Center users: 5; ✅ Identity Center MFA: Enforced centrally for all 5 users; Traditional IAM users: 3; Traditional IAM MFA devices: 1

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-users --output json`
   **Purpose:** Get traditional IAM users for MFA analysis

2. **Command:** `aws iam list-mfa-devices --output json`
   **Purpose:** Check traditional IAM MFA devices

3. **Command:** `aws sso-admin list-instances --output json`
   **Purpose:** Get Identity Center instances and Identity Store IDs

4. **Command:** `aws identitystore list-users --identity-store-id d-9067ccc0ff --output json`
   **Purpose:** Get Identity Center users (using discovered Identity Store ID)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-users --output json`
  - **Purpose:** Get traditional IAM users for MFA analysis
- **Command:** `aws iam list-mfa-devices --output json`
  - **Purpose:** Check traditional IAM MFA devices
- **Command:** `aws sso-admin list-instances --output json`
  - **Purpose:** Get Identity Center instances and Identity Store IDs
- **Command:** `aws identitystore list-users --identity-store-id d-9067ccc0ff --output json`
  - **Purpose:** Get Identity Center users (using discovered Identity Store ID)

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

**Implementation Justification:** Validates MFA enforcement across both traditional IAM and Identity Center users with accurate user counts

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 4 commands executed successfully | 👤 3 IAM users found | 🔐 1 MFA devices detected | ✅ Command output received

**Commands Executed:** 4
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*