# KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

<<<<<<< Updated upstream
*Generated on 2025-06-06 08:21:01 UTC*
=======
*Generated on 2025-06-06 08:22:08 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-MLA-04`
**Description:** Perform authenticated vulnerability scanning on information resources
**Justification:** Validates authenticated vulnerability scanning capabilities through Inspector and Security Hub
<<<<<<< Updated upstream
**Last Validation:** ❌ 2025-06-06T08:21:01.668129
=======
**Last Validation:** ❌ 2025-06-06T08:22:08.664104
>>>>>>> Stashed changes
**Result:** ❌ No authenticated vulnerability scanning: ❌ No Inspector coverage found for authenticated scanning; ℹ️ No EC2 instances found (acceptable for low-impact if using other services)

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

**Documentation:** KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

Expected: Inspector Coverage + EC2 Instances

### Rule Implementation
```python
def evaluate_KSI_MLA_04(cli_output):
    """
    KSI-MLA-04: Perform authenticated vulnerability scanning on information resources
    
    Expected: Inspector Coverage + EC2 Instances
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    inspector_coverage = None
    ec2_instances = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-coverage" in cli_command:
            inspector_coverage = raw_output.get("coveredResources", [])
        elif "describe-instances" in cli_command:
            ec2_instances = raw_output.get("Reservations", [])
    findings = []
    scanning_capabilities = 0
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