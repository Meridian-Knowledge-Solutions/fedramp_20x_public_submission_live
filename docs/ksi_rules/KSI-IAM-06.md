# KSI-IAM-06: Automatically disable accounts with privileged access on suspicious activity

*Generated on 2025-06-06 05:34:53 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-06`
**Description:** Automatically disable accounts with privileged access on suspicious activity
**Justification:** Validates automated response capabilities for privileged account security incidents
**Last Validation:** ❌ 2025-06-06T05:34:53.038079
**Result:** ❌ No automated response to suspicious activity: ❌ No CloudWatch alarms found for automated monitoring; ❌ No Lambda functions found for automated response

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-users --query 'Users[?contains(UserName, `admin`) || contains(UserName, `root`)]' --output json`
   **Purpose:** Identify privileged user accounts

2. **Command:** `aws logs describe-log-groups --log-group-name-prefix '/aws/lambda' --output json`
   **Purpose:** Check for automated response Lambda functions

3. **Command:** `aws events list-rules --output json`
   **Purpose:** Verify EventBridge rules for automated responses

4. **Command:** `aws cloudwatch describe-alarms --alarm-names 'HighPrivilegedActivity' --output json`
   **Purpose:** Check for CloudWatch alarms on privileged activities

5. **Command:** `aws iam generate-credential-report --output json && aws iam get-credential-report --output text`
   **Purpose:** Get credential report to check for disabled/inactive accounts

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-users --query 'Users[?contains(UserName, `admin`) || contains(UserName, `root`)]' --output json`
  - **Purpose:** Identify privileged user accounts
- **Command:** `aws logs describe-log-groups --log-group-name-prefix '/aws/lambda' --output json`
  - **Purpose:** Check for automated response Lambda functions
- **Command:** `aws events list-rules --output json`
  - **Purpose:** Verify EventBridge rules for automated responses
- **Command:** `aws cloudwatch describe-alarms --alarm-names 'HighPrivilegedActivity' --output json`
  - **Purpose:** Check for CloudWatch alarms on privileged activities
- **Command:** `aws iam generate-credential-report --output json && aws iam get-credential-report --output text`
  - **Purpose:** Get credential report to check for disabled/inactive accounts

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_06`

**Documentation:** KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access 
in response to suspicious activity

Expected: CloudWatch Alarms + Lambda Functions

### Rule Implementation
```python
def evaluate_KSI_IAM_06(cli_output):
    """
    KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access 
    in response to suspicious activity
    
    Expected: CloudWatch Alarms + Lambda Functions
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    alarms = None
    lambda_functions = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-alarms" in cli_command:
            alarms = raw_output.get("MetricAlarms", [])
        elif "list-functions" in cli_command:
            lambda_functions = raw_output.get("Functions", [])
    findings = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Automatically disable accounts with privileged access on suspicious activity

**Implementation Justification:** Validates automated response capabilities for privileged account security incidents

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 5 commands executed successfully | ⚠️ No usable output | ✅ Command output received | ✅ Command output received

**Commands Executed:** 5
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*