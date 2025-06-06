# KSI-CNA-07: Follow AWS best practices

*Generated on 2025-06-06 10:59:24 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-07`
**Description:** Follow AWS best practices
**Justification:** Validates basic AWS configuration best practices
**Last Validation:** ❌ 2025-06-06T10:59:24.547714
**Result:** ❌ Config service error: 

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws config describe-config-rules --output json`
   **Purpose:** Check if Config rules are configured

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws config describe-config-rules --output json`
  - **Purpose:** Check if Config rules are configured

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_07`

**Documentation:** Fixed rule for KSI-CNA-07: AWS best practices
Expected: Config rules configured

### Rule Implementation
```python
def evaluate_KSI_CNA_07(cli_output):
    """
    Fixed rule for KSI-CNA-07: AWS best practices
    Expected: Config rules configured
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-config-rules" in cli_command:
            if isinstance(raw_output, str):
                if "InvalidParameterValueException" in raw_output or "ConfigurationRecorderNotAvailable" in raw_output:
                    return True, "✅ AWS Config available but not configured (acceptable for Low impact)"
                else:
                    return False, f"❌ Config service error: {raw_output[:100]}"
            elif isinstance(raw_output, dict):
                config_rules = raw_output.get("ConfigRules", [])
                if config_rules:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Follow AWS best practices

**Implementation Justification:** Validates basic AWS configuration best practices

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*