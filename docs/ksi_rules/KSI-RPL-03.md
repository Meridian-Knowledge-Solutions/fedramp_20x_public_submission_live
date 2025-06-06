# KSI-RPL-03: Perform system backups aligned with recovery objectives

*Generated on 2025-06-06 10:12:33 UTC*

## 📖 Overview

**KSI ID:** `KSI-RPL-03`
**Description:** Perform system backups aligned with recovery objectives
**Justification:** Validates backup implementation through AWS Backup, EBS snapshots, and RDS backups aligned with documented objectives INCLUDING retention policies
**Last Validation:** ❌ 2025-06-06T10:12:33.759056
**Result:** ❌ Insufficient backup implementation: ❌ No AWS Backup plans configured; ℹ️ No EBS snapshots (using AWS Backup exclusively)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws backup list-backup-plans --output json`
   **Purpose:** Check AWS Backup plans for systematic backup implementation

2. **Command:** `aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text) --output json`
   **Purpose:** Get detailed backup plan configuration including retention policies

3. **Command:** `aws ec2 describe-snapshots --owner-ids self --output json`
   **Purpose:** Validate EBS snapshots for system backup coverage

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws backup list-backup-plans --output json`
  - **Purpose:** Check AWS Backup plans for systematic backup implementation
- **Command:** `aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text) --output json`
  - **Purpose:** Get detailed backup plan configuration including retention policies
- **Command:** `aws ec2 describe-snapshots --owner-ids self --output json`
  - **Purpose:** Validate EBS snapshots for system backup coverage

## 🧠 Validation Logic

**Function:** `evaluate_KSI_RPL_03`

**Documentation:** FIXED: KSI-RPL-03: Perform system backups aligned with recovery objectives

BUG FIX: Corrected command parsing logic to distinguish between list-backup-plans and get-backup-plan

### Rule Implementation
```python
def evaluate_KSI_RPL_03(cli_output):
    """
    FIXED: KSI-RPL-03: Perform system backups aligned with recovery objectives
    
    BUG FIX: Corrected command parsing logic to distinguish between list-backup-plans and get-backup-plan
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    backup_plans = None
    backup_plan_details = None
    ebs_snapshots = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "list-backup-plans" in cli_command:
            backup_plans = raw_output.get("BackupPlansList", [])
        elif "get-backup-plan" in cli_command:  # This was being missed!
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Perform system backups aligned with recovery objectives

**Implementation Justification:** Validates backup implementation through AWS Backup, EBS snapshots, and RDS backups aligned with documented objectives INCLUDING retention policies

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 3 commands executed successfully | 💾 2 backup plans configured | ✅ Command output received | ✅ Command output received

**Commands Executed:** 3
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*