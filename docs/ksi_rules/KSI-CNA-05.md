# KSI-CNA-05: Have denial of service protection

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-06-24 00:57

**What it validates:** Have denial of service protection

**Why it matters:** Validates comprehensive multi-layer DDoS protection through network-layer shields, application-layer filtering, edge protection, capacity-based mitigation, and automated response capabilities

## Validation Method

1. ``
   *Check AWS Shield Advanced subscription for premium DDoS protection and response team*

2. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Validate WAF for application-layer DDoS protection and rate limiting*

3. `aws wafv2 list-web-acls --scope CLOUDFRONT --output json`
   *Check CloudFront WAF for edge-based application protection*

4. `aws cloudfront list-distributions --output json`
   *Verify CloudFront distributions for edge-based DDoS protection and traffic distribution*

5. `aws elbv2 describe-load-balancers --output json`
   *Check load balancers for traffic distribution and DDoS mitigation capabilities*

6. `aws autoscaling describe-auto-scaling-groups --output json`
   *Validate Auto Scaling Groups for capacity-based DDoS mitigation*

7. `aws route53 list-hosted-zones --output json`
   *Check Route 53 for DNS-layer protection and traffic routing capabilities*

8. `aws cloudwatch describe-alarms --output json`
   *Verify CloudWatch alarms for DDoS detection and automated response*

## Latest Results

WARNING Moderate DDoS protection (50%) - expand coverage: PASS AWS Shield Standard protection (provided by default - automatic network-layer protection)
- PASS Regional application protection: 1 WAF Web ACLs
- WARNING No CloudFront WAF found - missing edge application protection
- WARNING No CloudFront distributions - missing edge-based DDoS protection
- PASS Traffic distribution: 1 load balancers (1 ALB, 0 NLB)
- WARNING No Auto Scaling Groups - missing capacity-based DDoS mitigation
- PASS DNS resilience: 1 Route 53 hosted zones
- WARNING No CloudWatch alarms - missing DDoS detection and response

---
*Generated 2025-06-24 00:57 UTC*