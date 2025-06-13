# KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services

*Generated on 2025-06-13 17:07:48 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-04`
**Description:** Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services
**Justification:** Validates comprehensive authorization through IAM Identity Center permission sets (modern approach) and traditional IAM patterns for complete coverage of least privilege, role-based, attribute-based, and just-in-time access
**Last Validation:** ✅ 2025-06-13T17:07:48.415742
**Result:** ⚠️ Minimal authorization controls (35%): ℹ️ IAM Identity Center not configured (using traditional IAM); ✅ Traditional role-based access: 50 roles (24 service, 26 user-oriented) vs 2 users; ✅ Controlled user count: 2 users (appropriate for least privilege); ✅ Controlled policy count: 1 custom policies; ⚠️ Unknown credential type

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws sso-admin list-instances --output json`
   **Purpose:** Check for AWS IAM Identity Center (modern permission set approach)

2. **Command:** `aws sso-admin list-permission-sets --instance-arn $(aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text) --output json 2>/dev/null || echo '{"PermissionSets":[]}'`
   **Purpose:** List permission sets for role-based and attribute-based access validation

3. **Command:** `aws iam list-roles --output json`
   **Purpose:** Analyze traditional IAM roles for service accounts and legacy access patterns

4. **Command:** `aws iam list-users --output json`
   **Purpose:** Check if users have direct policy attachments (anti-pattern for least privilege)

5. **Command:** `aws sts get-caller-identity --output json`
   **Purpose:** Validate current session type (permission set session vs traditional credentials)

6. **Command:** `aws iam get-account-summary --output json`
   **Purpose:** Get account-wide IAM usage patterns for authorization model assessment

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws sso-admin list-instances --output json`
  - **Purpose:** Check for AWS IAM Identity Center (modern permission set approach)
- **Command:** `aws sso-admin list-permission-sets --instance-arn $(aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text) --output json 2>/dev/null || echo '{"PermissionSets":[]}'`
  - **Purpose:** List permission sets for role-based and attribute-based access validation
- **Command:** `aws iam list-roles --output json`
  - **Purpose:** Analyze traditional IAM roles for service accounts and legacy access patterns
- **Command:** `aws iam list-users --output json`
  - **Purpose:** Check if users have direct policy attachments (anti-pattern for least privilege)
- **Command:** `aws sts get-caller-identity --output json`
  - **Purpose:** Validate current session type (permission set session vs traditional credentials)
- **Command:** `aws iam get-account-summary --output json`
  - **Purpose:** Get account-wide IAM usage patterns for authorization model assessment

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_04`

**Documentation:** Complete KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time 
security authorization model for all user and non-user accounts and services

Validates both modern (IAM Identity Center Permission Sets) and traditional (IAM) approaches:
- Least privilege: Minimal permissions through permission sets and policies
- Role-based: Users access via permission sets/roles, not direct attachments
- Attribute-based: Conditional access through permission set conditions
- Just-in-time: Temporary credentials via permission sets or assumed roles

### Rule Implementation
```python
def evaluate_KSI_IAM_04(cli_output):
    """
    Complete KSI-IAM-04: Use a least-privileged, role and attribute-based, and just-in-time 
    security authorization model for all user and non-user accounts and services
    
    Validates both modern (IAM Identity Center Permission Sets) and traditional (IAM) approaches:
    - Least privilege: Minimal permissions through permission sets and policies
    - Role-based: Users access via permission sets/roles, not direct attachments
    - Attribute-based: Conditional access through permission set conditions
    - Just-in-time: Temporary credentials via permission sets or assumed roles
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    sso_instances = None
    permission_sets = None
    roles = None
    users = None
    caller_identity = None
    account_summary = None
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services

**Implementation Justification:** Validates comprehensive authorization through IAM Identity Center permission sets (modern approach) and traditional IAM patterns for complete coverage of least privilege, role-based, attribute-based, and just-in-time access

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 6 commands failed execution | ⚠️ No usable output

**Commands Executed:** 6
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*