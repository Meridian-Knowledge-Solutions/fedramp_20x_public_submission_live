# KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services

*Generated on 2025-06-10 18:51:13 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-03`
**Description:** Enforce appropriately secure authentication methods for non-user accounts and services
**Justification:** Validates service accounts use appropriate authentication methods (roles, not long-term keys) and detects insecure patterns
**Last Validation:** ✅ 2025-06-10T18:51:13.256786
**Result:** ✅ Secure service authentication methods: ✅ 48 IAM roles available (24 service-oriented); ✅ 2 users found, none appear to be service accounts; ✅ 1 active access keys (reasonable for admin use); ℹ️ No EC2 instance profile information available

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-roles --output json`
   **Purpose:** Check IAM roles for service authentication (primary secure method)

2. **Command:** `aws iam list-users --output json`
   **Purpose:** Identify potential service users who should be using roles instead

3. **Command:** `aws iam list-access-keys --output json`
   **Purpose:** Detect long-term access keys that may indicate insecure service authentication

4. **Command:** `aws ec2 describe-instances --query 'Reservations[*].Instances[*].IamInstanceProfile' --output json`
   **Purpose:** Validate EC2 instances use instance profiles for secure service authentication

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-roles --output json`
  - **Purpose:** Check IAM roles for service authentication (primary secure method)
- **Command:** `aws iam list-users --output json`
  - **Purpose:** Identify potential service users who should be using roles instead
- **Command:** `aws iam list-access-keys --output json`
  - **Purpose:** Detect long-term access keys that may indicate insecure service authentication
- **Command:** `aws ec2 describe-instances --query 'Reservations[*].Instances[*].IamInstanceProfile' --output json`
  - **Purpose:** Validate EC2 instances use instance profiles for secure service authentication

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_03`

**Documentation:** Enhanced KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services

Validates:
- IAM roles for service authentication (secure)
- Absence of long-term access keys for services (insecure)
- Instance profiles for EC2 services
- Service user patterns

### Rule Implementation
```python
def evaluate_KSI_IAM_03(cli_output):
    """
    Enhanced KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services
    
    Validates:
    - IAM roles for service authentication (secure)
    - Absence of long-term access keys for services (insecure)
    - Instance profiles for EC2 services
    - Service user patterns
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    roles = None
    users = None
    access_keys = None
    instance_profiles = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce appropriately secure authentication methods for non-user accounts and services

**Implementation Justification:** Validates service accounts use appropriate authentication methods (roles, not long-term keys) and detects insecure patterns

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 4 commands failed execution | ⚠️ No usable output

**Commands Executed:** 4
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*