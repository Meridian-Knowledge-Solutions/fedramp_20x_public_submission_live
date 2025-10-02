# KSI-CNA-08: Use automated services to persistently assess the security posture of all services and automatically enforce secure operations

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-10-02 03:01

**What it validates:** Use automated services to persistently assess the security posture of all services and automatically enforce secure operations

**Why it matters:** Validates both continuous security assessment (Config rules) AND automated enforcement (remediation configurations or SSM associations) as required by FedRAMP Moderate baseline

## Validation Method

1. `aws securityhub get-enabled-standards --output json`
   *Validate Security Hub standards for persistent assessment framework*

2. `aws configservice describe-config-rules --output json`
   *Count Config rules providing persistent security assessment*

3. `aws configservice describe-configuration-recorder-status --output json`
   *Verify Config recorder actively capturing assessment data*

4. `aws configservice describe-remediation-configurations --output json || echo '{"RemediationConfigurations": []}'`
   *Validate automated enforcement via Config remediation configurations*

5. `aws ssm list-associations --output json || echo '{"Associations": []}'`
   *Validate automated enforcement via SSM State Manager associations*

6. `aws securityhub describe-hub --output json`
   *Confirm Security Hub enabled for assessment aggregation*

7. `aws lambda list-functions --output json`
   *Identify custom enforcement automation capabilities*

## Latest Results

Excellent measurement posture (83%): Basic framework: 1 Security Hub standard(s)
- Extensive instrumentation: 327 Config rules
- Active measurement: Config recorder capturing data
- Centralized visibility: Security Hub enabled

---
*Generated 2025-10-02 03:01 UTC*