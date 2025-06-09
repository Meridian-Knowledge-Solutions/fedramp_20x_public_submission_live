# KSI-PIY-01: Have an up-to-date information resource inventory or code defining all deployed assets, software, and services

*Generated on 2025-06-09 09:58:08 UTC*

## 📖 Overview

**KSI ID:** `KSI-PIY-01`
**Description:** Have an up-to-date information resource inventory or code defining all deployed assets, software, and services
**Justification:** Validates asset inventory through AWS resource discovery and documented inventory records
**Last Validation:** ✅ 2025-06-09T09:58:08.572801
**Result:** ⚠️ Partial inventory coverage (expand documentation): ✅ AWS resource inventory: 11 tagged resources discovered; ❌ No manual asset inventory documentation found

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws resourcegroupstaggingapi get-resources --output json`
   **Purpose:** Get comprehensive resource inventory across all AWS services

2. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-PIY-01/ for asset_inventory.xlsx and software_inventory.pdf

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws resourcegroupstaggingapi get-resources --output json`
  - **Purpose:** Get comprehensive resource inventory across all AWS services

### 📄 Manual Evidence
- Check evidence_v2/KSI-PIY-01/ for asset_inventory.xlsx and software_inventory.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_PIY_01`

**Documentation:** KSI-PIY-01: Have an up-to-date information resource inventory or code defining 
all deployed assets, software, and services

Expected: AWS Resource Inventory + Manual Asset Documentation

### Rule Implementation
```python
def evaluate_KSI_PIY_01(cli_output):
    """
    KSI-PIY-01: Have an up-to-date information resource inventory or code defining 
    all deployed assets, software, and services
    
    Expected: AWS Resource Inventory + Manual Asset Documentation
    """
    evidence_dir = Path("evidence_v2/KSI-PIY-01")
    aws_resources = None
    if "commands" in cli_output:
        for cmd in cli_output["commands"]:
            cli_command = cmd.get("cli_command", "")
            raw_output = cmd.get("raw_output", {})
            if "get-resources" in cli_command:
                aws_resources = raw_output.get("ResourceTagMappingList", [])
    manual_evidence = []
    if evidence_dir.exists():
        inventory_files = [
            "asset_inventory.xlsx",
            "software_inventory.pdf", 
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Have an up-to-date information resource inventory or code defining all deployed assets, software, and services

**Implementation Justification:** Validates asset inventory through AWS resource discovery and documented inventory records

**FedRAMP 20x Category:** Policy and Inventory

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*