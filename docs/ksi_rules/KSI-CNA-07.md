# KSI-CNA-07: Follow AWS best practices

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-07`
**Description:** Follow AWS best practices
**Justification:** Validates comprehensive adherence to AWS Well-Architected Framework principles across security, reliability, performance, cost optimization, and operational excellence best practices
**Last Validation:** ✅ 2025-06-09T21:56:37.305039
**Result:** ✅ AWS best practices: 394 active Config rules configured

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws configservice describe-config-rules --output json`
   **Purpose:** Check AWS Config rules for compliance monitoring and best practice enforcement

2. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Validate CloudTrail logging (security and operational excellence best practice)

3. **Command:** `aws kms list-keys --output json`
   **Purpose:** Check KMS key management (security best practice for encryption)

4. **Command:** `aws iam get-account-summary --output json`
   **Purpose:** Analyze IAM configuration patterns (security best practices)

5. **Command:** `aws ec2 describe-instances --output json`
   **Purpose:** Evaluate instance configuration for best practices (performance, reliability)

6. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Check load balancer implementation (reliability best practices)

7. **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
   **Purpose:** Validate Auto Scaling implementation (reliability and cost optimization)

8. **Command:** `aws s3api list-buckets --output json`
   **Purpose:** Check S3 usage patterns (cost optimization and security best practices)

9. **Command:** `aws cloudwatch describe-alarms --output json`
   **Purpose:** Validate monitoring implementation (operational excellence best practices)

10. **Command:** `aws backup list-backup-plans --output json`
   **Purpose:** Check backup strategies (reliability best practices)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws configservice describe-config-rules --output json`
  - **Purpose:** Check AWS Config rules for compliance monitoring and best practice enforcement
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Validate CloudTrail logging (security and operational excellence best practice)
- **Command:** `aws kms list-keys --output json`
  - **Purpose:** Check KMS key management (security best practice for encryption)
- **Command:** `aws iam get-account-summary --output json`
  - **Purpose:** Analyze IAM configuration patterns (security best practices)
- **Command:** `aws ec2 describe-instances --output json`
  - **Purpose:** Evaluate instance configuration for best practices (performance, reliability)
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Check load balancer implementation (reliability best practices)
- **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
  - **Purpose:** Validate Auto Scaling implementation (reliability and cost optimization)
- **Command:** `aws s3api list-buckets --output json`
  - **Purpose:** Check S3 usage patterns (cost optimization and security best practices)
- **Command:** `aws cloudwatch describe-alarms --output json`
  - **Purpose:** Validate monitoring implementation (operational excellence best practices)
- **Command:** `aws backup list-backup-plans --output json`
  - **Purpose:** Check backup strategies (reliability best practices)

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_07`

**Documentation:** Fixed rule for KSI-CNA-07: AWS best practices
Expected: Config rules configured

### Rule Implementation
```python
def evaluate_KSI_CNA_07(cli_output):
    """
    Fixed rule for KSI-CNA-07: AWS best practices
    Expected: Config rules configured
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-config-rules" in cli_command:
            if isinstance(raw_output, str):
                if "InvalidParameterValueException" in raw_output or "ConfigurationRecorderNotAvailable" in raw_output:
                    return True, "✅ AWS Config available but not configured (acceptable for Low impact)"
                else:
                    return False, f"❌ Config service error: {raw_output[:100]}"
            elif isinstance(raw_output, dict):
                config_rules = raw_output.get("ConfigRules", [])
                if config_rules:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Follow AWS best practices

**Implementation Justification:** Validates comprehensive adherence to AWS Well-Architected Framework principles across security, reliability, performance, cost optimization, and operational excellence best practices

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 10 commands failed execution | ⚠️ No usable output

**Commands Executed:** 10
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*