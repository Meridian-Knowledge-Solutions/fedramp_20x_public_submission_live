# KSI-SVC-04: Manage configuration centrally

*Generated on 2025-06-06 07:53:43 UTC*

## 📖 Overview

**KSI ID:** `KSI-SVC-04`
**Description:** Manage configuration centrally
**Justification:** Validates centralized configuration management through Systems Manager and Config
**Last Validation:** ❌ 2025-06-06T07:53:43.080325
**Result:** ❌ Rule execution error: 'str' object has no attribute 'get'

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ssm describe-parameters --output json`
   **Purpose:** Check Systems Manager Parameter Store for centralized config

2. **Command:** `aws config describe-configuration-recorders --output json`
   **Purpose:** Validate AWS Config for configuration management

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ssm describe-parameters --output json`
  - **Purpose:** Check Systems Manager Parameter Store for centralized config
- **Command:** `aws config describe-configuration-recorders --output json`
  - **Purpose:** Validate AWS Config for configuration management

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_04`

**Documentation:** Simple rule for KSI-SVC-04: Centralized configuration management
Expected: SSM Parameters + Config Service

### Rule Implementation
```python
def evaluate_KSI_SVC_04(cli_output):
    """
    Simple rule for KSI-SVC-04: Centralized configuration management
    Expected: SSM Parameters + Config Service
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    ssm_parameters = None
    config_recorders = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-parameters" in cli_command:
            ssm_parameters = raw_output.get("Parameters", [])
        elif "describe-configuration-recorders" in cli_command:
            config_recorders = raw_output.get("ConfigurationRecorders", [])
    findings = []
    config_mechanisms = 0
    if ssm_parameters is not None:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Manage configuration centrally

**Implementation Justification:** Validates centralized configuration management through Systems Manager and Config

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ✅ Command output received | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*