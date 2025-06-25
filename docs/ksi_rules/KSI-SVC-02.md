# KSI-SVC-02: Encrypt or otherwise secure network traffic

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-06-25 22:28

**What it validates:** Encrypt or otherwise secure network traffic

**Why it matters:** Validates comprehensive network traffic encryption from basic service availability to enterprise-grade multi-layer encryption, covering load balancers, CDN, API gateways, databases, caching services, and hybrid connectivity with automated certificate management

## Validation Method

1. `aws elbv2 describe-load-balancers --output json`
   *Check Application and Network Load Balancer configurations for SSL/TLS traffic encryption*

2. `aws ec2 describe-vpc-endpoints --output json`
   *Validate VPC endpoints for private AWS service communication and traffic isolation*

3. `aws elbv2 describe-listeners --output json`
   *Analyze load balancer listeners for HTTPS/TLS protocol enforcement and cipher configuration*

4. `aws cloudfront list-distributions --output json`
   *Check CloudFront CDN distributions for HTTPS enforcement and global traffic encryption*

5. `aws apigateway get-rest-apis --output json`
   *Validate API Gateway configurations for API traffic encryption and secure endpoint access*

6. `aws rds describe-db-instances --output json`
   *Check RDS database instances for SSL/TLS connection encryption and secure data transit*

7. `aws elasticache describe-cache-clusters --output json`
   *Analyze ElastiCache clusters for in-transit encryption and secure cache communication*

8. `aws acm list-certificates --output json`
   *Check AWS Certificate Manager for automated TLS certificate provisioning and management*

9. `aws ec2 describe-vpn-connections --output json`
   *Validate VPN connections for encrypted hybrid cloud connectivity and secure site-to-site communication*

10. `aws organizations describe-organization --output json`
   *Check enterprise-wide encryption policies and organizational traffic security standards across accounts*

## Latest Results

PASS Production-ready multi-layer traffic encryption and certificate management (65%): PASS Load balancer encryption capability: 1 load balancers configured for traffic encryption
- PASS Private service communication: 7 VPC endpoints (4 interface, 1 gateway)
- INFO No load balancer listeners configured
- INFO No CloudFront distributions for global traffic encryption
- PASS API encryption capability: 1 API Gateway endpoints (HTTPS by default)
- PASS Database encryption capability: 1 RDS instances (0 with encrypted storage)
- INFO No ElastiCache clusters for cache encryption
- PASS Automated certificate management: 2/2 active ACM certificates (100% healthy)
- INFO No VPN connections for hybrid connectivity encryption
- PASS Enterprise-wide encryption governance: AWS Organizations enables centralized traffic encryption policies
- PASS Advanced organization features: SCPs for encryption policy enforcement enabled

---
*Generated 2025-06-25 22:28 UTC*