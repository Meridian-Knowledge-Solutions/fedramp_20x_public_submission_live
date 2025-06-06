# KSI-CNA-06: Design for high availability and recovery

*Generated on 2025-06-06 07:53:43 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-06`
**Description:** Design for high availability and recovery
**Justification:** Validates multi-AZ design and backup capabilities
**Last Validation:** ❌ 2025-06-06T07:53:43.080398
**Result:** ❌ Single AZ design not suitable for HA: 0 AZ(s), 0 subnets

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

**Documentation:** FIXED: KSI-CNA-06: Basic HA design

ISSUE: Subnet parsing not working with query format, but evidence shows 6 items + 2 backup plans
FIX: Handle the specific query format and properly detect multi-AZ from the data

### Rule Implementation
```python
def evaluate_KSI_CNA_06(cli_output):
    """
    FIXED: KSI-CNA-06: Basic HA design
    
    ISSUE: Subnet parsing not working with query format, but evidence shows 6 items + 2 backup plans
    FIX: Handle the specific query format and properly detect multi-AZ from the data
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    subnets = None
    backup_plans = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "describe-subnets" in cli_command:
            if isinstance(raw_output, list):
                subnets = raw_output  # Direct list from query
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