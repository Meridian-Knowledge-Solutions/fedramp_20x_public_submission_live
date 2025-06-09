# KSI-CNA-07: Follow AWS best practices

<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-09 07:55:36 UTC*
=======
*Generated on 2025-06-09 07:55:55 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-09 07:55:59 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-CNA-07`
**Description:** Follow AWS best practices
**Justification:** Validates basic AWS configuration best practices
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-09T07:55:36.268210
=======
**Last Validation:** ✅ 2025-06-09T07:55:55.135991
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-09T07:55:59.597994
>>>>>>> Stashed changes
**Result:** ✅ AWS best practices: 394 active Config rules configured

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws configservice describe-config-rules --output json --region us-east-1`
   **Purpose:** Check if Config rules are configured

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws configservice describe-config-rules --output json --region us-east-1`
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

**Evidence Analysis:** ✅ All 1 commands executed successfully | 📋 394 Config rules active

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*