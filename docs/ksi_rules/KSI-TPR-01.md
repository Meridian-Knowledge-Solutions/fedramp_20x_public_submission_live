# KSI-TPR-01: Identify all third-party information resources

<<<<<<< Updated upstream
<<<<<<< Updated upstream
*Generated on 2025-06-10 12:33:14 UTC*
=======
*Generated on 2025-06-10 12:33:33 UTC*
>>>>>>> Stashed changes
=======
*Generated on 2025-06-10 12:33:42 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-TPR-01`
**Description:** Identify all third-party information resources
**Justification:** Validates third-party resource identification through AWS services and documented third-party inventory
<<<<<<< Updated upstream
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T12:33:14.281421
=======
**Last Validation:** ✅ 2025-06-10T12:33:32.893510
>>>>>>> Stashed changes
=======
**Last Validation:** ✅ 2025-06-10T12:33:41.782960
>>>>>>> Stashed changes
**Result:** ⚠️ Partial third-party identification (expand documentation): ❌ No cross-account role data for third-party integration analysis; ✅ Documented third-party inventory: sbom_including_elastic.json, fedramp_moderate_vendor_list.xlsx, Elasticsearch Inc._06.04.2024_Self_Attestation.pdf

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws iam list-roles --query 'Roles[?contains(AssumeRolePolicyDocument, `sts:AssumeRole`)]' --output json`
   **Purpose:** Check for cross-account roles indicating third-party integrations

2. **Command:** `evidence_check`
   **Purpose:** Check evidence_v2/KSI-TPR-01/ for third_party_inventory.xlsx, saas_services_list.pdf, and vendor_registry.pdf

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws iam list-roles --query 'Roles[?contains(AssumeRolePolicyDocument, `sts:AssumeRole`)]' --output json`
  - **Purpose:** Check for cross-account roles indicating third-party integrations

### 📄 Manual Evidence
- Check evidence_v2/KSI-TPR-01/ for third_party_inventory.xlsx, saas_services_list.pdf, and vendor_registry.pdf

## 🧠 Validation Logic

**Function:** `evaluate_KSI_TPR_01`

**Documentation:** Fixed rule for KSI-TPR-01: Identify all third-party information resources
Expected: Cross-account roles + Manual third-party inventory

### Rule Implementation
```python
def evaluate_KSI_TPR_01(cli_output):
    """
    Fixed rule for KSI-TPR-01: Identify all third-party information resources
    Expected: Cross-account roles + Manual third-party inventory
    """
    evidence_dir = Path("evidence_v2/KSI-TPR-01")
    cross_account_roles = None
    if "commands" in cli_output:
        for cmd in cli_output["commands"]:
            cli_command = cmd.get("cli_command", "")
            raw_output = cmd.get("raw_output", {})
            if not isinstance(raw_output, dict):
                continue
            if "list-roles" in cli_command:
                cross_account_roles = raw_output.get("Roles", [])
    manual_evidence = []
    if evidence_dir.exists():
        inventory_files = [
            "sbom_including_elastic.json",
            "fedramp_moderate_vendor_list.xlsx",
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Identify all third-party information resources

**Implementation Justification:** Validates third-party resource identification through AWS services and documented third-party inventory

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 2 commands failed execution | ⚠️ No usable output

**Commands Executed:** 2
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*