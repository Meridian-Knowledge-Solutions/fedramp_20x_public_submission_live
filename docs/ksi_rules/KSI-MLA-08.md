# KSI-MLA-08: Use a least-privileged, role and attribute-based, and just-in-time access authorization model for access to log data

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-09-15 01:58

**What it validates:** Use a least-privileged, role and attribute-based, and just-in-time access authorization model for access to log data

**Why it matters:** Validates advanced RBAC with JIT capabilities for log access through specialized role analysis, privilege management automation, attribute-based access control, and just-in-time access mechanisms covering log-specific permissions and granular access control

## Validation Method

1. `aws iam list-roles --output json`
   *Analyze roles for log-specific RBAC and least privilege access patterns*

2. `aws iam list-policies --scope Local --output json`
   *Check custom policies for log-specific permissions and attribute-based access*

3. `aws logs describe-log-groups --output json`
   *Analyze log resources for attribute-based access control patterns*

4. `aws sts assume-role --role-arn arn:aws:iam::ACCOUNT:role/LogAccessRole --role-session-name JITTest --output json`
   *Test just-in-time access capability for log data access (replace ACCOUNT and role as needed)*

## Latest Results

PASS Good log access control - enhance JIT capabilities (60%): PASS Role-based log access: 3 log-specific roles
- PASS Least privilege design: Multiple specialized log access roles
- PASS Attribute-based access: 4 different retention policies suggest granular access control

---
*Generated 2025-09-15 01:58 UTC*