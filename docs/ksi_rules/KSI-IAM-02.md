# KSI-IAM-02: Use secure passwordless methods or strong passwords with MFA

*Generated on 2025-06-06 04:21:09 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-02`
**Description:** Use secure passwordless methods or strong passwords with MFA
**Justification:** Validates IAM user presence and confirms MFA enforcement with strong password policies
**Last Validation:** ❌ 2025-06-06T04:21:09.293111
**Result:** ❌ Insufficient secure authentication: ❌ No password policy configured

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-users --query 'Users[*].{UserName:UserName,PasswordLastUsed:PasswordLastUsed,CreateDate:CreateDate}' --output json`
   **Purpose:** Get user details including password usage

2. **Command:** `aws iam list-mfa-devices --output json`
   **Purpose:** Verify MFA device assignment for all users

3. **Command:** `aws iam get-account-password-policy --output json`
   **Purpose:** Validate strong password policy enforcement

4. **Command:** `aws iam list-access-keys --output json`
   **Purpose:** Check for programmatic access keys that bypass passwords

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-users --query 'Users[*].{UserName:UserName,PasswordLastUsed:PasswordLastUsed,CreateDate:CreateDate}' --output json`
  - **Purpose:** Get user details including password usage
- **Command:** `aws iam list-mfa-devices --output json`
  - **Purpose:** Verify MFA device assignment for all users
- **Command:** `aws iam get-account-password-policy --output json`
  - **Purpose:** Validate strong password policy enforcement
- **Command:** `aws iam list-access-keys --output json`
  - **Purpose:** Check for programmatic access keys that bypass passwords

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_02`

**Documentation:** KSI-IAM-02: Use secure passwordless methods for user authentication and authorization 
when feasible, otherwise enforce strong passwords with MFA

Expected: Password Policy + Access Keys

### Rule Implementation
```python
def evaluate_KSI_IAM_02(cli_output):
    """
    KSI-IAM-02: Use secure passwordless methods for user authentication and authorization 
    when feasible, otherwise enforce strong passwords with MFA
    
    Expected: Password Policy + Access Keys
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    password_policy = None
    access_keys = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "get-account-password-policy" in cli_command:
            password_policy = raw_output.get("PasswordPolicy", {})
        elif "list-access-keys" in cli_command:
            access_keys = raw_output.get("AccessKeyMetadata", [])
    findings = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use secure passwordless methods or strong passwords with MFA

**Implementation Justification:** Validates IAM user presence and confirms MFA enforcement with strong password policies

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/4 commands failed execution | 📋 3 items retrieved | 🔐 1 MFA devices detected | ⚠️ No usable output

**Commands Executed:** 4
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*