# KSI-CNA-03: Use logical networking for traffic flow controls

*Generated on 2025-06-08 04:24:33 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-03`
**Description:** Use logical networking for traffic flow controls
**Justification:** Validates network routing and access controls
**Last Validation:** ✅ 2025-06-08T04:24:33.663918
**Result:** ✅ Network controls configured: 1 NACLs (0 custom), 1 route tables

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-network-acls --output json`
   **Purpose:** Check Network ACL configurations

2. **Command:** `aws ec2 describe-route-tables --output json`
   **Purpose:** Validate routing configurations

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-network-acls --output json`
  - **Purpose:** Check Network ACL configurations
- **Command:** `aws ec2 describe-route-tables --output json`
  - **Purpose:** Validate routing configurations

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_03`

**Documentation:** Simple rule for KSI-CNA-03: Basic network controls exist
Expected: Network ACLs + Route Tables

### Rule Implementation
```python
def evaluate_KSI_CNA_03(cli_output):
    """
    Simple rule for KSI-CNA-03: Basic network controls exist
    Expected: Network ACLs + Route Tables
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    network_acls = None
    route_tables = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-network-acls" in cli_command:
            network_acls = raw_output.get("NetworkAcls", [])
        elif "describe-route-tables" in cli_command:
            route_tables = raw_output.get("RouteTables", [])
    if not network_acls:
        return False, "❌ No Network ACLs found"
    if not route_tables:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use logical networking for traffic flow controls

**Implementation Justification:** Validates network routing and access controls

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*