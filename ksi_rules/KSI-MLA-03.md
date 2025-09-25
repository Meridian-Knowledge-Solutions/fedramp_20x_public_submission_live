# KSI-MLA-03: Rapidly detect and remediate or mitigate vulnerabilities

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-25 19:26

**What it validates:** Rapidly detect and remediate or mitigate vulnerabilities

**Why it matters:** Validates comprehensive vulnerability detection and response from basic security monitoring to enterprise-grade automated remediation, threat intelligence, and cross-account vulnerability management

## Validation Method

1. `aws securityhub get-enabled-standards --region us-east-1 --output json`
   *Check Security Hub standards for foundational vulnerability detection and compliance monitoring*

2. `aws inspector2 get-configuration --output json`
   *Validate Inspector automated scanning for EC2, container, and application vulnerabilities*

3. `aws securityhub get-findings --filters '{"RecordState":[{"Value":"ACTIVE","Comparison":"EQUALS"}]}' --max-results 50 --output json`
   *Analyze active security findings for rapid vulnerability detection and response assessment*

4. `aws ssm describe-patch-baselines --output json`
   *Check automated patch management for rapid vulnerability remediation*

5. `aws lambda list-functions --output json`
   *Validate automated response functions for vulnerability remediation and incident handling*

6. `aws cloudwatch describe-alarms --output json`
   *Check real-time alerting for rapid vulnerability detection and notification*

7. `aws config describe-config-rules --output json`
   *Validate continuous compliance monitoring for configuration vulnerability detection*

8. `aws organizations describe-organization --output json`
   *Check enterprise-wide vulnerability management and cross-account detection capabilities*

## Latest Results

PASS Solid vulnerability detection foundation with automated capabilities (33%): FAIL Security Hub not configured for vulnerability detection
- WARNING Inspector configured but no scanning features enabled
- PASS Security automation: 2 Lambda functions for security operations
- PASS Real-time threat detection: 1 CloudWatch alarms for rapid vulnerability alerting
- PASS Enterprise vulnerability management: AWS Organizations enables centralized multi-account detection

---
*Generated 2025-09-25 19:26 UTC*