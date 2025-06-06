# KSI-IAM-05: Apply zero trust design principles

*Generated on 2025-06-06 08:21:01 UTC*

## 📖 Overview

**KSI ID:** `KSI-IAM-05`
**Description:** Apply zero trust design principles
**Justification:** Validates zero trust through continuous verification, conditional access, and comprehensive logging
**Last Validation:** ✅ 2025-06-06T08:21:01.669026
**Result:** ⚠️ Partial zero trust implementation: ✅ Continuous verification: 1 trails (0 active, 1 multi-region); ⚠️ No conditional access policies found

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Check continuous monitoring and verification logging

2. **Command:** `aws iam list-policies --scope Local --output json`
   **Purpose:** Check for conditional access policies implementing zero trust

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Check continuous monitoring and verification logging
- **Command:** `aws iam list-policies --scope Local --output json`
  - **Purpose:** Check for conditional access policies implementing zero trust

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_05`

**Documentation:** KSI-IAM-05: Apply zero trust design principles

Expected: CloudTrail + Conditional Access Policies

### Rule Implementation
```python
def evaluate_KSI_IAM_05(cli_output):
    """
    KSI-IAM-05: Apply zero trust design principles
    
    Expected: CloudTrail + Conditional Access Policies
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudtrail_trails = None
    local_policies = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-trails" in cli_command:
            cloudtrail_trails = raw_output.get("trailList", [])
        elif "list-policies" in cli_command and "Local" in cli_command:
            local_policies = raw_output.get("Policies", [])
    findings = []
    zero_trust_mechanisms = 0
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Apply zero trust design principles

**Implementation Justification:** Validates zero trust through continuous verification, conditional access, and comprehensive logging

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 📊 1 CloudTrail configurations | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*