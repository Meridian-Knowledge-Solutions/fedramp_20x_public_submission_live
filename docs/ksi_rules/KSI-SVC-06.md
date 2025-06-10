# KSI-SVC-06: Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates

*Generated on 2025-06-10 04:03:18 UTC*

## 📖 Overview

**KSI ID:** `KSI-SVC-06`
**Description:** Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates
**Justification:** Validates comprehensive automated key management from basic KMS availability to enterprise-grade key lifecycle management, covering encryption keys, certificates, rotation policies, access controls, hardware security modules, and organizational key governance with automated provisioning and compliance monitoring
**Last Validation:** ✅ 2025-06-10T04:03:18.719607
**Result:** ✅ Advanced automated key management with rotation and governance: ✅ 7 KMS keys for automated key management; ℹ️ No ACM certificates found (acceptable for low-impact); ✅ Key governance: 1 customer-managed aliases, 15 AWS-managed; ℹ️ No KMS-encrypted SecureString parameters found; ⚠️ Secrets Manager available but no automatic rotation configured; ✅ Modern certificate management: No legacy IAM certificates; ✅ Infrastructure as Code: 2/2 CloudFormation stacks for automated provisioning; ℹ️ No recent key creation events in audit trail; ✅ Enterprise governance: Organization-wide key management policies and standards

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws kms list-keys --output json`
   **Purpose:** Check KMS keys for automated key management and cryptographic service availability

2. **Command:** `aws acm list-certificates --output json`
   **Purpose:** Validate ACM certificates for automated certificate lifecycle management and SSL/TLS provisioning

3. **Command:** `aws kms list-aliases --output json`
   **Purpose:** Analyze KMS key aliases for key management governance and organizational naming standards

4. **Command:** `aws ssm describe-parameters --parameter-filters Key=Type,Values=SecureString --output json`
   **Purpose:** Check Systems Manager SecureString parameters for KMS-encrypted configuration management

5. **Command:** `aws secretsmanager list-secrets --output json`
   **Purpose:** Validate Secrets Manager for automated secrets rotation and centralized credential management

6. **Command:** `aws iam list-server-certificates --output json`
   **Purpose:** Check IAM server certificates for legacy certificate management and migration tracking

7. **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   **Purpose:** Analyze CloudFormation stacks for Infrastructure as Code key management and automated provisioning

8. **Command:** `aws config describe-config-rules --output json`
   **Purpose:** Check Config rules for key management compliance monitoring and policy enforcement

9. **Command:** `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateKey --start-time 2025-05-01 --output json`
   **Purpose:** Validate key management audit trail for creation, rotation, and access tracking

10. **Command:** `aws organizations describe-organization --output json`
   **Purpose:** Check enterprise-wide key management policies and organizational governance standards across accounts

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws kms list-keys --output json`
  - **Purpose:** Check KMS keys for automated key management and cryptographic service availability
- **Command:** `aws acm list-certificates --output json`
  - **Purpose:** Validate ACM certificates for automated certificate lifecycle management and SSL/TLS provisioning
- **Command:** `aws kms list-aliases --output json`
  - **Purpose:** Analyze KMS key aliases for key management governance and organizational naming standards
- **Command:** `aws ssm describe-parameters --parameter-filters Key=Type,Values=SecureString --output json`
  - **Purpose:** Check Systems Manager SecureString parameters for KMS-encrypted configuration management
- **Command:** `aws secretsmanager list-secrets --output json`
  - **Purpose:** Validate Secrets Manager for automated secrets rotation and centralized credential management
- **Command:** `aws iam list-server-certificates --output json`
  - **Purpose:** Check IAM server certificates for legacy certificate management and migration tracking
- **Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
  - **Purpose:** Analyze CloudFormation stacks for Infrastructure as Code key management and automated provisioning
- **Command:** `aws config describe-config-rules --output json`
  - **Purpose:** Check Config rules for key management compliance monitoring and policy enforcement
- **Command:** `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateKey --start-time 2025-05-01 --output json`
  - **Purpose:** Validate key management audit trail for creation, rotation, and access tracking
- **Command:** `aws organizations describe-organization --output json`
  - **Purpose:** Check enterprise-wide key management policies and organizational governance standards across accounts

## 🧠 Validation Logic

**Function:** `evaluate_KSI_SVC_06`

**Documentation:** Enhanced KSI-SVC-06: Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates
Expected: KMS Keys + ACM Certificates + Comprehensive automated key management

Scaling approach: Pilot (basic KMS availability) → Production (active key management) → Enterprise (comprehensive governance)

### Rule Implementation
```python
def evaluate_KSI_SVC_06(cli_output):
    """
    Enhanced KSI-SVC-06: Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates
    Expected: KMS Keys + ACM Certificates + Comprehensive automated key management
    
    Scaling approach: Pilot (basic KMS availability) → Production (active key management) → Enterprise (comprehensive governance)
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    kms_keys = None
    acm_certificates = None
    kms_aliases = None
    ssm_secure_parameters = None
    secrets_manager = None
    iam_certificates = None
    cloudformation_stacks = None
    config_rules = None
    cloudtrail_events = None
    organizations = None
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates

**Implementation Justification:** Validates comprehensive automated key management from basic KMS availability to enterprise-grade key lifecycle management, covering encryption keys, certificates, rotation policies, access controls, hardware security modules, and organizational key governance with automated provisioning and compliance monitoring

**FedRAMP 20x Category:** Service Configuration

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 10 commands failed execution | ⚠️ No usable output

**Commands Executed:** 10
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*