# KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing

*Generated on 2025-06-06 05:52:21 UTC*

## 📖 Overview

**KSI ID:** `KSI-MLA-05`
**Description:** Perform Infrastructure as Code and configuration evaluation and testing
**Justification:** Validates IaC security evaluation through Config rules, CloudFormation, and configuration testing
**Last Validation:** ❌ 2025-06-06T05:52:21.555704
**Result:** ❌ Rule execution error: 'str' object has no attribute 'get'

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws config describe-config-rules --output json`
   **Purpose:** Check Config rules for Infrastructure as Code evaluation

2. **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   **Purpose:** Validate CloudFormation stacks for IaC configuration testing

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws config describe-config-rules --output json`
  - **Purpose:** Check Config rules for Infrastructure as Code evaluation
- **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
  - **Purpose:** Validate CloudFormation stacks for IaC configuration testing

## 🧠 Validation Logic

**Function:** `evaluate_KSI_MLA_05`

**Documentation:** KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing

Expected: Config Rules + CloudFormation Stacks

### Rule Implementation
```python
def evaluate_KSI_MLA_05(cli_output):
    """
    KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing
    
    Expected: Config Rules + CloudFormation Stacks
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    config_rules = None
    cloudformation_stacks = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-config-rules" in cli_command:
            config_rules = raw_output.get("ConfigRules", [])
        elif "list-stacks" in cli_command:
            cloudformation_stacks = raw_output.get("StackSummaries", [])
    findings = []
    iac_evaluation = 0
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Perform Infrastructure as Code and configuration evaluation and testing

**Implementation Justification:** Validates IaC security evaluation through Config rules, CloudFormation, and configuration testing

**FedRAMP 20x Category:** Monitoring, Logging, and Auditing

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 🏗️ 2 CloudFormation stacks

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*