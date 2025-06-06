# KSI-RPL-03: Perform system backups aligned with recovery objectives

*Generated on 2025-06-06 07:53:43 UTC*

## 📖 Overview

**KSI ID:** `KSI-RPL-03`
**Description:** Perform system backups aligned with recovery objectives
**Justification:** Validates backup implementation through AWS Backup, EBS snapshots, and RDS backups aligned with documented objectives
**Last Validation:** ✅ 2025-06-06T07:53:43.083928
**Result:** ⚠️ Basic backup implementation (expand systematic coverage): ✅ Systematic backups: 2 AWS Backup plans configured; ℹ️ No EBS snapshots found (acceptable for low-impact if no EBS volumes)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws backup list-backup-plans --output json`
   **Purpose:** Check AWS Backup plans for systematic backup implementation

2. **Command:** `aws ec2 describe-snapshots --owner-ids self --output json`
   **Purpose:** Validate EBS snapshots for system backup coverage

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws backup list-backup-plans --output json`
  - **Purpose:** Check AWS Backup plans for systematic backup implementation
- **Command:** `aws ec2 describe-snapshots --owner-ids self --output json`
  - **Purpose:** Validate EBS snapshots for system backup coverage

## 🧠 Validation Logic

**Function:** `evaluate_KSI_RPL_03`

**Documentation:** KSI-RPL-03: Perform system backups aligned with recovery objectives

Expected: AWS Backup Plans + EBS Snapshots

### Rule Implementation
```python
def evaluate_KSI_RPL_03(cli_output):
    """
    KSI-RPL-03: Perform system backups aligned with recovery objectives
    
    Expected: AWS Backup Plans + EBS Snapshots
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    backup_plans = None
    ebs_snapshots = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-backup-plans" in cli_command:
            backup_plans = raw_output.get("BackupPlansList", [])
        elif "describe-snapshots" in cli_command:
            ebs_snapshots = raw_output.get("Snapshots", [])
    findings = []
    backup_mechanisms = 0
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Perform system backups aligned with recovery objectives

**Implementation Justification:** Validates backup implementation through AWS Backup, EBS snapshots, and RDS backups aligned with documented objectives

**FedRAMP 20x Category:** Recovery Planning

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 💾 2 backup plans configured | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*