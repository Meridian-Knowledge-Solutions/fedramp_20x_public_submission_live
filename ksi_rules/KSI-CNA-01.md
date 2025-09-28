# KSI-CNA-01: Configure ALL information resources to limit inbound and outbound traffic

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-28 03:01

**What it validates:** Configure ALL information resources to limit inbound and outbound traffic

**Why it matters:** Validates comprehensive traffic controls across all AWS resources through multi-layered network security including ingress/egress controls, application-layer protection, and traffic monitoring

## Validation Method

1. `aws ec2 describe-security-groups --output json`
   *Analyze security groups for comprehensive ingress AND egress traffic controls*

2. `aws ec2 describe-network-acls --output json`
   *Check Network ACLs for subnet-level traffic filtering (defense in depth)*

3. `aws ec2 describe-route-tables --output json`
   *Validate route tables for controlled traffic routing and egress paths*

4. `aws ec2 describe-nat-gateways --output json`
   *Check NAT Gateways for controlled egress traffic from private subnets*

5. `aws ec2 describe-vpc-endpoints --output json`
   *Validate VPC endpoints for private service access (avoiding internet routing)*

6. `aws wafv2 list-web-acls --scope REGIONAL --output json`
   *Check WAF for application-layer traffic filtering and protection*

7. `aws elbv2 describe-load-balancers --output json`
   *Analyze load balancers for traffic distribution and control capabilities*

8. `aws logs describe-log-groups --log-group-name-prefix '/aws/vpc/flowlogs' --output json`
   *Check VPC Flow Logs for traffic monitoring and analysis capabilities*

## Latest Results

PASS Comprehensive traffic controls across all resources (97%): PASS VPC infrastructure: 1 VPC(s) detected
- PASS Strong ingress controls: 15/15 security groups restrictive
- PASS Strong egress controls: 15/15 security groups control outbound traffic
- PASS Default security group properly secured
- PASS Custom network controls: 1/1 Network ACLs with custom traffic filtering rules
- PASS Controlled egress routing: 1 private route tables with NAT gateway routing
- PASS Managed egress: 1 NAT gateways for controlled outbound access
- PASS Private service access: 7 VPC endpoints reduce internet-bound traffic
- PASS Application-layer protection: 1 WAF Web ACLs configured
- PASS Traffic distribution: 1 load balancers (1 public, 0 internal)
- PASS Traffic visibility: 1 VPC Flow Log groups for traffic monitoring

---
*Generated 2025-09-28 03:01 UTC*