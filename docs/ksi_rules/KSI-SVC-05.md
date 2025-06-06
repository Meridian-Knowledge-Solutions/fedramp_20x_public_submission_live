# KSI-SVC-05: Enforce system integrity through cryptographic means

*Generated on 2025-06-06 09:29:28 UTC*

## 📖 Overview

**KSI ID:** `KSI-SVC-05`
**Description:** Enforce system integrity through cryptographic means
**Justification:** Validates integrity protection through CloudTrail log file validation and file integrity monitoring
**Last Validation:** ✅ 2025-06-06T09:29:28.446309
**Result:** ✅ Cryptographic integrity mechanisms: ✅ 1 CloudTrail trails (1 with log file validation)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Check CloudTrail log file validation for integrity

2. **Command:** `aws kms list-keys --output json`
   **Purpose:** Validate KMS keys available for cryptographic integrity

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Check CloudTrail log file validation for integrity
- **Command:** `aws kms list-keys --output json`
  - **Purpose:** Validate KMS keys available for cryptographic integrity

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_05`

**Documentation:** Simple rule for KSI-SVC-05: System integrity through cryptographic means
Expected: CloudTrail + KMS Keys

### Rule Implementation
```python
def evaluate_KSI_SVC_05(cli_output):
    """
    Simple rule for KSI-SVC-05: System integrity through cryptographic means
    Expected: CloudTrail + KMS Keys
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudtrail_trails = None
    kms_keys = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-trails" in cli_command:
            cloudtrail_trails = raw_output.get("trailList", [])
        elif "list-keys" in cli_command:
            kms_keys = raw_output.get("Keys", [])
    findings = []
    integrity_mechanisms = 0
    if cloudtrail_trails is not None:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Enforce system integrity through cryptographic means

**Implementation Justification:** Validates integrity protection through CloudTrail log file validation and file integrity monitoring

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 📊 1 CloudTrail configurations | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*