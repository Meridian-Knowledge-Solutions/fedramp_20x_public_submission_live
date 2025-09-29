# KSI-CMT-04: Have a documented and implemented change management procedure

## Overview

**Category:** Change Management
**Status:** FAIL
**Last Check:** 2025-09-29 22:00

**What it validates:** Have a documented and implemented change management procedure

**Why it matters:** Validates that the change management procedure is codified and enforced using AWS Systems Manager Change Manager templates with approval workflows, providing live, auditable evidence of an implemented control.

## Validation Method

1. `aws ssm list-documents --document-filter-list 'key=DocumentType,value=ChangeTemplate' --query 'DocumentIdentifiers[*].{Name:Name}'`
   *Lists all active SSM Change Manager templates in the account. This is the primary evidence of a codified change procedure.*

2. `aws ssm get-document --name TEMPLATE_NAME`
   *Retrieves the content of a specific Change Template. The evaluation logic will call this for each template found to inspect its approval configuration. TEMPLATE_NAME is a placeholder.*

## Latest Results

- No rule function found: evaluate_KSI_CMT_04

---
*Generated 2025-09-29 22:00 UTC*