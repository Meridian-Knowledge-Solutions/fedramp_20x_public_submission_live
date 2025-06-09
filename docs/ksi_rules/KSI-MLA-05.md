# KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing

*Generated on 2025-06-09 03:59:46 UTC*

## 📖 Overview

**KSI ID:** `KSI-MLA-05`
**Description:** Perform Infrastructure as Code and configuration evaluation and testing
**Justification:** Validates IaC security evaluation through Config rules, CloudFormation, and configuration testing
**Last Validation:** ✅ 2025-06-09T03:59:46.483335
**Result:** ⚠️ Basic IaC evaluation (needs enhancement): ❌ No Config service for infrastructure evaluation; ✅ Infrastructure as Code: 2/2 successful CloudFormation stacks

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

**Documentation:** Fixed rule for KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing
Expected: Config Rules + CloudFormation Stacks

### Rule Implementation
```python
def evaluate_KSI_MLA_05(cli_output):
    """
    Fixed rule for KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing
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
        if not isinstance(raw_output, dict):
            continue
        if "describe-config-rules" in cli_command:
            if isinstance(raw_output, str):
                if "ConfigurationRecorderNotAvailable" in raw_output:
                    config_rules = []  # No Config service
                else:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Perform Infrastructure as Code and configuration evaluation and testing

**Implementation Justification:** Validates IaC security evaluation through Config rules, CloudFormation, and configuration testing

**FedRAMP 20x Category:** Monitoring, Logging, and Auditing

## 📊 Recent Validation Results

**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 🏗️ 2 CloudFormation stacks

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*