# KSI-CNA-05: Protect against denial of service attacks and unwanted spam

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-10-01 03:22

**What it validates:** Protect against denial of service attacks and unwanted spam

**Why it matters:** Validates multi-layered protection against both network/application-layer denial of service attacks and email-based spam by checking for AWS Shield, WAF, resilient architecture, and email authentication standards like SES, SPF, DKIM, and DMARC.

## Validation Method

1. `aws shield describe-subscription --output json`
   *Check for AWS Shield Advanced for premium network-layer DDoS protection.*

2. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Validate regional WAF for application-layer DDoS protection.*

3. `aws wafv2 list-web-acls --scope CLOUDFONT --output json`
   *Check CloudFront WAF rules for edge-layer application protection.*

4. `aws cloudfront list-distributions --output json`
   *Validate CloudFront distributions for edge-layer DDoS mitigation.*

5. `aws elbv2 describe-load-balancers --output json`
   *Check for multi-AZ load balancers for service resilience.*

6. `aws autoscaling describe-auto-scaling-groups --output json`
   *Validate Auto Scaling Groups for capacity-based DDoS mitigation.*

7. `aws route53 list-hosted-zones --output json`
   *Check Route 53 for managed DNS protection and to find zones for record analysis.*

8. `aws cloudwatch describe-alarms --output json`
   *Verify CloudWatch alarms for DDoS detection and automated response.*

9. `aws sesv2 list-email-identities --output json`
   *Check for verified SES identities to validate secure email sending for spam prevention.*

10. `aws route53 list-resource-record-sets --hosted-zone-id <HOSTED_ZONE_ID>`
   *Check DNS records for SPF and DMARC. The <HOSTED_ZONE_ID> placeholder MUST be replaced by the execution script.*

11. `aws sesv2 get-email-identity --email-identity <DOMAIN_IDENTITY>`
   *Check for SES DKIM tokens. The <DOMAIN_IDENTITY> placeholder MUST be replaced by the execution script.*

## Latest Results

FAIL Insufficient protection against DDoS and/or Spam (50%): PASS Network-layer protection: AWS Shield Standard is automatically enabled.
- PASS Application-layer protection: 1 Regional WAF(s) found.
- PASS Service resilience: Multi-AZ load balancers are in use.
- PASS DNS protection: 1 Route 53 hosted zone(s) provide managed DNS.

---
*Generated 2025-10-01 03:22 UTC*