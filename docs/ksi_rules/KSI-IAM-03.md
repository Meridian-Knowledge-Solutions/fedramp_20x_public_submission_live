# KSI-IAM-03: Enforce secure authentication for non-user accounts and services

*Generated on 2025-06-09 09:44:44 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-03`
**Description:** Enforce secure authentication for non-user accounts and services
**Justification:** Validates service accounts use appropriate authentication methods (roles, not long-term keys)
**Last Validation:** ✅ 2025-06-09T09:44:44.696941
**Result:** ✅ Secure service authentication: ✅ 25 IAM roles (13 service-oriented)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-roles --output json`
   **Purpose:** Check IAM roles for service authentication

2. **Command:** `aws iam list-service-linked-roles --output json`
   **Purpose:** Validate AWS service-linked roles for secure service authentication

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-roles --output json`
  - **Purpose:** Check IAM roles for service authentication
- **Command:** `aws iam list-service-linked-roles --output json`
  - **Purpose:** Validate AWS service-linked roles for secure service authentication

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_03`

**Documentation:** Fixed rule for KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services
Expected: IAM Roles + Service-Linked Roles

### Rule Implementation
```python
def evaluate_KSI_IAM_03(cli_output):
    """
    Fixed rule for KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services
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
        if not isinstance(raw_output, dict):
            continue
        if "list-roles" in cli_command and "service-linked" not in cli_command:
            roles = raw_output.get("Roles", [])
        elif "list-service-linked-roles" in cli_command:
            service_linked_roles = raw_output.get("Roles", [])
    if not roles and not service_linked_roles:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce secure authentication for non-user accounts and services

**Implementation Justification:** Validates service accounts use appropriate authentication methods (roles, not long-term keys)

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*