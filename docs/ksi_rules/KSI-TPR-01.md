# KSI-TPR-01: Identify all third-party information resources

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-09-12 02:36

**What it validates:** Identify all third-party information resources

**Why it matters:** AWS API discovery of external integrations, identity providers, and cross-account relationships provides comprehensive third-party resource identification

## Validation Method

1. `aws iam list-saml-providers --output json`
   *SAML identity providers indicating external authentication integrations*

2. `aws iam list-open-id-connect-providers --output json`
   *OIDC providers for modern OAuth2/OpenID Connect integrations*

3. `aws organizations list-accounts --output json`
   *AWS organization accounts to identify multi-account third-party relationships*

4. `aws iam list-roles --query 'Roles[?contains(AssumeRolePolicyDocument, `sts:AssumeRole`)]' --output json`
   *Cross-account IAM roles indicating external account trust relationships*

5. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=AssumeRole --start-time 2024-08-01 --end-time 2024-09-01 --max-items 20 --output json`
   *Recent cross-account access events to identify active third-party integrations*

6. `aws apigateway get-rest-apis --output json`
   *API Gateway endpoints that may expose services to third parties*

## Latest Results

PASS Good third-party integration coverage: 2 integrations identified
- PASS SAML identity providers: 1 external authentication integrations
- PASS OIDC providers: 1 modern OAuth2/OpenID Connect integrations
- PASS API Gateway endpoints: 2 APIs potentially exposing services to third parties

---
*Generated 2025-09-12 02:36 UTC*