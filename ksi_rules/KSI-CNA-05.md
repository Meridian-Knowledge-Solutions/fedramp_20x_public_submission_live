# KSI-CNA-05: Use fully qualified domain names and encrypt information in transit

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-10-01 18:40

**What it validates:** Use fully qualified domain names and encrypt information in transit

**Why it matters:** Validates comprehensive encryption in transit from basic TLS to enterprise-grade certificate management, DNS, and email security

## Validation Method

1. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Check WAF configurations for HTTPS enforcement and TLS security*

2. `aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1 --output json`
   *Validate CloudFront WAF rules for global HTTPS enforcement*

3. `aws cloudfront list-distributions --output json`
   *Check CloudFront distributions for TLS configuration and FQDN usage*

4. `aws elbv2 describe-load-balancers --output json`
   *Validate load balancer HTTPS listeners and SSL policies*

5. `aws autoscaling describe-auto-scaling-groups --output json`
   *Check auto-scaling groups for secure configuration and TLS endpoints*

6. `aws route53 list-hosted-zones --output json`
   *Validate Route53 hosted zones for FQDN management and DNS security*

7. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for monitoring TLS and certificate issues*

8. `aws route53 list-resource-record-sets --hosted-zone-id $(aws route53 list-hosted-zones --query 'HostedZones[0].Id' --output text | cut -d'/' -f3) --max-items 50 --output json || echo '{"ResourceRecordSets": []}'`
   *Check DNS records in primary hosted zone for FQDN configurations*

## Latest Results

FAIL Insufficient DDoS and spam protection (43%): PASS Network-layer protection: AWS Shield Standard automatically enabled (all AWS accounts)
- PASS Application-layer protection: 1 Regional WAF Web ACL(s) configured
- PASS Service resilience: 1 Multi-AZ load balancer(s) configured
- WARNING No DNS records retrieved - cannot validate email authentication

---
*Generated 2025-10-01 18:40 UTC*