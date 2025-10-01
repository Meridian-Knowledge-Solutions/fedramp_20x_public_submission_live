# KSI-CNA-05: Protect against denial of service attacks and unwanted spam

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-10-01 22:14

**What it validates:** Protect against denial of service attacks and unwanted spam

**Why it matters:** Validates DDoS protection through WAF, Shield, Multi-AZ architecture, and DNS security. Email spam protection validated only when email services are detected (SES, MX records)

## Validation Method

1. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Check Regional WAF for Layer 7 DDoS protection*

2. `aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1 --output json`
   *Validate CloudFront WAF for edge DDoS protection*

3. `aws cloudfront list-distributions --output json`
   *Check CloudFront distributions for global DDoS mitigation*

4. `aws elbv2 describe-load-balancers --output json`
   *Validate Multi-AZ load balancers for service resilience*

5. `aws autoscaling describe-auto-scaling-groups --output json`
   *Check auto-scaling for capacity-based DDoS mitigation*

6. `aws route53 list-hosted-zones --output json`
   *Validate Route 53 hosted zones for DNS DDoS protection*

7. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for DDoS detection and alerting*

8. `aws route53 list-resource-record-sets --hosted-zone-id $(aws route53 list-hosted-zones --query 'HostedZones[0].Id' --output text | cut -d'/' -f3) --max-items 50 --output json || echo '{"ResourceRecordSets": []}'`
   *Check DNS records for email authentication (SPF/DMARC/DKIM)*

9. `aws sesv2 list-email-identities --output json || echo '{"EmailIdentities": []}'`
   *Detect email services to determine spam protection applicability*

## Latest Results

PASS Excellent DDoS and spam protection (86%): PASS Network-layer protection: AWS Shield Standard automatically enabled (all AWS accounts)
- PASS Application-layer protection: 1 Regional WAF Web ACL(s) configured
- PASS Service resilience: 1 Multi-AZ load balancer(s) configured
- INFO No email services detected - spam protection not applicable

---
*Generated 2025-10-01 22:14 UTC*