# KSI-IAM-02: Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA

*Generated on 2025-06-18 04:28:40 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-02`
**Description:** Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA
**Justification:** Validates passwordless authentication (SSO/SAML/temporary credentials) where feasible, otherwise strong password policy with mandatory MFA enforcement
**Last Validation:** ✅ 2025-06-18T04:28:40.195904
**Result:** ✅ Excellent authentication security (passwordless methods): ✅ 1 SAML providers configured (passwordless authentication); ❌ No MFA devices configured; ❌ Weak password policy: 0 chars, 0/5 requirements

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-saml-providers --output json`
   **Purpose:** Check for federated authentication (passwordless method)

2. **Command:** `aws iam list-virtual-mfa-devices --output json`
   **Purpose:** Validate MFA device configuration and enforcement

3. **Command:** `aws iam get-account-password-policy --output json`
   **Purpose:** Check strong password policy enforcement when passwords are used

4. **Command:** `aws iam list-users --output json`
   **Purpose:** Analyze user authentication patterns and requirements

5. **Command:** `aws sts get-caller-identity --output json`
   **Purpose:** Validate current authentication method (temporary vs permanent credentials)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-saml-providers --output json`
  - **Purpose:** Check for federated authentication (passwordless method)
- **Command:** `aws iam list-virtual-mfa-devices --output json`
  - **Purpose:** Validate MFA device configuration and enforcement
- **Command:** `aws iam get-account-password-policy --output json`
  - **Purpose:** Check strong password policy enforcement when passwords are used
- **Command:** `aws iam list-users --output json`
  - **Purpose:** Analyze user authentication patterns and requirements
- **Command:** `aws sts get-caller-identity --output json`
  - **Purpose:** Validate current authentication method (temporary vs permanent credentials)

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_02`

**Documentation:** Enhanced KSI-IAM-02: Use secure passwordless methods for user authentication and authorization 
when feasible, otherwise enforce strong passwords with MFA

Validates:
- True passwordless methods (SSO/SAML, temporary credentials)
- MFA enforcement when passwords are used
- Strong password policies when passwords are used
- Overall authentication security posture

### Rule Implementation
```python
def evaluate_KSI_IAM_02(cli_output):
    """
    Enhanced KSI-IAM-02: Use secure passwordless methods for user authentication and authorization 
    when feasible, otherwise enforce strong passwords with MFA
    
    Validates:
    - True passwordless methods (SSO/SAML, temporary credentials)
    - MFA enforcement when passwords are used
    - Strong password policies when passwords are used
    - Overall authentication security posture
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    saml_providers = None
    mfa_devices = None
    password_policy = None
    users = None
    caller_identity = None
    for cmd in commands:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA

**Implementation Justification:** Validates passwordless authentication (SSO/SAML/temporary credentials) where feasible, otherwise strong password policy with mandatory MFA enforcement

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 5 commands failed execution | ⚠️ No usable output

**Commands Executed:** 5
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*