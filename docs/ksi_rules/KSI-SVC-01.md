# KSI-SVC-01: Harden and review network and system configurations

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-06-24 18:34

**What it validates:** Harden and review network and system configurations

**Why it matters:** Validates comprehensive network and system hardening from basic security group configuration to enterprise-grade multi-layer defense, compliance monitoring, and advanced threat detection across cloud-native and traditional infrastructure

## Validation Method

1. `aws ec2 describe-security-groups --output json`
   *Check security group configurations for network hardening and access control validation*

2. `aws ec2 describe-instances --output json`
   *Review instance configurations and security settings for system hardening assessment*

3. `aws ec2 describe-network-acls --output json`
   *Analyze Network ACLs for subnet-level traffic filtering and defense-in-depth validation*

4. `aws config describe-config-rules --output json`
   *Check AWS Config rules for automated configuration compliance and hardening validation*

5. `aws guardduty list-detectors --output json`
   *Validate GuardDuty threat detection service enablement for network and system security monitoring*

6. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Check Web Application Firewall configuration for application-layer hardening and protection*

7. `aws ssm describe-patch-baselines --output json`
   *Analyze patch management baselines for systematic security updates and vulnerability remediation*

8. `aws ssm describe-instance-information --output json`
   *Check Systems Manager coverage for centralized system configuration management and compliance*

9. `aws inspector2 get-configuration --output json`
   *Validate Amazon Inspector for automated security assessments and vulnerability scanning*

10. `aws organizations describe-organization --output json`
   *Check enterprise-wide security policies and organizational hardening standards across accounts*

## Latest Results

PASS Production-ready multi-layer defense and automated compliance (72%): PASS Network hardening foundation: 14 security groups (14 hardened, 0 require review)
- PASS System configuration management: 4 instances configured
- PASS Comprehensive system management: 4/4 instances under SSM (100% coverage)
- PASS Automated patch management: 17 patch baselines configured
- INFO Config service available but no rules configured
- INFO 1 default Network ACLs (consider custom rules for enhanced security)
- PASS Threat detection enabled: 1 GuardDuty detectors monitoring for threats
- PASS Application layer protection: 1 Web ACLs configured
- PASS Enterprise-wide security governance: AWS Organizations enables centralized hardening policies
- PASS Advanced organization features: SCPs and advanced governance capabilities enabled

---
*Generated 2025-06-24 18:34 UTC*