# KSI-CNA-03: Use logical networking and related capabilities to enforce traffic flow controls

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-22 17:49

**What it validates:** Use logical networking and related capabilities to enforce traffic flow controls

**Why it matters:** Validates logical networking implementation through VPC design, subnet segmentation, routing controls, and network security enforcement

## Validation Method

1. `aws ec2 describe-vpcs --output json`
   *Check VPC configuration for logical network isolation and traffic control foundation*

2. `aws ec2 describe-subnets --output json`
   *Validate subnet design for logical segmentation and traffic isolation*

3. `aws ec2 describe-route-tables --output json`
   *Analyze routing tables for traffic flow control and network segmentation*

4. `aws ec2 describe-internet-gateways --output json`
   *Check internet gateways for controlled external connectivity*

5. `aws ec2 describe-nat-gateways --output json`
   *Validate NAT gateways for controlled outbound traffic from private networks*

6. `aws ec2 describe-vpc-endpoints --output json`
   *Check VPC endpoints for secure service communications without internet transit*

7. `aws directconnect describe-connections --output json`
   *Validate dedicated connections for enterprise traffic flow controls*

8. `aws ec2 describe-transit-gateways --output json`
   *Check transit gateways for inter-VPC and hybrid traffic control*

## Latest Results

PASS Solid logical networking foundation (69%): PASS Logical routing infrastructure: 5/5 route tables with intentional traffic flows
- PASS Advanced routing patterns: 4 route tables with custom traffic control
- FAIL Network ACL information not available
- PASS Advanced service routing: 7 VPC endpoints (1 gateway, 4 interface, 2 GWLB)
- PASS Single-VPC architecture: No Transit Gateways needed (appropriate design)
- PASS Controlled egress routing: 1 active NAT Gateways

---
*Generated 2025-09-22 17:49 UTC*