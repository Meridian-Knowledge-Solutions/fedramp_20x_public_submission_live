# KSI-IAM-02: Use secure passwordless methods or strong passwords with MFA

<<<<<<< Updated upstream
*Generated on 2025-06-09 07:55:36 UTC*
=======
*Generated on 2025-06-09 07:55:55 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-IAM-02`
**Description:** Use secure passwordless methods or strong passwords with MFA
**Justification:** Validates passwordless authentication where feasible, otherwise strong password policy with MFA
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-09T07:55:36.268477
=======
**Last Validation:** ✅ 2025-06-09T07:55:55.136247
>>>>>>> Stashed changes
**Result:** ⚠️ Basic secure authentication (needs improvement): ✅ 1 active access keys for passwordless programmatic access; ❌ Password policy information not accessible

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam get-account-password-policy --output json`
   **Purpose:** Check strong password policy enforcement

2. **Command:** `aws iam list-access-keys --output json`
   **Purpose:** Check for passwordless methods (access keys vs console passwords)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam get-account-password-policy --output json`
  - **Purpose:** Check strong password policy enforcement
- **Command:** `aws iam list-access-keys --output json`
  - **Purpose:** Check for passwordless methods (access keys vs console passwords)

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_02`

**Documentation:** FIXED: KSI-IAM-02: Use secure passwordless methods for user authentication and authorization 
when feasible, otherwise enforce strong passwords with MFA

ERROR FIX: Handles 'str' object has no attribute 'get' by adding robust type checking

### Rule Implementation
```python
def evaluate_KSI_IAM_02(cli_output):
    """
    FIXED: KSI-IAM-02: Use secure passwordless methods for user authentication and authorization 
    when feasible, otherwise enforce strong passwords with MFA
    
    ERROR FIX: Handles 'str' object has no attribute 'get' by adding robust type checking
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    password_policy = None
    access_keys = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output")
        try:
            if isinstance(raw_output, str):
                if "get-account-password-policy" in cli_command:
                    if any(error in raw_output for error in [
                        "NoSuchEntity",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use secure passwordless methods or strong passwords with MFA

**Implementation Justification:** Validates passwordless authentication where feasible, otherwise strong password policy with MFA

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*