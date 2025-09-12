# KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-12 02:36

**What it validates:** Perform authenticated vulnerability scanning on information resources

**Why it matters:** Validates comprehensive authenticated vulnerability scanning from basic service availability to enterprise-grade multi-service scanning, container security, and cloud-native vulnerability management

## Validation Method

1. `aws inspector2 list-coverage --output json`
   *Check Inspector coverage for authenticated vulnerability scanning of EC2 and container resources*

2. `aws inspector2 get-configuration --output json`
   *Validate Inspector service enablement and scanning configuration status*

3. `aws ec2 describe-instances --output json`
   *Analyze EC2 instances available for authenticated vulnerability scanning assessment*

4. `aws ecr describe-repositories --output json`
   *Check container registries for authenticated container image vulnerability scanning*

5. `aws lambda list-functions --output json`
   *Validate serverless functions for code vulnerability analysis and dependency scanning*

6. `aws ssm describe-instance-information --output json`
   *Check Systems Manager agent coverage for authenticated system-level scanning*

7. `aws securityhub get-findings --filters '{"ProductName":[{"Value":"Inspector","Comparison":"EQUALS"}]}' --max-results 20 --output json`
   *Analyze authenticated scanning results and vulnerability findings integration*

8. `aws organizations describe-organization --output json`
   *Check enterprise-wide authenticated vulnerability scanning and cross-account coverage*

## Latest Results

PASS Enterprise-grade authenticated vulnerability scanning with comprehensive coverage (100%): PASS Inspector service operational: Responds to coverage queries and scanning requests
- PASS Comprehensive scanning coverage: 5/5 instances under authenticated scanning
- PASS Multi-service authenticated scanning: Inspector EC2, ECR scanning enabled
- PASS Comprehensive service scanning: Both EC2 and ECR authenticated vulnerability assessment enabled
- PASS System-level scanning capability: 5/5 SSM-managed instances for authenticated system assessment
- PASS Serverless code analysis: 7 Lambda functions available for authenticated code vulnerability scanning
- PASS Active Lambda scanning: 7 functions actively scanned by Inspector
- PASS Comprehensive workload coverage: 3 service types available for authenticated scanning (EC2, Lambda, SSM)
- PASS Active vulnerability intelligence: 20 authenticated scan findings (0 critical, 5 high, 14 medium, 1 low)
- PASS Comprehensive vulnerability discovery: High-volume scanning indicates thorough authenticated assessment
- PASS Automated discovery: Inspector service can automatically detect and scan new resources
- PASS Enterprise scanning governance: AWS Organizations enables centralized multi-account vulnerability scanning
- PASS Enterprise scanning integration: Multi-service Inspector configuration for comprehensive authenticated assessment
- PASS Enterprise-scale scanning: 12 total resources requiring authenticated vulnerability assessment

---
*Generated 2025-09-12 02:36 UTC*