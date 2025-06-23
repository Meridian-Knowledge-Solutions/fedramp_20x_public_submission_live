# KSI-CNA-03: Use logical networking for traffic flow controls

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-06-23 04:26

**What it validates:** Use logical networking for traffic flow controls

**Why it matters:** Validates comprehensive logical networking through software-defined routing, traffic steering, network policies, and modern cloud networking patterns for intentional traffic flow control

## Validation Method

1. `aws ec2 describe-route-tables --output json`
   *Analyze route tables for custom traffic flow controls and logical routing patterns*

2. `aws ec2 describe-network-acls --output json`
   *Evaluate Network ACLs for subnet-level traffic filtering and flow control policies*

3. `aws ec2 describe-vpc-endpoints --output json`
   *Check VPC endpoints for private service routing and traffic flow optimization*

4. `aws ec2 describe-transit-gateways --output json`
   *Validate Transit Gateway for centralized network routing and cross-VPC traffic control*

5. `aws ec2 describe-vpc-peering-connections --output json`
   *Check VPC peering for controlled cross-network communication patterns*

6. `aws elbv2 describe-load-balancers --output json`
   *Analyze load balancers for application-layer traffic distribution and flow control*

7. `aws route53 list-hosted-zones --output json`
   *Check DNS-based traffic routing and resolver controls for logical networking*

8. `aws ec2 describe-nat-gateways --output json`
   *Validate NAT Gateways for controlled egress traffic flow from private networks*

9. `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json`
   *Verify VPC Flow Logs for traffic flow monitoring and control validation*

## Latest Results

PASS Strong logical networking controls (69%): PASS Logical routing infrastructure: 5/5 route tables with intentional traffic flows
- PASS Advanced routing patterns: 1 route tables with custom traffic control
- FAIL No network access control: 1 NACLs found but no rules
- PASS Advanced service routing: 6 VPC endpoints (1 gateway, 3 interface)
- INFO No Transit Gateways found (appropriate for single-VPC environments)
- PASS Application-layer traffic control: 1 Application Load Balancers
- PASS Controlled egress routing: 1 active NAT Gateways
- INFO No VPC Flow Logs found (monitoring not required for basic networking)

---
*Generated 2025-06-23 04:26 UTC*