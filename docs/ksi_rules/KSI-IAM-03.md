# KSI-IAM-03: Enforce secure authentication for non-user accounts and services

*Generated on 2025-06-06 05:34:53 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-03`
**Description:** Enforce secure authentication for non-user accounts and services
**Justification:** Validates that service accounts, roles, and automated systems use appropriate authentication methods
**Last Validation:** ❌ 2025-06-06T05:34:53.048873
**Result:** ❌ Rule execution error: 'str' object has no attribute 'get'

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-roles --output json`
   **Purpose:** Get all IAM roles (service accounts)

2. **Command:** `aws iam list-instance-profiles --output json`
   **Purpose:** Get EC2 instance profiles for service authentication

3. **Command:** `aws sts get-caller-identity --output json`
   **Purpose:** Verify current authentication context

4. **Command:** `aws iam list-service-linked-roles --output json`
   **Purpose:** Check AWS service-linked roles

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-roles --output json`
  - **Purpose:** Get all IAM roles (service accounts)
- **Command:** `aws iam list-instance-profiles --output json`
  - **Purpose:** Get EC2 instance profiles for service authentication
- **Command:** `aws sts get-caller-identity --output json`
  - **Purpose:** Verify current authentication context
- **Command:** `aws iam list-service-linked-roles --output json`
  - **Purpose:** Check AWS service-linked roles

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_03`

**Documentation:** KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services

Expected: IAM Roles + Service-Linked Roles

### Rule Implementation
```python
def evaluate_KSI_IAM_03(cli_output):
    """
    KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services
    
    Expected: IAM Roles + Service-Linked Roles
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    roles = None
    service_linked_roles = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-roles" in cli_command and "service-linked" not in cli_command:
            roles = raw_output.get("Roles", [])
        elif "list-service-linked-roles" in cli_command:
            service_linked_roles = raw_output.get("Roles", [])
    if not roles and not service_linked_roles:
        return False, "❌ No IAM roles found for service authentication"
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce secure authentication for non-user accounts and services

**Implementation Justification:** Validates that service accounts, roles, and automated systems use appropriate authentication methods

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/4 commands failed execution | ✅ Command output received | ✅ Command output received | ✅ Command output received

**Commands Executed:** 4
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*