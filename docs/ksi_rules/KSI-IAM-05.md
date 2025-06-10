# KSI-IAM-05: Apply zero trust design principles

<<<<<<< Updated upstream
*Generated on 2025-06-10 13:17:42 UTC*
=======
*Generated on 2025-06-10 13:18:11 UTC*
>>>>>>> Stashed changes

## 📖 Overview

**KSI ID:** `KSI-IAM-05`
**Description:** Apply zero trust design principles
**Justification:** Validates comprehensive zero trust implementation through Identity Center (modern approach), network security, continuous monitoring, conditional access, and secure communications patterns
<<<<<<< Updated upstream
**Last Validation:** ✅ 2025-06-10T13:17:42.448965
=======
**Last Validation:** ✅ 2025-06-10T13:18:11.040815
>>>>>>> Stashed changes
**Result:** ⚠️ Basic zero trust elements (42%): ✅ Modern identity platform: IAM Identity Center configured (1 instance(s)); ✅ Multi-factor authentication: 6 MFA devices configured; ✅ Network micro-segmentation: 1 restrictive vs 0 permissive security groups; ❌ Permanent credentials: Using IAM user (not zero trust); ⚠️ VPC endpoint information not available; ❌ No continuous monitoring found (zero trust requires comprehensive logging)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws sso-admin list-instances --output json`
   **Purpose:** Check IAM Identity Center for modern zero trust user access patterns

2. **Command:** `aws cloudtrail describe-trails --output json`
   **Purpose:** Validate continuous monitoring and verification logging (must be active)

3. **Command:** `aws cloudtrail get-trail-status --name $(aws cloudtrail describe-trails --query 'trailList[0].Name' --output text) --output json 2>/dev/null || echo '{"IsLogging":false}'`
   **Purpose:** Verify CloudTrail is actively logging (zero trust requires continuous monitoring)

4. **Command:** `aws ec2 describe-security-groups --output json`
   **Purpose:** Analyze network micro-segmentation and least privilege network access

5. **Command:** `aws ec2 describe-vpc-endpoints --output json`
   **Purpose:** Validate secure private communications (VPC endpoints for AWS services)

6. **Command:** `aws iam list-virtual-mfa-devices --output json`
   **Purpose:** Check multi-factor authentication enforcement (verify explicitly principle)

7. **Command:** `aws sts get-caller-identity --output json`
   **Purpose:** Validate current session type (temporary credentials indicate zero trust access)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws sso-admin list-instances --output json`
  - **Purpose:** Check IAM Identity Center for modern zero trust user access patterns
- **Command:** `aws cloudtrail describe-trails --output json`
  - **Purpose:** Validate continuous monitoring and verification logging (must be active)
- **Command:** `aws cloudtrail get-trail-status --name $(aws cloudtrail describe-trails --query 'trailList[0].Name' --output text) --output json 2>/dev/null || echo '{"IsLogging":false}'`
  - **Purpose:** Verify CloudTrail is actively logging (zero trust requires continuous monitoring)
- **Command:** `aws ec2 describe-security-groups --output json`
  - **Purpose:** Analyze network micro-segmentation and least privilege network access
- **Command:** `aws ec2 describe-vpc-endpoints --output json`
  - **Purpose:** Validate secure private communications (VPC endpoints for AWS services)
- **Command:** `aws iam list-virtual-mfa-devices --output json`
  - **Purpose:** Check multi-factor authentication enforcement (verify explicitly principle)
- **Command:** `aws sts get-caller-identity --output json`
  - **Purpose:** Validate current session type (temporary credentials indicate zero trust access)

## 🧠 Validation Logic

**Function:** `evaluate_KSI_IAM_05`

**Documentation:** Enhanced KSI-IAM-05: Apply zero trust design principles

Validates comprehensive zero trust implementation:
- Never trust, always verify (MFA, continuous authentication)
- Assume breach (network segmentation, monitoring)
- Verify explicitly (multi-factor, device compliance)
- Least privilege access (just-in-time, time-limited sessions)
- Secure communications (private networks, encryption)
- Monitor everything (active logging, real-time visibility)

### Rule Implementation
```python
def evaluate_KSI_IAM_05(cli_output):
    """
    Enhanced KSI-IAM-05: Apply zero trust design principles
    
    Validates comprehensive zero trust implementation:
    - Never trust, always verify (MFA, continuous authentication)
    - Assume breach (network segmentation, monitoring)
    - Verify explicitly (multi-factor, device compliance)
    - Least privilege access (just-in-time, time-limited sessions)
    - Secure communications (private networks, encryption)
    - Monitor everything (active logging, real-time visibility)
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    sso_instances = None
    cloudtrail_trails = None
    trail_status = None
    security_groups = None
    vpc_endpoints = None
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Apply zero trust design principles

**Implementation Justification:** Validates comprehensive zero trust implementation through Identity Center (modern approach), network security, continuous monitoring, conditional access, and secure communications patterns

**FedRAMP 20x Category:** Identity and Access Management

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 7 commands failed execution | ⚠️ No usable output

**Commands Executed:** 7
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*