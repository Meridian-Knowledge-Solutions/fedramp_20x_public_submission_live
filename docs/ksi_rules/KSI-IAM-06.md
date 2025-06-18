# KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

*Generated on 2025-06-18 19:47:42 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-06`
**Description:** Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity
**Justification:** Validates end-to-end automated response workflows including threat detection, event triggers, and account security actions through modern AWS security services and Identity Center integration
**Last Validation:** ✅ 2025-06-18T19:47:42.488327
**Result:** ✅ Strong automated response capabilities (82%): ✅ Advanced threat detection: GuardDuty enabled (1 detector(s)); ✅ Centralized security management: Security Hub enabled; ✅ Automated security triggers: 1 active EventBridge rules; ✅ Modern identity automation: Identity Center configured (1 instance(s)); ✅ Built-in automated identity controls: Session management, conditional access, risk-based authentication; ⚠️ No Config rules found for automated remediation; ⚠️ 2 Lambda functions found but none explicitly security-focused; ❌ No CloudWatch alarms found for security monitoring

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws events list-rules --output json`
   **Purpose:** Check EventBridge rules for automated security response triggers (critical for automation)

2. **Command:** `aws guardduty list-detectors --output json`
   **Purpose:** Validate GuardDuty threat detection service for suspicious activity identification

3. **Command:** `aws securityhub describe-hub --output json`
   **Purpose:** Check Security Hub for centralized security findings and automated response coordination

4. **Command:** `aws sso-admin list-instances --output json`
   **Purpose:** Validate Identity Center for built-in automated session and access controls

5. **Command:** `aws config describe-config-rules --output json`
   **Purpose:** Check Config rules for automated compliance remediation and account security

6. **Command:** `aws lambda list-functions --output json`
   **Purpose:** Identify automated response functions for account disabling and security actions

7. **Command:** `aws cloudwatch describe-alarms --output json`
   **Purpose:** Check CloudWatch alarms for suspicious privileged account activity monitoring

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws events list-rules --output json`
  - **Purpose:** Check EventBridge rules for automated security response triggers (critical for automation)
- **Command:** `aws guardduty list-detectors --output json`
  - **Purpose:** Validate GuardDuty threat detection service for suspicious activity identification
- **Command:** `aws securityhub describe-hub --output json`
  - **Purpose:** Check Security Hub for centralized security findings and automated response coordination
- **Command:** `aws sso-admin list-instances --output json`
  - **Purpose:** Validate Identity Center for built-in automated session and access controls
- **Command:** `aws config describe-config-rules --output json`
  - **Purpose:** Check Config rules for automated compliance remediation and account security
- **Command:** `aws lambda list-functions --output json`
  - **Purpose:** Identify automated response functions for account disabling and security actions
- **Command:** `aws cloudwatch describe-alarms --output json`
  - **Purpose:** Check CloudWatch alarms for suspicious privileged account activity monitoring

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_06`

**Documentation:** Enhanced KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access 
in response to suspicious activity

Validates comprehensive automated response workflows:
- Threat detection (GuardDuty, Security Hub, CloudWatch)
- Event triggers (EventBridge rules for automation)
- Response actions (Lambda functions, Config remediation)
- Identity management (Identity Center automated controls)
- End-to-end workflows (not just isolated components)

### Rule Implementation
```python
def evaluate_KSI_IAM_06(cli_output):
    """
    Enhanced KSI-IAM-06: Automatically disable or otherwise secure accounts with privileged access 
    in response to suspicious activity
    
    Validates comprehensive automated response workflows:
    - Threat detection (GuardDuty, Security Hub, CloudWatch)
    - Event triggers (EventBridge rules for automation)
    - Response actions (Lambda functions, Config remediation)
    - Identity management (Identity Center automated controls)
    - End-to-end workflows (not just isolated components)
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    event_rules = None
    guardduty_detectors = None
    security_hub = None
    sso_instances = None
    config_rules = None
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

**Implementation Justification:** Validates end-to-end automated response workflows including threat detection, event triggers, and account security actions through modern AWS security services and Identity Center integration

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 7 commands failed execution | ⚠️ No usable output

**Commands Executed:** 7
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*