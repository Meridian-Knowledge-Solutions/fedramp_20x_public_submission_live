# KSI-CNA-05: Have denial of service protection

*Generated on 2025-06-06 05:52:21 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-05`
**Description:** Have denial of service protection
**Justification:** Validates basic DDoS protection is enabled
**Last Validation:** ❌ 2025-06-06T05:52:21.554236
**Result:** ❌ Rule execution error: 'str' object has no attribute 'get'

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

**Documentation:** Simple rule for KSI-CNA-05: Basic DDoS protection
Expected: AWS Shield status

### Rule Implementation
```python
def evaluate_KSI_CNA_05(cli_output):
    """
    Simple rule for KSI-CNA-05: Basic DDoS protection
    Expected: AWS Shield status
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-subscription" in cli_command:
            if "SubscriptionArn" in raw_output:
                return True, "✅ AWS Shield Advanced subscription active"
            elif not raw_output.get("Error"):
                return True, "✅ AWS Shield Standard protection active (sufficient for Low impact)"
            else:
                return False, "❌ AWS Shield protection not available"
    return False, "❌ No Shield protection data found"
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