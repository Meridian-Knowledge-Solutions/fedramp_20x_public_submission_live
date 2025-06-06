# KSI-MLA-01: Operate a SIEM or similar system for centralized, tamper-resistant logging

*Generated on 2025-06-06 11:23:25 UTC*

## 📖 Overview

**KSI ID:** `KSI-MLA-01`
**Description:** Operate a SIEM or similar system for centralized, tamper-resistant logging
**Justification:** Validates centralized logging with tamper resistance through CloudTrail, CloudWatch, and log integrity
**Last Validation:** ✅ 2025-06-06T11:23:25.289002
**Result:** ✅ SIEM/centralized tamper-resistant logging: ✅ CloudTrail: 1 trails (0 active, 1 tamper-resistant); ✅ Centralized logging: 3 log groups (1 AWS services, 2 applications)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Check CloudTrail for centralized, tamper-resistant logging

2. **Command:** `aws logs describe-log-groups --output json`
   **Purpose:** Validate centralized log collection in CloudWatch

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Check CloudTrail for centralized, tamper-resistant logging
- **Command:** `aws logs describe-log-groups --output json`
  - **Purpose:** Validate centralized log collection in CloudWatch

## 🧠 Validation Logic

**Function:** `evaluate_KSI_MLA_01`

**Documentation:** KSI-MLA-01: Operate a Security Information and Event Management (SIEM) or similar 
system(s) for centralized, tamper-resistant logging of events, activities, and changes

Expected: CloudTrail + CloudWatch Log Groups

### Rule Implementation
```python
def evaluate_KSI_MLA_01(cli_output):
    """
    KSI-MLA-01: Operate a Security Information and Event Management (SIEM) or similar 
    system(s) for centralized, tamper-resistant logging of events, activities, and changes
    
    Expected: CloudTrail + CloudWatch Log Groups
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudtrail_trails = None
    log_groups = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-trails" in cli_command:
            cloudtrail_trails = raw_output.get("trailList", [])
        elif "describe-log-groups" in cli_command:
            log_groups = raw_output.get("logGroups", [])
    findings = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Operate a SIEM or similar system for centralized, tamper-resistant logging

**Implementation Justification:** Validates centralized logging with tamper resistance through CloudTrail, CloudWatch, and log integrity

**FedRAMP 20x Category:** Monitoring, Logging, and Auditing

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 📊 1 CloudTrail configurations | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*