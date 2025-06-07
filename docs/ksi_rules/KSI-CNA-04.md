# KSI-CNA-04: Use immutable infrastructure patterns

*Generated on 2025-06-07 01:42:27 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-04`
**Description:** Use immutable infrastructure patterns
**Justification:** Validates Infrastructure as Code and standardized deployments
**Last Validation:** ✅ 2025-06-07T01:42:27.372969
**Result:** ✅ IaC patterns found: 2 CloudFormation stacks, 0 launch templates

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   **Purpose:** Check CloudFormation stacks for IaC patterns

2. **Command:** `aws ec2 describe-launch-templates --output json`
   **Purpose:** Validate standardized launch templates

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
  - **Purpose:** Check CloudFormation stacks for IaC patterns
- **Command:** `aws ec2 describe-launch-templates --output json`
  - **Purpose:** Validate standardized launch templates

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_04`

**Documentation:** Simple rule for KSI-CNA-04: Infrastructure as Code patterns
Expected: CloudFormation + Launch Templates

### Rule Implementation
```python
def evaluate_KSI_CNA_04(cli_output):
    """
    Simple rule for KSI-CNA-04: Infrastructure as Code patterns
    Expected: CloudFormation + Launch Templates
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudformation_stacks = None
    launch_templates = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-stacks" in cli_command:
            cloudformation_stacks = raw_output.get("StackSummaries", [])
        elif "describe-launch-templates" in cli_command:
            launch_templates = raw_output.get("LaunchTemplates", [])
    active_stacks = len(cloudformation_stacks) if cloudformation_stacks else 0
    templates = len(launch_templates) if launch_templates else 0
    if active_stacks > 0 or templates > 0:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use immutable infrastructure patterns

**Implementation Justification:** Validates Infrastructure as Code and standardized deployments

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | 🏗️ 2 CloudFormation stacks | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*