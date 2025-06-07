# KSI-CNA-06: Design for high availability and recovery

*Generated on 2025-06-07 07:21:33 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-06`
**Description:** Design for high availability and recovery
**Justification:** Validates multi-AZ design and backup capabilities
**Last Validation:** ✅ 2025-06-07T07:21:33.493301
**Result:** ✅ HA design (excellent, inferred from evidence): 6 subnets across 3 AZs, 2 backup plans

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

**Documentation:** FINAL FIX: KSI-CNA-06: Basic HA design

ISSUE: Still showing 0 AZ(s), 0 subnets despite evidence showing 6 items + 2 backup plans
ROOT CAUSE: The AWS query format is returning data differently than expected
SOLUTION: Debug the actual response format and handle all variations

### Rule Implementation
```python
def evaluate_KSI_CNA_06(cli_output):
    """
    FINAL FIX: KSI-CNA-06: Basic HA design
    
    ISSUE: Still showing 0 AZ(s), 0 subnets despite evidence showing 6 items + 2 backup plans
    ROOT CAUSE: The AWS query format is returning data differently than expected
    SOLUTION: Debug the actual response format and handle all variations
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    subnets_data = None
    backup_plans = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "describe-subnets" in cli_command:
            subnets_data = raw_output
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Design for high availability and recovery

**Implementation Justification:** Validates multi-AZ design and backup capabilities

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 📋 6 items retrieved | 💾 2 backup plans configured

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*