# KSI-IAM-05: Apply zero trust design principles

*Generated on 2025-06-06 04:21:09 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-05`
**Description:** Apply zero trust design principles
**Justification:** Validates zero trust implementation through conditional access, logging, and continuous verification
**Last Validation:** ❌ 2025-06-06T04:21:09.292288
**Result:** ❌ Zero trust principles not implemented: ❌ No CloudTrail found for continuous verification

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-policies --scope AWS --query 'Policies[?contains(PolicyName, `Condition`)]' --output json`
   **Purpose:** Find policies with conditional access controls

2. **Command:** `aws logs describe-log-groups --log-group-name-prefix '/aws/cloudtrail' --output json`
   **Purpose:** Verify CloudTrail logging for continuous monitoring

3. **Command:** `aws iam list-role-policies --role-name OrganizationAccountAccessRole --output json`
   **Purpose:** Check cross-account access controls

4. **Command:** `aws organizations list-accounts --output json`
   **Purpose:** Validate organizational boundary controls

5. **Command:** `aws iam list-policy-versions --policy-arn arn:aws:iam::aws:policy/PowerUserAccess --output json`
   **Purpose:** Check for overly broad AWS managed policies in use

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-policies --scope AWS --query 'Policies[?contains(PolicyName, `Condition`)]' --output json`
  - **Purpose:** Find policies with conditional access controls
- **Command:** `aws logs describe-log-groups --log-group-name-prefix '/aws/cloudtrail' --output json`
  - **Purpose:** Verify CloudTrail logging for continuous monitoring
- **Command:** `aws iam list-role-policies --role-name OrganizationAccountAccessRole --output json`
  - **Purpose:** Check cross-account access controls
- **Command:** `aws organizations list-accounts --output json`
  - **Purpose:** Validate organizational boundary controls
- **Command:** `aws iam list-policy-versions --policy-arn arn:aws:iam::aws:policy/PowerUserAccess --output json`
  - **Purpose:** Check for overly broad AWS managed policies in use

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_05`

**Documentation:** KSI-IAM-05: Apply zero trust design principles

Expected: CloudTrail + Conditional Access Policies

### Rule Implementation
```python
def evaluate_KSI_IAM_05(cli_output):
    """
    KSI-IAM-05: Apply zero trust design principles
    
    Expected: CloudTrail + Conditional Access Policies
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudtrail_trails = None
    local_policies = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-trails" in cli_command:
            cloudtrail_trails = raw_output.get("trailList", [])
        elif "list-policies" in cli_command and "Local" in cli_command:
            local_policies = raw_output.get("Policies", [])
    findings = []
    zero_trust_mechanisms = 0
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Apply zero trust design principles

**Implementation Justification:** Validates zero trust implementation through conditional access, logging, and continuous verification

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/5 commands failed execution | ⚠️ No usable output | ✅ Command output received | ⚠️ No usable output

**Commands Executed:** 5
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*