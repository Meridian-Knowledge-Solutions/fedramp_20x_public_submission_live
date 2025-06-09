# KSI-CMT-02: Execute changes through redeployment of version controlled immutable resources

*Generated on 2025-06-09 20:05:24 UTC*

## 📖 Overview

**KSI ID:** `KSI-CMT-02`
**Description:** Execute changes through redeployment of version controlled immutable resources
**Justification:** Validates immutable infrastructure patterns through CloudFormation and version control practices
**Last Validation:** ✅ 2025-06-09T20:05:24.224749
**Result:** ⚠️ Basic immutable deployment (expand coverage): ✅ Immutable infrastructure: 2/2 successful CloudFormation deployments; ⚠️ No launch templates for immutable instance deployment

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   **Purpose:** Check CloudFormation for immutable infrastructure deployments

2. **Command:** `aws ec2 describe-launch-templates --output json`
   **Purpose:** Validate launch templates for immutable instance deployments

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
  - **Purpose:** Check CloudFormation for immutable infrastructure deployments
- **Command:** `aws ec2 describe-launch-templates --output json`
  - **Purpose:** Validate launch templates for immutable instance deployments

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CMT_02`

**Documentation:** KSI-CMT-02: Execute changes through redeployment of version controlled immutable resources 
rather than direct modification wherever possible

Expected: CloudFormation Stacks + Launch Templates

### Rule Implementation
```python
def evaluate_KSI_CMT_02(cli_output):
    """
    KSI-CMT-02: Execute changes through redeployment of version controlled immutable resources 
    rather than direct modification wherever possible
    
    Expected: CloudFormation Stacks + Launch Templates
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
    findings = []
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Execute changes through redeployment of version controlled immutable resources

**Implementation Justification:** Validates immutable infrastructure patterns through CloudFormation and version control practices

**FedRAMP 20x Category:** Change Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*