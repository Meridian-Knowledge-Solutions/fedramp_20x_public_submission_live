# KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

*Generated on 2025-06-09 09:44:44 UTC*

## 📖 Overview

**KSI ID:** `KSI-MLA-04`
**Description:** Perform authenticated vulnerability scanning on information resources
**Justification:** Validates authenticated vulnerability scanning capabilities through Inspector and Security Hub
**Last Validation:** ✅ 2025-06-09T09:44:44.697713
**Result:** ✅ Authenticated vulnerability scanning capability established: ✅ Inspector service operational (responds to coverage queries); ℹ️ No coverage needed - no EC2 instances deployed; ℹ️ Serverless/managed services architecture (no EC2 instances)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws inspector2 list-coverage --output json`
   **Purpose:** Check Inspector coverage for authenticated vulnerability scanning

2. **Command:** `aws inspector2 get-configuration --output json`

3. **Command:** `aws ec2 describe-instances --output json`
   **Purpose:** Validate information resources available for vulnerability scanning

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws inspector2 list-coverage --output json`
  - **Purpose:** Check Inspector coverage for authenticated vulnerability scanning
- **Command:** `aws inspector2 get-configuration --output json`
- **Command:** `aws ec2 describe-instances --output json`
  - **Purpose:** Validate information resources available for vulnerability scanning

## 🧠 Validation Logic

**Function:** `evaluate_KSI_MLA_04`

**Documentation:** FIXED: KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

FIX: Handle case where Inspector service is accessible but configuration check is missing

### Rule Implementation
```python
def evaluate_KSI_MLA_04(cli_output):
    """
    FIXED: KSI-MLA-04: Perform authenticated vulnerability scanning on information resources
    
    FIX: Handle case where Inspector service is accessible but configuration check is missing
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    inspector_coverage = None
    ec2_instances = None
    inspector_config = None
    inspector_service_available = False
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

**Evidence Analysis:** ❌ All 3 commands failed execution | ⚠️ No usable output

**Commands Executed:** 3
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*