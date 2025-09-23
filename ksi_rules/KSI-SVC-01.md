# KSI-SVC-01: Harden and review network and system configurations

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-09-23 13:26

**What it validates:** Harden and review network and system configurations

**Why it matters:** Validates comprehensive system hardening from basic network security to enterprise-grade multi-layer defense...

## Validation Method

1. `aws ec2 describe-security-groups --output json`
   *Analyze security groups for network hardening and restrictive access controls*

2. `aws ec2 describe-instances --output json`
   *Check instance configurations for system hardening and security posture*

3. `aws ssm describe-instance-information --output json`
   *Validate Systems Manager agent coverage for centralized configuration management*

4. `aws ssm describe-patch-baselines --output json`
   *Check patch baselines for automated system hardening and vulnerability management*

5. `aws configservice describe-config-rules --output json`
   *Validate Config rules for automated configuration compliance and hardening*

6. `aws ec2 describe-network-acls --output json`
   *Check Network ACLs for subnet-level network hardening and traffic control*

7. `aws guardduty list-detectors --output json`
   *Validate GuardDuty for threat detection and security monitoring*

8. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Check WAF for application-layer protection and attack mitigation*

9. `aws inspector2 get-configuration --output json`
   *Validate Inspector for vulnerability assessment and security hardening*

10. `aws organizations describe-organization --output json`
   *Check enterprise-wide hardening policies and organizational security governance*

11. `aws ec2 describe-vpc-endpoints --output json`
   *ADDED: Check for VPC endpoints for secure service access.*

## Latest Results

PASS Enterprise-grade network and system hardening with comprehensive governance (82%): PASS Network hardening foundation: 16 security groups (14 hardened, 2 require review)
- PASS System configuration management: 6 instances configured
- PASS Comprehensive system management: 6/6 instances under SSM (100% coverage)
- PASS Automated patch management: 17 patch baselines configured
- INFO Config service available but no rules configured
- INFO 1 default Network ACLs (consider custom rules for enhanced security)
- PASS Threat detection enabled: 1 GuardDuty detectors monitoring for threats
- PASS Application layer protection: 1 Web ACLs configured
- PASS Secure service access: 7 VPC endpoints (4 interface, 1 gateway)
- PASS Enterprise-wide security governance: AWS Organizations enables centralized hardening policies
- PASS Advanced organization features: SCPs and advanced governance capabilities enabled

---
*Generated 2025-09-23 13:26 UTC*