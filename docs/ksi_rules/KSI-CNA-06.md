# KSI-CNA-06: Design for high availability and recovery

*Generated on 2025-06-06 05:52:21 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-06`
**Description:** Design for high availability and recovery
**Justification:** Validates multi-AZ design and backup capabilities
**Last Validation:** ❌ 2025-06-06T05:52:21.554447
**Result:** ❌ Rule execution error: 'list' object has no attribute 'get'

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-subnets --query 'Subnets[*].{SubnetId:SubnetId,AvailabilityZone:AvailabilityZone}' --output json`
   **Purpose:** Check multi-AZ subnet distribution

2. **Command:** `aws backup list-backup-plans --output json`
   **Purpose:** Validate backup plans exist

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-subnets --query 'Subnets[*].{SubnetId:SubnetId,AvailabilityZone:AvailabilityZone}' --output json`
  - **Purpose:** Check multi-AZ subnet distribution
- **Command:** `aws backup list-backup-plans --output json`
  - **Purpose:** Validate backup plans exist

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_06`

**Documentation:** Simple rule for KSI-CNA-06: Basic HA design
Expected: Multi-AZ subnets + Backup plans

### Rule Implementation
```python
def evaluate_KSI_CNA_06(cli_output):
    """
    Simple rule for KSI-CNA-06: Basic HA design
    Expected: Multi-AZ subnets + Backup plans
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    subnets = None
    backup_plans = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-subnets" in cli_command:
            subnets = raw_output.get("Subnets", [])
        elif "list-backup-plans" in cli_command:
            backup_plans = raw_output.get("BackupPlansList", [])
    if not subnets:
        return False, "❌ No subnets found for HA analysis"
    availability_zones = set(subnet.get("AvailabilityZone") for subnet in subnets)
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Design for high availability and recovery

**Implementation Justification:** Validates multi-AZ design and backup capabilities

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 📋 6 items retrieved | 💾 2 backup plans configured

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*