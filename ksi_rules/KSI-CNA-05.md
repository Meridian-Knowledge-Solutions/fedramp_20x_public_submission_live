# KSI-CNA-05: Have denial of service protection

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-30 01:03

**What it validates:** Have denial of service protection

**Why it matters:** Validates comprehensive DDoS protection through AWS Shield, CloudFront, WAF, load balancers, and monitoring systems for traffic-based attacks

## Validation Method

1. `aws cloudfront list-distributions --output json`
   *Validate CloudFront distributions for DDoS mitigation and global edge protection*

2. `aws wafv2 list-web-acls --scope CLOUDFRONT --output json`
   *Check CloudFront WAF rules for application-layer DDoS protection*

3. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Validate regional WAF rules for regional DDoS protection*

4. `aws elbv2 describe-load-balancers --output json`
   *Check load balancers for traffic distribution and DDoS mitigation capabilities*

5. `aws autoscaling describe-auto-scaling-groups --output json`
   *Validate Auto Scaling Groups for capacity-based DDoS mitigation*

6. `aws route53 list-hosted-zones --output json`
   *Check Route 53 for DNS-layer protection and traffic routing capabilities*

7. `aws cloudwatch describe-alarms --output json`
   *Verify CloudWatch alarms for DDoS detection and automated response*

## Latest Results

PASS Comprehensive DoS protection established (100%): PASS Network-layer protection: AWS Shield Standard (automatic DDoS protection)
- PASS Application-layer protection: 1 Regional WAF Web ACL(s) - meridian-waf-acl
- PASS Service resilience: 1 multi-AZ load balancer(s) providing traffic distribution
- PASS Internal DNS resilience: 1 private Route 53 hosted zone(s)
- PASS Bonus: DDoS monitoring via 1 relevant CloudWatch alarm(s)

---
*Generated 2025-09-30 01:03 UTC*