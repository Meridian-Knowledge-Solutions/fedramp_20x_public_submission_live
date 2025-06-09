# KSI-IAM-04: Use least-privileged, role-based, and just-in-time authorization

*Generated on 2025-06-09 04:38:29 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-04`
**Description:** Use least-privileged, role-based, and just-in-time authorization
**Justification:** Validates least privilege implementation through roles, policies, and time-based access controls
**Last Validation:** ✅ 2025-06-09T04:38:29.318513
**Result:** ⚠️ Partial authorization model: ✅ Role-based access: 25 roles (3 admin, 14 service); ⚠️ Direct user access detected (not session-based)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-roles --output json`
   **Purpose:** Analyze roles for least privilege implementation

2. **Command:** `aws sts get-caller-identity --output json`
   **Purpose:** Validate current session-based access (just-in-time principle)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-roles --output json`
  - **Purpose:** Analyze roles for least privilege implementation
- **Command:** `aws sts get-caller-identity --output json`
  - **Purpose:** Validate current session-based access (just-in-time principle)

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

**Implementation Justification:** Validates least privilege implementation through roles, policies, and time-based access controls

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*