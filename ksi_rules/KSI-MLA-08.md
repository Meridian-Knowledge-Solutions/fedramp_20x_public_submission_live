# KSI-MLA-08: Protect audit logs to support after-the-fact investigations

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-10-03 02:59

**What it validates:** Protect audit logs to support after-the-fact investigations

**Why it matters:** Validates comprehensive audit log protection from basic S3 retention to enterprise-grade immutable storage and forensic capabilities

## Validation Method

1. `aws iam list-roles --output json`
   *Check IAM roles for least privilege access to audit logs*

2. `aws iam list-policies --scope Local --output json`
   *Validate IAM policies restricting audit log modifications*

3. `aws logs describe-log-groups --output json`
   *Check CloudWatch Logs encryption and retention for audit protection*

## Latest Results

PASS Good log access control foundation (50%): PASS Rbac Log Roles Found
- PASS Least Privilege Design Indicated
- FAIL Jit Access Capability Proven
- FAIL Log Specific Permissions Exist

---
*Generated 2025-10-03 02:59 UTC*