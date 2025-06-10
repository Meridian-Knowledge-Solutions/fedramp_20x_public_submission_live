# KSI-TPR-02: Regularly confirm services handling federal information are FedRAMP authorized and securely configured

*Generated on 2025-06-10 21:56:42 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-02`
**Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured
**Justification:** Validates service inventory, FedRAMP authorization verification, and secure configuration compliance for services handling federal data
**Last Validation:** ❌ 2025-06-10T21:56:41.716707
**Result:** ❌ Insufficient FedRAMP service verification (20%): ✅ Federal information service inventory: Federal Information Mapping - Meridian LMS.pdf; ❌ No FedRAMP authorization verification documentation; ❌ No verification that services are configured per FedRAMP requirements; ⚠️ No documented process for regular FedRAMP verification

## 🛠️ Implementation

### Commands Executed
1. **Command:** `evidence_check`
   **Purpose:** Primary validation through documentation: federal_data_service_inventory.xlsx, fedramp_authorization_verification.xlsx, service_security_configurations.pdf, regular_verification_process.pdf

## 📋 Evidence Requirements

### 📄 Manual Evidence
- Manual documentation required

## 🧠 Validation Logic

**Function:** `evaluate_KSI_TPR_02`

**Documentation:** KSI-TPR-02: Regularly confirm that services handling federal information are 
FedRAMP authorized and securely configured

Focus: Service inventory → Authorization verification → Configuration compliance

### Rule Implementation
```python
def evaluate_KSI_TPR_02(cli_output):
    """
    KSI-TPR-02: Regularly confirm that services handling federal information are 
    FedRAMP authorized and securely configured
    
    Focus: Service inventory → Authorization verification → Configuration compliance
    """
    evidence_dir = Path("evidence_v2/KSI-TPR-02")
    findings = []
    score = 0
    service_inventory = []
    if evidence_dir.exists():
        inventory_files = [
            "Federal Information Mapping - Meridian LMS.pdf" 
        ]
        for doc in inventory_files:
            if (evidence_dir / doc).exists():
                service_inventory.append(doc)
        if service_inventory:
            findings.append(f"✅ Federal information service inventory: {', '.join(service_inventory)}")
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured

**Implementation Justification:** Validates service inventory, FedRAMP authorization verification, and secure configuration compliance for services handling federal data

**FedRAMP 20x Category:** Third-Party Information Resources

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 1 commands failed execution | ⚠️ No usable output

**Commands Executed:** 1
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*