# KSI-CNA-08: Use native security capabilities including agent-based security

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-10-01 18:40

**What it validates:** Use native security capabilities including agent-based security

**Why it matters:** Validates comprehensive native security from basic Security Hub to enterprise-grade automated remediation and agent-based protection

## Validation Method

1. `aws securityhub get-enabled-standards --output json`
   *Check Security Hub enabled standards for native security monitoring*

2. `aws configservice describe-config-rules --output json`
   *Validate AWS Config rules for native compliance automation*

3. `aws configservice describe-remediation-configurations --config-rule-names $(aws configservice describe-config-rules --query 'ConfigRules[0].ConfigRuleName' --output text) --output json || echo '{"RemediationConfigurations": []}'`
   *Check automated remediation configurations for Config rules*

4. `aws lambda list-functions --output json`
   *Validate custom security automation and remediation functions*

5. `aws securityhub describe-organization-configuration --output json`
   *Check Security Hub organization-wide configuration*

6. `aws configservice describe-configuration-aggregators --output json || echo '{"ConfigurationAggregators": []}'`
   *Validate Config aggregators for centralized compliance monitoring*

## Latest Results

FAIL Insufficient automated enforcement for Moderate baseline (12%): Config remediation required. FAIL Security Hub not enabled - required for centralized security monitoring
- FAIL No AWS Config rules detected - required for compliance automation
- FAIL No Config remediations - automated enforcement not proven
-   ↳ Moderate baseline requires automated response to non-compliance
- PASS Custom automation: 2 security Lambda function(s)

---
*Generated 2025-10-01 18:40 UTC*