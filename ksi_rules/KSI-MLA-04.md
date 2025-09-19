# KSI-MLA-04: Perform authenticated vulnerability scanning on information resources

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-16 07:31

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

- PASS KSI retired in Phase Two - superseded by KSI-MLA-03 (FedRAMP Vulnerability Response and Detection standard)

---
*Generated 2025-09-16 07:31 UTC*