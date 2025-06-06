# KSI-CNA-05: Have denial of service protection

<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-06 08:21:01 UTC*
=======
*Generated on 2025-06-06 08:22:08 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-06 08:23:18 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-CNA-05`
**Description:** Have denial of service protection
**Justification:** Validates basic DDoS protection is enabled
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ❌ 2025-06-06T08:21:01.666192
=======
**Last Validation:** ❌ 2025-06-06T08:22:08.662171
>>>>>>> Stashed changes
=======
**Last Validation:** ❌ 2025-06-06T08:23:18.262160
>>>>>>> Stashed changes
**Result:** ❌ AWS Shield error: 

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws shield describe-subscription --output json`
   **Purpose:** Check AWS Shield protection status

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws shield describe-subscription --output json`
  - **Purpose:** Check AWS Shield protection status

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_05`

**Documentation:** Fixed rule for KSI-CNA-05: Basic DDoS protection
Expected: AWS Shield status

### Rule Implementation
```python
def evaluate_KSI_CNA_05(cli_output):
    """
    Fixed rule for KSI-CNA-05: Basic DDoS protection
    Expected: AWS Shield status
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-subscription" in cli_command:
            if isinstance(raw_output, str):
                if "InvalidParameterValueException" in raw_output or "SubscriptionNotFound" in raw_output:
                    return True, "✅ AWS Shield Standard protection active (sufficient for Low impact)"
                else:
                    return False, f"❌ AWS Shield error: {raw_output[:100]}"
            elif isinstance(raw_output, dict):
                if "SubscriptionArn" in raw_output:
                    return True, "✅ AWS Shield Advanced subscription active"
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have denial of service protection

**Implementation Justification:** Validates basic DDoS protection is enabled

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*