# KSI-CNA-01: Configure information resources to limit traffic

<<<<<<< Updated upstream
*Generated on 2025-06-06 08:21:01 UTC*
=======
*Generated on 2025-06-06 08:22:08 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-CNA-01`
**Description:** Configure information resources to limit traffic
**Justification:** Validates basic network access controls are configured
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-06T08:21:01.662157
=======
**Last Validation:** ✅ 2025-06-06T08:22:08.658199
>>>>>>> Stashed changes
**Result:** ✅ Traffic controls configured: 1 restrictive security groups, 1 VPCs

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-security-groups --output json`
   **Purpose:** Check security groups have restrictive rules

2. **Command:** `aws ec2 describe-vpcs --output json`
   **Purpose:** Validate VPC configuration exists

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-security-groups --output json`
  - **Purpose:** Check security groups have restrictive rules
- **Command:** `aws ec2 describe-vpcs --output json`
  - **Purpose:** Validate VPC configuration exists

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_01`

**Documentation:** Simple rule for KSI-CNA-01: Basic traffic controls configured
Expected: Security Groups + VPC

### Rule Implementation
```python
def evaluate_KSI_CNA_01(cli_output):
    """
    Simple rule for KSI-CNA-01: Basic traffic controls configured
    Expected: Security Groups + VPC
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    security_groups = None
    vpcs = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-security-groups" in cli_command:
            security_groups = raw_output.get("SecurityGroups", [])
        elif "describe-vpcs" in cli_command:
            vpcs = raw_output.get("Vpcs", [])
    if not security_groups:
        return False, "❌ No security groups found"
    if not vpcs:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Configure information resources to limit traffic

**Implementation Justification:** Validates basic network access controls are configured

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 🛡️ 1 security groups analyzed | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*