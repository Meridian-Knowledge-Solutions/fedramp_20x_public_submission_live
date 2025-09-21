# KSI-IAM-07: Securely manage the lifecycle and privileges of all accounts, roles, and groups

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-09-21 08:11

**What it validates:** Securely manage the lifecycle and privileges of all accounts, roles, and groups

**Why it matters:** Validates comprehensive account lifecycle management through automated IAM analysis covering service-oriented architecture, active lifecycle management, privilege automation, provisioning processes, and access review mechanisms with enterprise identity management integration

## Validation Method

1. `aws iam list-roles --output json`
   *Analyze IAM roles for service-oriented architecture and lifecycle management patterns*

2. `aws iam list-users --output json`
   *Analyze user accounts for lifecycle management and privilege patterns*

3. `aws iam list-policies --scope Local --output json`
   *Check custom policies for privilege management and access control automation*

4. `aws sso list-accounts --output json`
   *Validate AWS SSO/Identity Center for advanced account lifecycle management*

## Latest Results

PASS Advanced automated account lifecycle management (80%): PASS Service Oriented Architecture
- PASS Active Lifecycle Management
- FAIL Privilege Automation
- PASS Automated Provisioning
- PASS Regular Access Reviews

---
*Generated 2025-09-21 08:11 UTC*