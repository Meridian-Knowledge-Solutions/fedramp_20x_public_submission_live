# KSI-CMT-01: Log and monitor system modifications

*Generated on 2025-06-06 06:36:35 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-01`
**Description:** Log and monitor system modifications
**Justification:** Validates system modification logging through CloudTrail and Config change tracking
**Last Validation:** ❌ 2025-06-06T06:36:35.347817
**Result:** ❌ No system modification tracking: ✅ System modification logging: 1 CloudTrail trails (0 active, 1 global events); ❌ No Config service for configuration change monitoring

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Check CloudTrail for system modification logging

2. **Command:** `aws config describe-configuration-recorders --output json`
   **Purpose:** Validate Config for configuration change monitoring

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Check CloudTrail for system modification logging
- **Command:** `aws config describe-configuration-recorders --output json`
  - **Purpose:** Validate Config for configuration change monitoring

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_01`

**Documentation:** Fixed rule for KSI-CMT-01: Log and monitor system modifications
Expected: CloudTrail + Config Recorders

### Rule Implementation
```python
def evaluate_KSI_CMT_01(cli_output):
    """
    Fixed rule for KSI-CMT-01: Log and monitor system modifications
    Expected: CloudTrail + Config Recorders
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudtrail_trails = None
    config_recorders = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "describe-trails" in cli_command:
            cloudtrail_trails = raw_output.get("trailList", [])
        elif "describe-configuration-recorders" in cli_command:
            if isinstance(raw_output, str):
                if "NoSuchConfigurationRecorderException" in raw_output:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Log and monitor system modifications

**Implementation Justification:** Validates system modification logging through CloudTrail and Config change tracking

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/2 commands failed execution | 📊 1 CloudTrail configurations | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*