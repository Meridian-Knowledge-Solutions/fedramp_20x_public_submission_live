# KSI-SVC-07: Use consistent, risk-informed security patching

*Generated on 2025-06-06 10:12:33 UTC*

## 📖 Overview

**KSI ID:** `KSI-SVC-07`
**Description:** Use consistent, risk-informed security patching
**Justification:** Validates patch management through Systems Manager and automated patching
**Last Validation:** ✅ 2025-06-06T10:12:33.750912
**Result:** ✅ Consistent patch management: ✅ 17 patch baselines configured for consistent patching; ℹ️ No SSM-managed instances found (acceptable if no EC2 instances)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ssm describe-patch-baselines --output json`
   **Purpose:** Check patch baselines for consistent patching approach

2. **Command:** `aws ssm describe-instance-information --output json`
   **Purpose:** Validate SSM agent coverage for automated patching

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ssm describe-patch-baselines --output json`
  - **Purpose:** Check patch baselines for consistent patching approach
- **Command:** `aws ssm describe-instance-information --output json`
  - **Purpose:** Validate SSM agent coverage for automated patching

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_07`

**Documentation:** Simple rule for KSI-SVC-07: Consistent, risk-informed security patching
Expected: SSM Patch Baselines + SSM Agent Coverage

### Rule Implementation
```python
def evaluate_KSI_SVC_07(cli_output):
    """
    Simple rule for KSI-SVC-07: Consistent, risk-informed security patching
    Expected: SSM Patch Baselines + SSM Agent Coverage
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    patch_baselines = None
    ssm_instances = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-patch-baselines" in cli_command:
            patch_baselines = raw_output.get("BaselineIdentities", [])
        elif "describe-instance-information" in cli_command:
            ssm_instances = raw_output.get("InstanceInformationList", [])
    findings = []
    patching_mechanisms = 0
    if patch_baselines is not None:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use consistent, risk-informed security patching

**Implementation Justification:** Validates patch management through Systems Manager and automated patching

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*