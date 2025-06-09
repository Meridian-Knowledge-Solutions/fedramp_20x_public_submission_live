# KSI-IAM-06: Automatically disable accounts with privileged access on suspicious activity

*Generated on 2025-06-09 20:05:24 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-06`
**Description:** Automatically disable accounts with privileged access on suspicious activity
**Justification:** Validates automated response capabilities for privileged account security incidents
**Last Validation:** ✅ 2025-06-09T20:05:24.228083
**Result:** ⚠️ Basic automated response (expand capabilities): ❌ No CloudWatch alarms found for automated monitoring; ⚠️ 1 Lambda functions found but none explicitly security-focused; ✅ Automated notification capability: 2 SNS topics configured; ⚠️ No SNS subscriptions found

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudwatch describe-alarms --output json`
   **Purpose:** Check for automated alarms on suspicious privileged activities

2. **Command:** `aws lambda list-functions --output json`
   **Purpose:** Check for automated response functions for account security

3. **Command:** `aws sns list-topics --output json`
   **Purpose:** Check SNS topics for security alert notifications

4. **Command:** `aws sns list-subscriptions --output json`
   **Purpose:** Verify active subscriptions for security notifications

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudwatch describe-alarms --output json`
  - **Purpose:** Check for automated alarms on suspicious privileged activities
- **Command:** `aws lambda list-functions --output json`
  - **Purpose:** Check for automated response functions for account security
- **Command:** `aws sns list-topics --output json`
  - **Purpose:** Check SNS topics for security alert notifications
- **Command:** `aws sns list-subscriptions --output json`
  - **Purpose:** Verify active subscriptions for security notifications

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_06`

**Documentation:** UPDATED: KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access 
in response to suspicious activity

ENHANCEMENT: Now recognizes SNS topics and subscriptions as automated response mechanisms

### Rule Implementation
```python
def evaluate_KSI_IAM_06(cli_output):
    """
    UPDATED: KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access 
    in response to suspicious activity
    
    ENHANCEMENT: Now recognizes SNS topics and subscriptions as automated response mechanisms
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    alarms = None
    lambda_functions = None
    sns_topics = None
    sns_subscriptions = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "describe-alarms" in cli_command:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Automatically disable accounts with privileged access on suspicious activity

**Implementation Justification:** Validates automated response capabilities for privileged account security incidents

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 4 commands failed execution | ⚠️ No usable output

**Commands Executed:** 4
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*