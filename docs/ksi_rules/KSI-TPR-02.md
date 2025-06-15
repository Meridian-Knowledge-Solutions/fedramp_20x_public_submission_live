# KSI-TPR-02: Regularly confirm services handling federal information are FedRAMP authorized and securely configured

*Generated on 2025-06-15 03:24:19 UTC*

## 📖 Overview

**KSI ID:** `KSI-TPR-02`
**Description:** Regularly confirm services handling federal information are FedRAMP authorized and securely configured
**Justification:** Validates service inventory, FedRAMP authorization verification, and secure configuration compliance for services handling federal data
**Last Validation:** ✅ 2025-06-15T03:24:19.410153
**Result:** ✅ Comprehensive FedRAMP service verification with integrated documentation (100%): ℹ️ Evidence validation triggered via CLI; ✅ Comprehensive federal information mapping: Federal Information Mapping - Meridian LMS.pdf; ✅ FedRAMP authorization verification included in comprehensive mapping; ✅ Security configuration compliance included in comprehensive mapping; ✅ Regular verification process included in comprehensive mapping

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
    try:
        if isinstance(cli_output, dict) and "commands" in cli_output:
            for cmd in cli_output.get("commands", []):
                if isinstance(cmd, dict):
                    cli_command = cmd.get("cli_command", "")
                    if "evidence_check" in cli_command:
                        findings.append("ℹ️ Evidence validation triggered via CLI")
    except Exception as e:
        findings.append(f"ℹ️ CLI output processing note: {str(e)}")
    service_inventory = []
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