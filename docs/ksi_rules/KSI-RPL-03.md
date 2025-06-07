# KSI-RPL-03: Perform system backups aligned with recovery objectives

*Generated on 2025-06-07 06:46:54 UTC*

## 📖 Overview

**KSI ID:** `KSI-RPL-03`
**Description:** Perform system backups aligned with recovery objectives
**Justification:** Validates backup implementation through AWS Backup, EBS snapshots, and RDS backups aligned with documented objectives INCLUDING retention policies
**Last Validation:** ✅ 2025-06-07T06:46:54.376534
**Result:** ✅ System backups with compliant retention aligned with recovery objectives: ✅ Backup infrastructure: 2 AWS Backup plans (Dailybackup, Monthly); ✅ Adequate retention: 35 days meets FedRAMP minimum (rule: DailyBackups); ✅ Full retention compliance: 1/1 rules meet requirements; ℹ️ No EBS snapshots (acceptable if using AWS Backup exclusively)

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

**Documentation:** FRESH BUILD: KSI-RPL-03: Perform system backups aligned with recovery objectives

Built from scratch based on actual data structure analysis

### Rule Implementation
```python
def evaluate_KSI_RPL_03(cli_output):
    """
    FRESH BUILD: KSI-RPL-03: Perform system backups aligned with recovery objectives
    
    Built from scratch based on actual data structure analysis
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    backup_plans_found = []
    backup_plan_details = None
    snapshots_count = 0
    for cmd in commands:
        if cmd.get("status") != "success":
            continue
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if cli_command.startswith("aws backup get-backup-plan"):
            backup_plan = raw_output.get("BackupPlan", {})
            if backup_plan:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Perform system backups aligned with recovery objectives

**Implementation Justification:** Validates backup implementation through AWS Backup, EBS snapshots, and RDS backups aligned with documented objectives INCLUDING retention policies

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 3 commands executed successfully | 💾 2 backup plans configured | ✅ Command output received | ✅ Command output received

**Commands Executed:** 3
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*