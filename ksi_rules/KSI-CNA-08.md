# KSI-CNA-08: Use automated services to persistently assess the security posture of all services and automatically enforce secure operations.

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-10-01 03:22

**What it validates:** Use automated services to persistently assess the security posture of all services and automatically enforce secure operations.

**Why it matters:** Validates persistent security posture assessment with mandatory proof of automated enforcement. Requires either AWS Config remediation configurations or SSM State Manager associations as direct evidence of enforcement. Assesses active Config recording, comprehensive Security Hub standards, and sufficient compliance rules. Enterprise capabilities (Organization-level Security Hub and Config aggregators) provide additional scoring but are not required for base compliance.

## Validation Method

1. `aws securityhub get-enabled-standards --output json`
   *Verify Security Hub standards are enabled, prioritizing AWS Foundational Security Best Practices for comprehensive coverage.*

2. `aws configservice describe-configuration-recorder-status --output json`
   *Confirm AWS Config recorder is actively recording configurations with SUCCESS status.*

3. `aws configservice describe-config-rules --output json`
   *Inventory Config rules for persistent compliance checking. Moderate baseline requires minimum 8 rules for reasonable service coverage.*

4. `aws configservice describe-remediation-configurations --output json`
   *ENFORCEMENT PROOF: Validate Config rules have automated remediation actions attached. Required for passing grade.*

5. `aws ssm list-associations --output json`
   *ENFORCEMENT PROOF: Verify SSM State Manager associations provide persistent configuration enforcement. Required for passing grade if Config remediation absent.*

6. `aws lambda list-functions --output json`
   *Identify Lambda functions for custom remediation logic. Provides supporting evidence but not sufficient alone.*

7. `aws securityhub list-organization-configuration --output json`
   *ENTERPRISE: Detect centralized Security Hub management across AWS Organization. Requires delegated admin permissions.*

8. `aws configservice describe-configuration-aggregators --output json`
   *ENTERPRISE: Detect multi-account compliance monitoring via Config aggregators.*

## Latest Results

- FAIL Insufficient continuous security assessment for Moderate baseline (33%): PASS Automated remediation: 2 security automation functions

---
*Generated 2025-10-01 03:22 UTC*