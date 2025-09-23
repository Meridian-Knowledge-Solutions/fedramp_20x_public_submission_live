# KSI-CNA-03: Use logical networking and related capabilities to enforce traffic flow controls

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-23 07:50

**What it validates:** Use logical networking and related capabilities to enforce traffic flow controls

**Why it matters:** Validates logical networking implementation through VPC design, subnet segmentation, routing controls, and network security enforcement

## Validation Method

1. `aws ec2 describe-route-tables --output json`
   *Analyze routing tables for traffic flow control and network segmentation*

2. `aws ec2 describe-network-acls --output json`
   *ADDED: Analyze Network ACLs for subnet-level traffic control rules.*

3. `aws ec2 describe-vpc-endpoints --output json`
   *Check VPC endpoints for secure service communications without internet transit*

4. `aws ec2 describe-transit-gateways --output json`
   *Check transit gateways for inter-VPC and hybrid traffic control*

5. `aws elbv2 describe-load-balancers --output json`
   *Check load balancers for application and network-layer traffic control.*

6. `aws ec2 describe-nat-gateways --output json`
   *Validate NAT gateways for controlled outbound traffic from private networks*

7. `aws logs describe-log-groups --log-group-name-prefix /aws/vpc-flow-logs --output json`
   *ADDED: Check for VPC Flow Log groups for traffic monitoring.*

## Latest Results

PASS Comprehensive logical networking for traffic flow control (100%): PASS Logical routing infrastructure: 5/5 route tables with intentional traffic flows
- PASS Advanced routing patterns: 4 route tables with custom traffic control
- PASS Advanced network access control: 1/1 NACLs with custom traffic flow policies
- PASS Advanced service routing: 7 VPC endpoints (1 gateway, 4 interface, 2 GWLB)
- PASS Single-VPC architecture: No Transit Gateways needed (appropriate design)
- PASS Application-layer traffic control: 1 Application Load Balancers
- PASS Controlled egress routing: 1 active NAT Gateways
- INFO No VPC Flow Logs found (monitoring enhances but not required for basic networking)

---
*Generated 2025-09-23 07:50 UTC*