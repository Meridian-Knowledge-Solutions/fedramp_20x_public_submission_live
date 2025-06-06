# KSI-IAM-04: Use least-privileged, role-based, and just-in-time authorization

*Generated on 2025-06-06 04:21:09 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-04`
**Description:** Use least-privileged, role-based, and just-in-time authorization
**Justification:** Validates implementation of least privilege through roles, policies, and time-based access controls
**Last Validation:** ✅ 2025-06-06T04:21:09.291719
**Result:** ⚠️ Partial authorization model: ✅ Role-based access: 25 roles (2 admin, 13 service)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-roles --output json`
   **Purpose:** Get all roles for privilege analysis

2. **Command:** `aws iam list-policies --scope Local --output json`
   **Purpose:** Get custom policies to review permissions

3. **Command:** `aws iam list-attached-role-policies --role-name AdminRole --output json`
   **Purpose:** Check for overly permissive admin roles

4. **Command:** `aws iam generate-credential-report --output json`
   **Purpose:** Generate credential report for access analysis

5. **Command:** `aws iam get-credential-report --output text`
   **Purpose:** Get credential report data

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-roles --output json`
  - **Purpose:** Get all roles for privilege analysis
- **Command:** `aws iam list-policies --scope Local --output json`
  - **Purpose:** Get custom policies to review permissions
- **Command:** `aws iam list-attached-role-policies --role-name AdminRole --output json`
  - **Purpose:** Check for overly permissive admin roles
- **Command:** `aws iam generate-credential-report --output json`
  - **Purpose:** Generate credential report for access analysis
- **Command:** `aws iam get-credential-report --output text`
  - **Purpose:** Get credential report data

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_04`

**Documentation:** KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time 
security authorization model for all user and non-user accounts and services

Expected: IAM Roles + Current Session Context

### Rule Implementation
```python
def evaluate_KSI_IAM_04(cli_output):
    """
    KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time 
    security authorization model for all user and non-user accounts and services
    
    Expected: IAM Roles + Current Session Context
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    roles = None
    caller_identity = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-roles" in cli_command:
            roles = raw_output.get("Roles", [])
        elif "get-caller-identity" in cli_command:
            caller_identity = raw_output
    findings = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use least-privileged, role-based, and just-in-time authorization

**Implementation Justification:** Validates implementation of least privilege through roles, policies, and time-based access controls

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/5 commands failed execution | ✅ Command output received | ✅ Command output received | ⚠️ No usable output

**Commands Executed:** 5
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*