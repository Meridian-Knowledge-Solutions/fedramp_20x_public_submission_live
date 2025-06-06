# KSI-SVC-06: Use automated key management systems

*Generated on 2025-06-06 10:12:33 UTC*

## 📖 Overview

**KSI ID:** `KSI-SVC-06`
**Description:** Use automated key management systems
**Justification:** Validates automated key management through AWS KMS and certificate management
**Last Validation:** ❌ 2025-06-06T10:12:33.757505
**Result:** ❌ No automated key management systems found: ℹ️ No ACM certificates found (acceptable for low-impact)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws kms list-keys --output json`
   **Purpose:** Check KMS keys for automated key management

2. **Command:** `aws acm list-certificates --output json`
   **Purpose:** Validate certificate management through ACM

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws kms list-keys --output json`
  - **Purpose:** Check KMS keys for automated key management
- **Command:** `aws acm list-certificates --output json`
  - **Purpose:** Validate certificate management through ACM

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_06`

**Documentation:** Simple rule for KSI-SVC-06: Automated key management systems
Expected: KMS Keys + ACM Certificates

### Rule Implementation
```python
def evaluate_KSI_SVC_06(cli_output):
    """
    Simple rule for KSI-SVC-06: Automated key management systems
    Expected: KMS Keys + ACM Certificates
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    kms_keys = None
    acm_certificates = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-keys" in cli_command:
            kms_keys = raw_output.get("Keys", [])
        elif "list-certificates" in cli_command:
            acm_certificates = raw_output.get("CertificateSummaryList", [])
    findings = []
    key_management_systems = 0
    if kms_keys is not None:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use automated key management systems

**Implementation Justification:** Validates automated key management through AWS KMS and certificate management

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*