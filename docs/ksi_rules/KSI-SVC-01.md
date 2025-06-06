# KSI-SVC-01: Harden and review network and system configurations

*Generated on 2025-06-06 10:05:53 UTC*

## 📖 Overview

**KSI ID:** `KSI-SVC-01`
**Description:** Harden and review network and system configurations
**Justification:** Validates system hardening through security groups, NACLs, and instance configurations
**Last Validation:** ✅ 2025-06-06T10:05:53.256473
**Result:** ✅ System hardening: 1 hardened security groups, 0 instances configured

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-security-groups --output json`
   **Purpose:** Check security group configurations for hardening

2. **Command:** `aws ec2 describe-instances --output json`
   **Purpose:** Review instance configurations and security settings

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-security-groups --output json`
  - **Purpose:** Check security group configurations for hardening
- **Command:** `aws ec2 describe-instances --output json`
  - **Purpose:** Review instance configurations and security settings

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_01`

**Documentation:** Simple rule for KSI-SVC-01: Network and system configuration hardening
Expected: Security Groups + EC2 Instances

### Rule Implementation
```python
def evaluate_KSI_SVC_01(cli_output):
    """
    Simple rule for KSI-SVC-01: Network and system configuration hardening
    Expected: Security Groups + EC2 Instances
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    security_groups = None
    instances = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-security-groups" in cli_command:
            security_groups = raw_output.get("SecurityGroups", [])
        elif "describe-instances" in cli_command:
            instances = raw_output.get("Reservations", [])
    if not security_groups:
        return False, "❌ No security groups found"
    hardened_sgs = 0
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Harden and review network and system configurations

**Implementation Justification:** Validates system hardening through security groups, NACLs, and instance configurations

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 🛡️ 1 security groups analyzed | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*