# KSI-SVC-03: Encrypt all federal and sensitive information at rest

<<<<<<< Updated upstream
*Generated on 2025-06-06 08:21:01 UTC*
=======
*Generated on 2025-06-06 08:22:08 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-SVC-03`
**Description:** Encrypt all federal and sensitive information at rest
**Justification:** Validates at-rest encryption for S3, EBS, RDS, and other storage services
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-06T08:21:01.667230
=======
**Last Validation:** ✅ 2025-06-06T08:22:08.663201
>>>>>>> Stashed changes
**Result:** ✅ At-rest encryption configured: ✅ 2 S3 buckets found (encryption validation requires bucket-level check); ℹ️ No EBS volumes found

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws s3api list-buckets --output json`
   **Purpose:** Get S3 buckets for encryption validation

2. **Command:** `aws ec2 describe-volumes --output json`
   **Purpose:** Check EBS volume encryption status

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws s3api list-buckets --output json`
  - **Purpose:** Get S3 buckets for encryption validation
- **Command:** `aws ec2 describe-volumes --output json`
  - **Purpose:** Check EBS volume encryption status

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_03`

**Documentation:** Simple rule for KSI-SVC-03: At-rest encryption
Expected: S3 Buckets + EBS Volumes

### Rule Implementation
```python
def evaluate_KSI_SVC_03(cli_output):
    """
    Simple rule for KSI-SVC-03: At-rest encryption
    Expected: S3 Buckets + EBS Volumes
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    s3_buckets = None
    ebs_volumes = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-buckets" in cli_command:
            s3_buckets = raw_output.get("Buckets", [])
        elif "describe-volumes" in cli_command:
            ebs_volumes = raw_output.get("Volumes", [])
    findings = []
    encrypted_resources = 0
    total_resources = 0
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Encrypt all federal and sensitive information at rest

**Implementation Justification:** Validates at-rest encryption for S3, EBS, RDS, and other storage services

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received

**Commands Executed:** 2
**Validation Method:** multi-command

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*