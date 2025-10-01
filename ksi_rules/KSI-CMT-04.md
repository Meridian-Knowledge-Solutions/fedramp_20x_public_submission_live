# KSI-CMT-04: Use codified change templates with approval rules

## Overview

**Category:** Change Management
**Status:** FAIL
**Last Check:** 2025-10-01 08:13

**What it validates:** Use codified change templates with approval rules

**Why it matters:** Validates comprehensive change approval automation from basic templates to enterprise-grade policy-driven approvals and governance

## Validation Method

1. `aws ssm list-documents --document-filter-list 'key=DocumentType,value=Automation' --query 'DocumentIdentifiers[?contains(Name, `Change`) || contains(Name, `Template`)].{Name:Name}' --output json`
   *Check SSM change management templates with approval workflows*

2. `DOC_NAME=$(aws ssm list-documents --document-filter-list 'key=DocumentType,value=Automation' --query 'DocumentIdentifiers[0].Name' --output text 2>/dev/null || echo 'none'); if [ "$DOC_NAME" != "none" ]; then aws ssm get-document --name "$DOC_NAME" --output json; else echo '{"Content": null}'; fi`
   *Validate change template content and approval configuration*

## Latest Results

- FAIL No SSM Change Manager templates found - change procedure not codified

---
*Generated 2025-10-01 08:13 UTC*