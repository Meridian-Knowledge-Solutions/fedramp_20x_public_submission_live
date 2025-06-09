# KSI-CNA-05: Have denial of service protection

*Generated on 2025-06-09 09:58:08 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-05`
**Description:** Have denial of service protection
**Justification:** Validates basic DDoS protection is enabled
**Last Validation:** ❌ 2025-06-09T09:58:08.568496
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

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*