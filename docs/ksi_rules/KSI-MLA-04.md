# KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

*Generated on 2025-06-06 08:50:09 UTC*

## 📖 Overview

**KSI ID:** `KSI-MLA-04`
**Description:** Perform authenticated vulnerability scanning on information resources
**Justification:** Validates authenticated vulnerability scanning capabilities through Inspector and Security Hub
**Last Validation:** ❌ 2025-06-06T08:50:09.214144
**Result:** ❌ No authenticated vulnerability scanning capability: ⚠️ No Inspector coverage found; ℹ️ No EC2 instances found (acceptable for low-impact if using managed services)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws inspector2 list-coverage --output json`
   **Purpose:** Check Inspector coverage for authenticated vulnerability scanning

2. **Command:** `aws ec2 describe-instances --output json`
   **Purpose:** Validate information resources available for vulnerability scanning

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws inspector2 list-coverage --output json`
  - **Purpose:** Check Inspector coverage for authenticated vulnerability scanning
- **Command:** `aws ec2 describe-instances --output json`
  - **Purpose:** Validate information resources available for vulnerability scanning

## 🧠 Validation Logic

**Function:** `evaluate_KSI_MLA_04`

**Documentation:** REALISTIC: KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

UPDATED LOGIC: Inspector capability enabled is sufficient for cost-optimized environments
where resources are spun down when not in use

### Rule Implementation
```python
def evaluate_KSI_MLA_04(cli_output):
    """
    REALISTIC: KSI-MLA-04: Perform authenticated vulnerability scanning on information resources
    
    UPDATED LOGIC: Inspector capability enabled is sufficient for cost-optimized environments
    where resources are spun down when not in use
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    inspector_coverage = None
    ec2_instances = None
    inspector_config = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "list-coverage" in cli_command:
            inspector_coverage = raw_output.get("coveredResources", [])
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Perform authenticated vulnerability scanning on information resources

**Implementation Justification:** Validates authenticated vulnerability scanning capabilities through Inspector and Security Hub

**FedRAMP 20x Category:** Monitoring, Logging, and Auditing

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*