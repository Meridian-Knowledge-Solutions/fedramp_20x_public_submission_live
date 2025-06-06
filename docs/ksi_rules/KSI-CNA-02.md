# KSI-CNA-02: Design systems to minimize attack surface

*Generated on 2025-06-06 05:52:21 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-02`
**Description:** Design systems to minimize attack surface
**Justification:** Validates network segmentation and isolation
**Last Validation:** ❌ 2025-06-06T05:52:21.549714
**Result:** ❌ Rule execution error: 'list' object has no attribute 'get'

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-subnets --output json`
   **Purpose:** Check subnet segmentation

2. **Command:** `aws ec2 describe-security-groups --query 'SecurityGroups[?GroupName!=`default`]' --output json`
   **Purpose:** Verify custom security groups exist

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-subnets --output json`
  - **Purpose:** Check subnet segmentation
- **Command:** `aws ec2 describe-security-groups --query 'SecurityGroups[?GroupName!=`default`]' --output json`
  - **Purpose:** Verify custom security groups exist

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_02`

**Documentation:** Simple rule for KSI-CNA-02: Network segmentation exists
Expected: Subnets + Custom Security Groups

### Rule Implementation
```python
def evaluate_KSI_CNA_02(cli_output):
    """
    Simple rule for KSI-CNA-02: Network segmentation exists
    Expected: Subnets + Custom Security Groups
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    subnets = None
    security_groups = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-subnets" in cli_command:
            subnets = raw_output.get("Subnets", [])
        elif "describe-security-groups" in cli_command:
            security_groups = raw_output.get("SecurityGroups", [])
    if not subnets:
        return False, "❌ No subnets found"
    availability_zones = set(subnet.get("AvailabilityZone") for subnet in subnets)
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Design systems to minimize attack surface

**Implementation Justification:** Validates network segmentation and isolation

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*