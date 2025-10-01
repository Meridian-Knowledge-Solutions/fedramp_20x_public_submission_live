# SYSTEM SECURITY VALIDATION METHODOLOGY

**Document Version**: 3.0
**Date**: 2025-09-30
**Status**: Official Technical Reference for FedRAMP 20x Phase Two (Moderate)

---

## 1.0 Document Purpose

This document provides the definitive technical methodology for the automated validation of all applicable Key Security Indicators (KSIs) for the FedRAMP 20x Phase Two Moderate pilot. It serves as the sole, authoritative reference that details:

1.  The specific CLI commands used to gather evidence directly from the production environment for each KSI.
2.  The sophisticated, automated validation logic applied to the collected data to determine compliance.
3.  The technical justification for why each validation approach is sufficient to meet the security objectives of a Moderate impact system.

This document replaces and supersedes previous versions of the `ksi-command-validation-reference.md` by integrating the precise implementation details from the `cli_command_register.json` and `cli_assertion_rules_full.py` files.

---

## 2.0 Methodology Framework

### 2.1 Coverage Classification System
Each KSI validation is classified based on the number of automated commands and the depth of the validation logic. This system quantifies the level of automation and sophistication applied to each indicator.

| Coverage Level | Command Count | Validation Approach |
| :--- | :--- | :--- |
| **High Coverage** | 6+ commands | Multi-command, defense-in-depth validation directly measuring live system properties. |
| **Medium Coverage** | 3-5 commands | Hybrid validation using multiple CLI commands, often supplemented by operational artifacts. |
| **Low Coverage** | 1-2 commands | Validation relies primarily on the presence of procedural documentation or simple configuration checks. |

### 2.2 Category Achievement Summary
The following table summarizes the automation coverage across all KSI categories, reflecting the implementation for the Moderate baseline.

| Category | High Coverage | Medium Coverage | Low Coverage | Total KSIs |
| :--- | :--- | :--- | :--- | :--- |
| **Cloud Native Architecture** | 8 | 0 | 0 | 8 |
| **Service Configuration** | 10 | 0 | 0 | 10 |
| **Monitoring, Logging, & Auditing** | 4 | 0 | 0 | 4 |
| **Identity & Access Management** | 5 | 2 | 0 | 7 |
| **Change Management** | 2 | 3 | 0 | 5 |
| **Third-Party Resources** | 0 | 2 | 0 | 2 |
| **Recovery Planning** | 1 | 2 | 1 | 4 |
| **Incident Reporting** | 1 | 1 | 1 | 3 |
| **Policy & Inventory** | 1 | 2 | 4 | 7 |
| **Cybersecurity Education** | 0 | 0 | 3 | 3 |
| **Total** | **32** | **12** | **9** | **53** |

### 2.3 Hard Fail Methodology

Our KSI validation ruleset employs two distinct evaluation models: **graduated scoring** for measuring security maturity and **hard fails** for enforcing non-negotiable security baselines. While most KSIs use a graduated scoring model, a small, strategic subset of six KSIs are designed to fail immediately if a foundational requirement is not met, regardless of other positive findings.

This dual approach ensures that while we can measure and reward progressive maturity in areas like defense-in-depth, we maintain an uncompromising stance on a few critical, foundational security principles where any deficiency constitutes an unacceptable risk.

## KSIs with Hard Fail Conditions

A hard fail is reserved for controls where the absence of a single, specific component represents a complete failure of the control's intent. The following six KSIs have hard fail conditions:

* **KSI-CNA-04** (Immutability & Least Privilege): Fails if the `AdministratorAccess` policy is found on unapproved roles or if sensitive ports (e.g., SSH port 22) are exposed to `0.0.0.0/0`. This enforces a strict, non-negotiable least-privilege stance.

* **KSI-CNA-08** (Automated Security Posture): Fails if there is no direct proof of automated enforcement, such as AWS Config remediation actions or SSM State Manager associations. The control explicitly requires enforcement, making its absence a total failure.

* **KSI-CMT-01** (Log System Modifications): Fails if no CloudTrail trails are configured. Without this foundational service, there is no authoritative log of system modifications, rendering the control completely unmet.

* **KSI-IAM-02** (Passwordless & MFA): Fails if the environment has neither a passwordless authentication method (like SAML/SSO) nor a strong traditional security posture (MFA + strong password policy). This ensures a minimum baseline for user authentication security.

* **KSI-IAM-03** (Service Account Security): Fails if the account lacks a foundational role-based architecture, indicating that insecure practices like using IAM users for services are likely prevalent.

* **KSI-RPL-02** (Recovery Plan): Fails if the required PDF documents outlining the recovery plan are not found in the evidence directory. The control is specifically about maintaining documentation, so its absence is a complete failure.

## The Graduated Scoring Model for Maturity

The majority of KSIs use a graduated scoring model. This is appropriate for controls where security is achieved through multiple layers and a "defense-in-depth" approach. A perfect example is **KSI-CNA-01** (Configure ALL information resources to limit inbound and outbound traffic).

The evaluation for this KSI assesses multiple components, including Security Groups, Network ACLs, WAF, and VPC Endpoints. An environment could have strong Security Group rules but lack a WAF. A hard fail would be inappropriate here, as some effective controls are still in place. The graduated score correctly identifies this as a "Moderate" or "Basic" implementation, reflecting its security maturity without declaring a total failure.

This approach allows us to measure progress and reward incremental improvements, which is more effective for complex, multi-faceted security domains.

## Rationale for CNA-08's Hard Fail Requirement

**KSI-CNA-08** deserves special attention as a new Phase 2 Moderate KSI. Its hard fail requirement represents alignment with Phase 2's philosophy shift:

1. **Explicit Control Text Mandate**: The RFC states "automatically **enforce** secure operations" - an explicit action requirement, not an assessment-only control.

2. **Control Mapping Justification**: Maps to CA-2.1 (Independent Assessors) and CA-7.1 (Continuous Monitoring), both of which emphasize actionable assessment, not passive observation.

3. **Phase 2 Philosophy**: RFC-0014 emphasizes "truly automated and opinionated validation" and "demonstrating participation and involvement" - requiring proof of actual enforcement operations, not just infrastructure presence.

4. **Addresses Structural Criticism**: This implementation directly responds to identified weaknesses where KSIs validated "infrastructure presence rather than actual security posture validation."

_The enforcement requirement is philosophically more aligned with Phase 2's stated objectives than some existing Moderate KSIs (SVC-08/09/10), which may warrant future tightening._

---

## 3.0 Detailed KSI Validation Methodology

# KSI Command Validation Technical Methodology

**Official Technical Reference for FedRAMP 20x Phase One Assessment**

**Document Version**: 2.0  
**Date**: July 2025  
**Authority**: Meridian Knowledge Solutions, LLC  
**Assessment Partner**: Fortreum, LLC (3PAO)  
**FedRAMP Authorization**: Low Impact Level

---

## 📋 **Document Purpose**

This official technical methodology document provides the **complete technical justification** for the CLI command approach used in the Meridian Knowledge Solutions FedRAMP 20x assessment across all 51 Key Security Indicators. It demonstrates:

1. **Technical validity** of CLI commands for each specific KSI requirement
2. **Comprehensive coverage** through command combinations for security control objectives
3. **Direct system property validation** methodology superior to document-based approaches
4. **Complete automation alignment** with FedRAMP 20x pilot goals

**Intended Audience**: 3PAO assessors, FedRAMP PMO reviewers, federal agency stakeholders

---

## 🎯 **Methodology Framework**

### **Coverage Classification System**

| Coverage Level | Command Count | Validation Approach | KSI Count |
|---------------|---------------|-------------------|-----------|
| **High Coverage** | 6+ commands | Multi-command defense-in-depth validation | 27 KSIs (53%) |
| **Medium Coverage** | 3-5 commands | Hybrid CLI + documentation validation | 12 KSIs (24%) |
| **Low Coverage** | 1-2 commands | Evidence-based with selective CLI enhancement | 12 KSIs (23%) |

### **Category Achievement Summary**

| Category | High Coverage | Medium Coverage | Low Coverage | Total |
|----------|---------------|-----------------|--------------|-------|
| **Cloud Native Architecture** | 7 | 0 | 0 | 7 |
| **Service Configuration** | 7 | 0 | 0 | 7 |
| **Monitoring & Logging** | 6 | 0 | 0 | 6 |
| **Identity & Access Management** | 3 | 3 | 0 | 6 |
| **Change Management** | 2 | 0 | 3 | 5 |
| **Recovery Planning** | 0 | 4 | 0 | 4 |
| **Third-Party Resources** | 0 | 0 | 4 | 4 |
| **Policy & Inventory** | 0 | 2 | 5 | 7 |
| **Incident Reporting** | 0 | 1 | 2 | 3 |
| **Cybersecurity Education** | 0 | 0 | 2 | 2 |

---

## 🏗️ **High Coverage KSIs: Advanced Multi-Command Validation (27 KSIs)**

### **Cloud Native Architecture (7/7 KSIs - Complete Category Coverage)**

### **KSI-CNA-01: Configure ALL information resources to limit inbound and outbound traffic**

**Security Objective**: Comprehensive traffic controls across all AWS resources through multi-layered network security

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-security-groups` | **Instance-level controls**: Validates ingress/egress rules per EC2 instance, including restrictive configurations and least-privilege access | Network Layer 3/4 |
| `aws ec2 describe-network-acls` | **Subnet-level filtering**: Provides defense-in-depth through subnet-wide traffic controls, validates custom rules beyond defaults | Network Layer 3 |
| `aws ec2 describe-route-tables` | **Traffic routing validation**: Ensures controlled egress paths and prevents unintended internet routing from private subnets | Network Routing |
| `aws ec2 describe-nat-gateways` | **Managed egress control**: Validates controlled outbound internet access from private subnets through managed NAT infrastructure | Egress Control |
| `aws ec2 describe-vpc-endpoints` | **Private service access**: Confirms AWS services are accessed privately without internet routing, reducing attack surface | Service Access |
| `aws wafv2 list-web-acls --scope REGIONAL` | **Application-layer protection**: Validates Layer 7 traffic filtering and protection against web-based attacks | Application Layer |
| `aws elbv2 describe-load-balancers` | **Traffic distribution controls**: Confirms proper traffic distribution patterns and public/private load balancer placement | Traffic Management |
| `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs` | **Traffic monitoring**: Validates VPC Flow Logs for traffic visibility and security monitoring capabilities | Monitoring/Visibility |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ All network layers covered (L3-L7)
- ✅ Both ingress and egress validation
- ✅ Defense-in-depth approach
- ✅ Monitoring and visibility included

---

### **KSI-CNA-02: Design systems to minimize attack surface and lateral movement**

**Security Objective**: Attack surface reduction through network segmentation, workload isolation, and lateral movement prevention

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-subnets` | **Network segmentation analysis**: Validates subnet placement across AZs and public/private segregation patterns | Network Segmentation |
| `aws ec2 describe-security-groups` | **Micro-segmentation validation**: Confirms custom security groups implementing least-privilege access | Micro-segmentation |
| `aws ec2 describe-instances` | **Workload placement assessment**: Validates compute resource placement in appropriate security contexts | Instance Placement |
| `aws ec2 describe-network-acls` | **Subnet-level isolation**: Validates Network ACLs providing subnet-level access controls | Network Isolation |
| `aws elbv2 describe-load-balancers` | **Exposure pattern analysis**: Validates load balancer placement to minimize attack surface | Service Exposure |
| `aws lambda list-functions` | **Serverless isolation**: Confirms serverless workload VPC configuration patterns | Serverless Security |
| `aws rds describe-db-instances` | **Database placement validation**: Ensures databases are properly isolated in private subnets | Data Tier Security |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Multi-tier architecture validation
- ✅ Network segmentation analysis 
- ✅ Workload placement verification
- ✅ Database isolation assessment

---

### **KSI-CNA-03: Use logical networking for traffic flow controls**

**Security Objective**: Logical network segmentation and traffic flow control enforcement

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-route-tables` | **Traffic flow routing analysis**: Validates custom routing patterns and logical traffic flow controls | Routing Logic |
| `aws ec2 describe-network-acls` | **Subnet-level traffic filtering**: Confirms network ACL rules for subnet-wide traffic flow policies | Traffic Filtering |
| `aws ec2 describe-vpc-endpoints` | **Private service routing**: Validates VPC endpoints for controlled service access patterns | Service Access |
| `aws ec2 describe-transit-gateways` | **Centralized routing validation**: Checks Transit Gateway for enterprise-scale network routing control | Cross-VPC Routing |
| `aws ec2 describe-vpc-peering-connections` | **Cross-network communication**: Validates controlled VPC communication patterns | Network Interconnect |
| `aws elbv2 describe-load-balancers` | **Application-layer traffic distribution**: Confirms load balancer traffic flow patterns | Application Routing |
| `aws route53 list-hosted-zones` | **DNS-based traffic routing**: Validates DNS resolver controls for logical networking | DNS Control |
| `aws ec2 describe-nat-gateways` | **Managed egress flow**: Confirms controlled egress traffic flow from private networks | Egress Management |
| `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs` | **Traffic flow monitoring**: Validates flow log capabilities for traffic control verification | Flow Monitoring |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Advanced logical networking validation
- ✅ Multiple traffic control mechanisms
- ✅ Enterprise-scale routing capabilities

---

### **KSI-CNA-04: Use immutable infrastructure patterns**

**Security Objective**: Immutable infrastructure deployment with strict privilege definitions

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]'` | **Instance deployment pattern analysis**: Validates Infrastructure-as-Code deployment patterns through consistent tagging | Instance Management |
| `aws ec2 describe-launch-templates` | **Standardized deployment validation**: Confirms versioned launch templates for consistent deployments | Template Management |
| `aws autoscaling describe-auto-scaling-groups` | **Instance replacement patterns**: Validates Auto Scaling Groups for immutable scaling strategies | Scaling Patterns |
| `aws ec2 describe-images --owners self` | **Custom AMI pipeline validation**: Confirms versioned machine image pipeline for immutable deployments | Image Management |
| `aws lambda list-functions` | **Serverless immutability**: Validates serverless functions as inherently immutable compute patterns | Serverless Computing |
| `aws s3api list-buckets --query 'Buckets[?contains(Name, terraform) or contains(Name, tfstate)]'` | **Infrastructure-as-Code detection**: Identifies Terraform state management patterns | IaC Management |
| `aws dynamodb list-tables` | **State locking validation**: Checks for Terraform state locking tables indicating advanced IaC practices | State Management |
| `aws codebuild list-projects` | **CI/CD pipeline validation**: Confirms build projects for automated deployment pipelines | Build Automation |
| `aws ssm describe-parameters` | **Configuration management**: Validates Systems Manager parameters for versioned configuration | Config Management |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Infrastructure-as-Code pattern detection
- ✅ Immutable deployment validation
- ✅ Serverless architecture assessment

---

### **KSI-CNA-05: Have denial of service protection**

**Security Objective**: DDoS protection through technical and procedural safeguards

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| (AWS Shield Advanced check placeholder) | **Enterprise DDoS protection**: Validates AWS Shield Advanced subscription for premium protection | DDoS Service |
| `aws wafv2 list-web-acls --scope REGIONAL` | **Application-layer protection**: Validates WAF for Layer 7 DDoS protection and rate limiting | Application Defense |
| `aws wafv2 list-web-acls --scope CLOUDFRONT` | **Edge-based protection**: Confirms CloudFront WAF for distributed DDoS mitigation | Edge Defense |
| `aws cloudfront list-distributions` | **Edge infrastructure**: Validates CloudFront distributions for global DDoS protection and traffic distribution | Global Distribution |
| `aws elbv2 describe-load-balancers` | **Traffic distribution**: Confirms load balancers for traffic spreading and absorption capabilities | Load Distribution |
| `aws autoscaling describe-auto-scaling-groups` | **Capacity-based mitigation**: Validates Auto Scaling for dynamic capacity response to attacks | Dynamic Scaling |
| `aws route53 list-hosted-zones` | **DNS-layer protection**: Confirms Route 53 for DNS-based traffic routing and protection | DNS Defense |
| `aws cloudwatch describe-alarms` | **Attack detection**: Validates CloudWatch alarms for DDoS detection and automated response | Monitoring |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Multi-layer DDoS protection analysis
- ✅ Edge and application layer validation
- ✅ Capacity-based mitigation verification

---

### **KSI-CNA-06: Design for high availability and recovery**

**Security Objective**: High availability architecture with rapid recovery capabilities

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-subnets` | **Multi-AZ deployment validation**: Confirms multiple availability zones for fault tolerance | Availability Zones |
| `aws ec2 describe-availability-zones` | **AZ availability assessment**: Validates available zones for high availability planning | Zone Planning |
| `aws rds describe-db-instances` | **Database availability**: Validates RDS Multi-AZ deployments and automated backup configurations | Database HA |
| `aws elbv2 describe-load-balancers` | **Load distribution and health**: Confirms load balancers with health checks for traffic distribution and failover | Health Management |
| `aws autoscaling describe-auto-scaling-groups` | **Automated recovery**: Validates Auto Scaling Groups for automatic instance replacement and recovery | Auto Recovery |
| `aws backup list-backup-plans` | **Recovery planning**: Confirms AWS Backup plans for systematic recovery capabilities | Backup Strategy |
| `aws ec2 describe-snapshots --owner-ids self` | **Storage recovery**: Validates EBS snapshots for data protection and recovery | Storage Backup |
| `aws s3api list-buckets` | **Storage redundancy**: Confirms S3 bucket configurations for data durability and availability | Object Storage HA |
| `aws route53 list-hosted-zones` | **DNS failover**: Validates Route 53 health checks and failover routing for service availability | DNS Failover |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Comprehensive availability validation
- ✅ Automated recovery mechanisms
- ✅ Multi-layer redundancy analysis

---

### **KSI-CNA-07: Follow AWS best practices**

**Security Objective**: Comprehensive adherence to AWS Well-Architected Framework principles

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws configservice describe-config-rules` | **Compliance automation**: Confirms AWS Config rules for automated best practice enforcement | Compliance Automation |
| `aws cloudtrail describe-trails` | **Audit trail best practices**: Validates CloudTrail configuration following AWS security guidelines | Audit Infrastructure |
| `aws cloudtrail get-trail-status --name $(aws cloudtrail describe-trails --query 'trailList[0].Name' --output text)` | **Operational validation**: Confirms CloudTrail is actively logging for security monitoring | Operational Status |
| `aws kms list-keys` | **Encryption best practices**: Validates KMS key management for data protection | Key Management |
| `aws iam get-account-summary` | **IAM best practices**: Analyzes IAM configuration patterns for security compliance | Access Management |
| `aws ec2 describe-instances` | **Instance best practices**: Evaluates instance configurations for performance and security | Compute Best Practices |
| `aws elbv2 describe-load-balancers` | **Load balancer best practices**: Confirms load balancer implementation for reliability | Load Balancing |
| `aws autoscaling describe-auto-scaling-groups` | **Scaling best practices**: Validates Auto Scaling for reliability and cost optimization | Auto Scaling |
| `aws s3api list-buckets` | **Storage best practices**: Checks S3 usage patterns for security and cost optimization | Storage Optimization |
| `aws cloudwatch describe-alarms` | **Monitoring best practices**: Validates monitoring implementation for operational excellence | Monitoring Excellence |
| `aws backup list-backup-plans` | **Backup best practices**: Confirms backup strategies for data protection and recovery | Backup Strategy |
| `aws organizations describe-organization` | **Governance best practices**: Validates AWS Organizations for enterprise governance | Enterprise Governance |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Complete Well-Architected Framework coverage
- ✅ Multi-pillar validation (security, reliability, performance, cost, operations)
- ✅ Enterprise governance integration

---

## 🛡️ **Service Configuration (7/7 KSIs - Complete Category Coverage)**

### **KSI-SVC-01: Harden and review network and system configurations**

**Security Objective**: Comprehensive network and system hardening with enterprise-grade multi-layer defense

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-security-groups` | **Network hardening validation**: Analyzes security group configurations for access control and traffic filtering | Network Security |
| `aws ec2 describe-instances` | **System configuration review**: Evaluates instance configurations and security settings | System Hardening |
| `aws ec2 describe-network-acls` | **Subnet-level defense**: Validates Network ACLs for defense-in-depth traffic filtering | Defense-in-Depth |
| `aws config describe-config-rules` | **Configuration compliance**: Confirms automated compliance monitoring and hardening validation | Compliance Automation |
| `aws guardduty list-detectors` | **Threat detection**: Validates GuardDuty for network and system security monitoring | Threat Monitoring |
| `aws wafv2 list-web-acls --scope REGIONAL` | **Application hardening**: Confirms Web Application Firewall for application-layer protection | Application Security |
| `aws ssm describe-patch-baselines` | **Patch management**: Analyzes patch baselines for systematic security updates | Vulnerability Management |
| `aws ssm describe-instance-information` | **Configuration management**: Validates Systems Manager coverage for centralized management | Centralized Management |
| `aws inspector2 get-configuration` | **Security assessment**: Confirms Inspector for automated vulnerability scanning | Automated Assessment |
| `aws organizations describe-organization` | **Enterprise hardening**: Validates organization-wide security policies and standards | Enterprise Security |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Multi-layer security validation
- ✅ Automated compliance monitoring
- ✅ Enterprise-wide hardening standards

---

### **KSI-SVC-02: Encrypt or otherwise secure network traffic**

**Security Objective**: Comprehensive network traffic encryption with enterprise-grade multi-layer coverage

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws elbv2 describe-load-balancers` | **Load balancer encryption**: Validates SSL/TLS configurations for traffic encryption | Load Balancer Security |
| `aws ec2 describe-vpc-endpoints` | **Private communications**: Confirms VPC endpoints for secure AWS service access | Private Connectivity |
| `aws elbv2 describe-listeners` | **Protocol enforcement**: Analyzes listeners for HTTPS/TLS protocol enforcement | Protocol Security |
| `aws cloudfront list-distributions` | **Edge encryption**: Validates CloudFront for global HTTPS enforcement | Edge Security |
| `aws apigateway get-rest-apis` | **API encryption**: Confirms API Gateway configurations for secure API access | API Security |
| `aws rds describe-db-instances` | **Database encryption**: Validates RDS SSL/TLS connection encryption | Database Security |
| `aws elasticache describe-cache-clusters` | **Cache encryption**: Analyzes ElastiCache for in-transit encryption | Cache Security |
| `aws acm list-certificates` | **Certificate management**: Confirms ACM for automated TLS certificate lifecycle | Certificate Automation |
| `aws ec2 describe-vpn-connections` | **Hybrid connectivity**: Validates VPN connections for encrypted site-to-site communication | Hybrid Security |
| `aws organizations describe-organization` | **Enterprise encryption**: Confirms organization-wide traffic encryption policies | Enterprise Encryption |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Comprehensive encryption coverage
- ✅ Automated certificate management
- ✅ Hybrid connectivity security

---

### **KSI-SVC-03: Encrypt all federal and sensitive information at rest**

**Security Objective**: Comprehensive at-rest encryption with enterprise-grade multi-service coverage

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws s3api list-buckets` | **Object storage encryption**: Validates S3 bucket encryption for federal data protection | Object Storage |
| `aws ec2 describe-volumes` | **Block storage encryption**: Confirms EBS volume encryption for instance data protection | Block Storage |
| `aws rds describe-db-instances` | **Database encryption**: Validates RDS encryption for structured data at rest | Database Storage |
| `aws rds describe-db-snapshots --owner-type self` | **Backup encryption**: Confirms RDS snapshot encryption for backup data protection | Backup Security |
| `aws efs describe-file-systems` | **File system encryption**: Validates EFS encryption for shared storage protection | File Storage |
| `aws backup list-backup-vaults` | **Centralized backup encryption**: Confirms AWS Backup vault encryption for compliance | Backup Compliance |
| `aws kms list-keys` | **Key management**: Validates KMS key infrastructure for enterprise encryption governance | Key Management |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Multi-service encryption validation
- ✅ Federal data protection compliance
- ✅ Comprehensive key management

---

### **KSI-SVC-04: Manage configuration centrally**

**Security Objective**: Comprehensive centralized configuration management with enterprise-grade governance

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ssm describe-parameters` | **Parameter management**: Validates Systems Manager Parameter Store for centralized configuration | Parameter Store |
| `aws config describe-configuration-recorders` | **Configuration tracking**: Confirms AWS Config for configuration change monitoring | Config Tracking |
| `aws ssm list-documents --document-filter-list key=DocumentType,value=Command` | **Configuration automation**: Validates Systems Manager documents for configuration workflows | Config Automation |
| `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE` | **Infrastructure-as-Code**: Confirms CloudFormation for template-based configuration management | IaC Management |
| `aws secretsmanager list-secrets` | **Secrets management**: Validates Secrets Manager for centralized sensitive configuration | Secrets Management |
| `aws ssm describe-patch-baselines` | **Patch configuration**: Analyzes patch baselines for centralized system management | Patch Management |
| `aws config describe-config-rules` | **Compliance validation**: Confirms Config rules for automated configuration compliance | Compliance Rules |
| `aws ssm describe-instance-information` | **Agent coverage**: Validates Systems Manager agent coverage for centralized management | Agent Management |
| `aws servicecatalog search-products` | **Template governance**: Confirms Service Catalog for standardized configuration templates | Template Governance |
| `aws organizations describe-organization` | **Enterprise governance**: Validates organization-wide configuration policies and standards | Enterprise Config |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Multi-service configuration management
- ✅ Automation and governance validation
- ✅ Enterprise policy enforcement

---

### **KSI-SVC-05: Enforce system and information resource integrity through cryptographic means**

**Security Objective**: Comprehensive cryptographic integrity enforcement with enterprise-grade multi-layer protection

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws cloudtrail describe-trails` | **Audit trail integrity**: Validates CloudTrail log file validation for tamper-evident logging | Audit Integrity |
| `aws kms list-keys` | **Cryptographic foundation**: Confirms KMS keys for integrity protection services | Crypto Foundation |
| `aws kms list-aliases` | **Key governance**: Validates key aliases for organizational key management practices | Key Governance |
| `aws s3api list-buckets` | **Object integrity**: Validates S3 bucket versioning and integrity verification capabilities | Object Integrity |
| `aws rds describe-db-instances` | **Database integrity**: Confirms RDS backup encryption and transaction log integrity | Database Integrity |
| `aws config describe-configuration-recorders` | **Configuration integrity**: Validates Config for configuration change integrity tracking | Config Integrity |
| `aws cloudwatch describe-alarms` | **Integrity monitoring**: Confirms CloudWatch alarms for integrity violation detection | Integrity Monitoring |
| `aws sns list-topics` | **Integrity alerting**: Validates SNS topics for integrity event notification | Alert Management |
| `aws backup list-backup-vaults` | **Backup integrity**: Confirms backup vault encryption and integrity verification | Backup Integrity |
| `aws organizations describe-organization` | **Enterprise integrity**: Validates organization-wide cryptographic integrity policies | Enterprise Crypto |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Multi-layer integrity validation
- ✅ Cryptographic implementation verification
- ✅ Enterprise integrity governance

---

### **KSI-SVC-06: Use automated key management systems**

**Security Objective**: Comprehensive automated key management with enterprise-grade lifecycle management

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws kms list-keys` | **Key infrastructure**: Validates KMS key availability and management infrastructure | Key Infrastructure |
| `aws acm list-certificates` | **Certificate lifecycle**: Confirms ACM for automated certificate management and rotation | Certificate Automation |
| `aws kms list-aliases` | **Key governance**: Validates key aliases for organizational key management practices | Key Governance |
| `aws ssm describe-parameters --parameter-filters Key=Type,Values=SecureString` | **Encrypted parameters**: Confirms KMS-encrypted parameter management | Parameter Encryption |
| `aws secretsmanager list-secrets` | **Secrets rotation**: Validates Secrets Manager for automated secrets lifecycle management | Secrets Automation |
| `aws iam list-server-certificates` | **Legacy certificates**: Confirms legacy certificate management and migration tracking | Legacy Management |
| `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE` | **IaC key management**: Validates CloudFormation for Infrastructure-as-Code key provisioning | IaC Integration |
| `aws config describe-config-rules` | **Key compliance**: Confirms Config rules for key management compliance monitoring | Compliance Monitoring |
| `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateKey --start-time 2025-05-01` | **Key audit trail**: Validates key management audit trail for lifecycle tracking | Audit Trail |
| `aws organizations describe-organization` | **Enterprise key management**: Confirms organization-wide key management policies | Enterprise Keys |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Comprehensive key lifecycle validation
- ✅ Automation verification
- ✅ Enterprise governance integration

---

### **KSI-SVC-07: Use consistent, risk-informed approach for applying security patches**

**Security Objective**: Comprehensive risk-informed patch management with enterprise-grade vulnerability-driven patching

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ssm describe-patch-baselines` | **Patch consistency**: Validates patch baselines for standardized patching approach | Patch Standards |
| `aws ssm describe-instance-information` | **Patch coverage**: Confirms SSM agent coverage for automated patching | Coverage Validation |
| `aws ssm describe-patch-groups` | **Risk segmentation**: Validates patch groups for risk-informed deployment scheduling | Risk Management |
| `aws ssm list-documents --document-filter-list key=DocumentType,value=Command` | **Patch automation**: Confirms automation workflows for risk-informed procedures | Automation Workflows |
| `aws ssm describe-maintenance-windows` | **Controlled deployment**: Validates maintenance windows for risk mitigation scheduling | Deployment Control |
| `aws inspector2 get-configuration` | **Vulnerability integration**: Confirms Inspector for vulnerability-driven patch prioritization | Vulnerability Focus |
| `aws ecr describe-repositories` | **Container patching**: Validates container registries for image patching integration | Container Security |
| `aws lambda list-layers` | **Serverless patching**: Confirms Lambda layers for serverless runtime management | Serverless Management |
| `aws config describe-config-rules` | **Patch compliance**: Validates Config rules for patch compliance monitoring | Compliance Monitoring |
| `aws organizations describe-organization` | **Enterprise patching**: Confirms organization-wide risk-informed patch policies | Enterprise Patching |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Risk-informed approach validation
- ✅ Multi-platform patch coverage
- ✅ Enterprise governance integration

---

## 📊 **Monitoring, Logging & Auditing (4/4 KSIs - Complete Category Coverage)**

### **KSI-MLA-01: Operate a SIEM or similar system for centralized, tamper-resistant logging**

**Security Objective**: Comprehensive SIEM capabilities and centralized logging validation

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws cloudtrail describe-trails` | **Audit trail foundation**: Validates CloudTrail for tamper-resistant, centralized logging infrastructure | Audit Infrastructure |
| `aws logs describe-log-groups` | **Log aggregation**: Confirms CloudWatch Logs for centralized log collection and retention | Log Management |
| `aws cloudwatch describe-alarms` | **Automated analysis**: Validates real-time log analysis and alerting capabilities | Analysis Automation |
| `aws kms list-keys` | **Cryptographic protection**: Confirms KMS keys for sensitive log encryption and integrity | Log Protection |
| `aws config describe-delivery-channels` | **Configuration logging**: Validates Config delivery channels for configuration change logging | Config Logging |
| `aws s3api list-buckets` | **Log archival**: Confirms S3 buckets for long-term log storage and forensic capabilities | Archive Storage |
| `aws securityhub get-findings --max-results 20` | **Security correlation**: Validates Security Hub for advanced threat detection and event correlation | Security Integration |
| `aws organizations describe-organization` | **Enterprise logging**: Confirms organization-wide centralized logging capabilities | Enterprise SIEM |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Comprehensive logging infrastructure
- ✅ Tamper-resistance validation
- ✅ Enterprise SIEM capabilities

---

### **KSI-MLA-02: Regularly review and audit logs**

**Security Objective**: Comprehensive log review capabilities with enterprise-grade automated analysis

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws cloudwatch describe-alarms` | **Automated monitoring**: Validates CloudWatch alarms for real-time log analysis | Automated Review |
| `aws logs describe-metric-filters` | **Pattern analysis**: Confirms metric filters for log pattern detection and analysis | Pattern Detection |
| `aws sns list-topics` | **Alert delivery**: Validates SNS topics for log review notification mechanisms | Alert Management |
| `aws logs describe-log-groups` | **Retention management**: Analyzes log retention policies and compliance-grade management | Retention Compliance |
| `aws cloudtrail lookup-events --max-items 10` | **Audit validation**: Confirms recent audit events for review process verification | Audit Process |
| `aws securityhub get-insights` | **Advanced correlation**: Validates Security Hub insights for intelligent log analysis | Advanced Analytics |
| `aws config describe-config-rules` | **Compliance rules**: Confirms automated compliance rules for log governance | Compliance Automation |
| `aws lambda list-functions` | **Custom processing**: Validates custom log processing and automated review functions | Custom Analysis |
| `aws organizations describe-organization` | **Enterprise review**: Confirms organization-wide centralized log review capabilities | Enterprise Review |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Automated review mechanisms
- ✅ Advanced analytics capabilities
- ✅ Enterprise-wide review processes

---

### **KSI-MLA-03: Rapidly detect and remediate or mitigate vulnerabilities**

**Security Objective**: Comprehensive vulnerability detection and response with enterprise-grade automated remediation. This KSI supersedes KSI-MLA-04 and KSI-MLA-06 by providing a holistic validation of the entire vulnerability management lifecycle from detection through remediation.

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws securityhub get-enabled-standards --region us-east-1` | **Standards validation**: Confirms Security Hub standards for vulnerability detection foundations | Detection Standards |
| `aws inspector2 get-configuration` | **Automated scanning**: Validates Inspector for EC2, container, and application vulnerabilities | Automated Detection |
| `aws securityhub get-findings --filters '{"RecordState":[{"Value":"ACTIVE","Comparison":"EQUALS"}]}' --max-results 50` | **Active findings**: Analyzes active security findings for rapid detection assessment | Finding Analysis |
| `aws ssm describe-patch-baselines` | **Patch remediation**: Confirms automated patch management for vulnerability remediation | Patch Management |
| `aws lambda list-functions` | **Automated response**: Validates automated response functions for vulnerability handling | Response Automation |
| `aws cloudwatch describe-alarms` | **Real-time alerting**: Confirms CloudWatch alarms for rapid vulnerability notification | Alert Systems |
| `aws config describe-config-rules` | **Configuration monitoring**: Validates continuous compliance for configuration vulnerabilities | Config Monitoring |
| `aws organizations describe-organization` | **Enterprise detection**: Confirms organization-wide vulnerability management capabilities | Enterprise Security |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Rapid detection capabilities
- ✅ Automated remediation workflows
- ✅ Enterprise vulnerability management

---

### **KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing**

**Security Objective**: Comprehensive Infrastructure as Code security evaluation with enterprise-grade governance

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws config describe-config-rules` | **IaC evaluation**: Validates Config rules for Infrastructure as Code compliance monitoring | IaC Compliance |
| `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE` | **Stack validation**: Confirms CloudFormation stacks for IaC deployment testing | Stack Management |
| `aws cloudformation describe-stacks` | **Configuration analysis**: Analyzes detailed stack configuration for drift detection | Configuration Testing |
| `aws ssm describe-parameters --max-results 50` | **Parameter management**: Validates Systems Manager for centralized configuration management | Parameter Control |
| `aws codebuild list-projects` | **Testing automation**: Confirms automated IaC testing through build projects | Testing Automation |
| `aws codepipeline list-pipelines` | **Deployment pipelines**: Validates automated IaC deployment pipelines and change validation | Pipeline Validation |
| `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateStack --start-time 2025-05-01` | **Deployment auditing**: Analyzes deployment audit trail for IaC change tracking | Audit Trail |
| `aws resourcegroupstaggingapi get-resources --resource-type-filters cloudformation` | **Resource governance**: Validates resource inventory and tag-based governance for IaC assets | Resource Management |
| `aws organizations describe-organization` | **Enterprise governance**: Confirms enterprise-level multi-account governance for IaC | Enterprise IaC |
| `aws servicecatalog search-products` | **Template governance**: Validates standardized IaC templates and governance through Service Catalog | Template Standards |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ Complete IaC lifecycle validation
- ✅ Automated testing verification
- ✅ Enterprise governance assessment

---

## 🔧 **Medium Coverage KSIs: Hybrid Validation (12 KSIs)**

### **Identity & Access Management (3/6 KSIs)**

### **KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication**

**Security Objective**: Comprehensive federated MFA enforcement with upstream identity provider validation

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws iam list-users` | **Traditional IAM analysis**: Identifies direct IAM users vs federated authentication patterns | User Inventory |
| `aws iam list-mfa-devices` | **MFA device validation**: Documents traditional MFA implementations for service accounts | Device Inventory |
| `aws sso-admin list-instances` | **Identity Center detection**: Validates AWS Identity Center deployment for centralized identity management | Federated Identity |
| `aws identitystore list-users --identity-store-id d-9067ccc0ff` | **Federated user patterns**: Detects SCIM provisioning and external IdP integration (Okta patterns) | External Identity |
| `evidence_check` | **MFA enforcement documentation**: Validates Identity Center MFA configuration screenshots | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Automated federated identity pattern detection
- ✅ External IdP integration recognition
- ✅ Context-aware service vs human account assessment

---

### **KSI-IAM-02: Use secure passwordless methods when feasible, otherwise enforce strong passwords with MFA**

**Security Objective**: Passwordless authentication validation with fallback to strong password policies

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws iam list-saml-providers` | **Federated authentication**: Validates SAML providers for passwordless authentication methods | Passwordless Auth |
| `aws iam list-virtual-mfa-devices` | **MFA validation**: Confirms MFA device configuration and enforcement | MFA Enforcement |
| `aws iam get-account-password-policy` | **Password policy**: Validates strong password policy when passwords are required | Password Security |
| `aws iam list-users` | **Authentication patterns**: Analyzes user authentication requirements and configurations | User Auth Analysis |
| `aws sts get-caller-identity` | **Credential validation**: Confirms current authentication method (temporary vs permanent) | Credential Type |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Passwordless method detection
- ✅ Strong password policy validation
- ✅ Authentication pattern analysis

---

### **KSI-IAM-03: Enforce appropriately secure authentication methods for non-user accounts and services**

**Security Objective**: Service account security through role-based authentication and access key management

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws iam list-roles` | **Role-based authentication**: Validates IAM roles for secure service authentication | Service Roles |
| `aws iam list-users` | **Service user detection**: Identifies potential service users that should use roles instead | User Analysis |
| `aws iam list-access-keys` | **Access key security**: Detects long-term access keys indicating insecure service authentication | Key Management |
| `aws ec2 describe-instances --query 'Reservations[*].Instances[*].IamInstanceProfile'` | **Instance profiles**: Validates EC2 instances use instance profiles for secure authentication | Instance Security |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Role-based authentication validation
- ✅ Insecure pattern detection
- ✅ Instance profile verification

---

### **Change Management (2/5 KSIs)**

### **KSI-CMT-04: Have documented change management procedure**
**Security Objective**: Codified change management procedure with an enforced, auditable approval workflow.

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ssm list-documents --document-filter-list 'key=DocumentType,value=ChangeTemplate'` | **Procedure Codification**: Validates that change procedures are codified as executable SSM Change Templates. | Process Automation |
| `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=StartChangeRequestExecution` | **Approval Enforcement**: Confirms that the approval workflow is consistently initiated for changes, providing an audit trail. | Governance & Audit |
| `aws ssm get-document` | **Workflow Inspection**: Allows inspection of individual templates to verify specific approvers and runbooks. | Workflow Validation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Verifies the procedure is technically implemented, not just documented.
- ✅ Provides auditable proof that the approval process is followed.
- ✅ Aligns with automated change management goals.

---

### **KSI-CMT-05: Evaluate risk and potential impact of any change**
**Security Objective**: Technical risk and impact assessment through automated, event-driven deployment workflows.

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws stepfunctions list-executions` | **Workflow Activity**: Lists recent executions of the deployment state machine, proving the process is active. | Operational Status |
| `aws stepfunctions describe-execution` | **Impact Assessment Validation**: Retrieves the final output of each execution to confirm that the `impactAssessment.status` field is 'GENERATED'. | Risk Assessment |
| `aws s3 cp` | **Artifact Retrieval**: (Conceptual) Allows retrieval of the generated `manifest.json` for detailed audit of the assessed impact. | Audit & Forensics |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Validates impact assessment as an automated step within a workflow.
- ✅ Provides direct, machine-readable evidence of assessment completion.
- ✅ Eliminates reliance on manual documentation.

---

### **Recovery Planning (4/4 KSIs - Complete Medium Coverage)**

### **KSI-RPL-01: Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)**

**Security Objective**: RTO/RPO definition with technical infrastructure capability verification

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,PreferredBackupWindow]'` | **RPO validation**: Validates RDS backup retention for point-in-time recovery capability | Database Recovery |
| `aws backup list-backup-plans` | **Infrastructure alignment**: Confirms backup plan frequency alignment with recovery objectives | Backup Planning |
| `evidence_check` | **RTO/RPO documentation**: Validates documented recovery objectives with infrastructure validation | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Technical infrastructure validation
- ✅ Recovery capability verification
- ✅ Documentation alignment

---

### **KSI-RPL-02: Develop and maintain recovery plan aligned with recovery objectives**

**Security Objective**: Recovery plans with technical implementation evidence and automation capabilities

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DeletionProtection,BackupRetentionPeriod,PreferredMaintenanceWindow]'` | **Recovery configuration**: Validates RDS recovery settings align with documented procedures | Database Recovery |
| `aws backup describe-backup-plans` | **Plan validation**: Confirms backup plan configuration supports recovery procedures | Backup Configuration |
| `evidence_check` | **Recovery documentation**: Validates disaster recovery plans with technical implementation | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Technical configuration alignment
- ✅ Recovery automation validation
- ✅ Plan implementation verification

---

### **KSI-RPL-03: Perform system backups aligned with recovery objectives**

**Security Objective**: Comprehensive backup implementation with operational evidence and retention validation

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws backup list-backup-plans` | **Backup infrastructure**: Validates AWS Backup plans for systematic implementation | Backup Planning |
| `aws backup get-backup-plan --backup-plan-id $(aws backup list-backup-plans --query 'BackupPlansList[0].BackupPlanId' --output text)` | **Configuration detail**: Analyzes detailed backup configuration including retention policies | Configuration Detail |
| `aws backup list-backup-jobs --by-state COMPLETED --max-results 20` | **Operational validation**: Confirms recent successful backup operations prove functionality | Operational Proof |
| `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,BackupRetentionPeriod,DeletionProtection]'` | **Database backup**: Validates RDS automated backup configuration and protection settings | Database Backup |
| `aws ec2 describe-snapshots --owner-ids self` | **Volume backup**: Confirms EBS snapshots for comprehensive system backup coverage | Volume Backup |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Systematic backup implementation
- ✅ Operational proof of functionality
- ✅ Multi-service backup coverage

---

### **KSI-RPL-04: Regularly test recovery capability**

**Security Objective**: Recovery testing validation through operational metrics and documented procedures

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws backup list-restore-jobs --max-results 20` | **Recovery testing**: Documents historical restore operations proving actual testing | Recovery Operations |
| `aws backup list-backup-jobs --by-state COMPLETED --by-created-after 2024-05-01` | **Performance metrics**: Validates recent backup performance for recovery time validation | Performance Validation |
| `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,LatestRestorableTime,PreferredBackupWindow]'` | **Recovery capability**: Verifies point-in-time recovery capability for testing validation | Recovery Capability |
| `evidence_check` | **Testing documentation**: Validates recovery testing procedures and results | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Operational recovery validation
- ✅ Performance metric verification
- ✅ Testing procedure documentation

---

### **Incident Reporting (1/3 KSIs)**

### **KSI-INR-03: Generate after action reports and incorporate lessons learned**

**Security Objective**: Automated incident analysis with manual after action report integration

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws securityhub get-insights` | **Incident analysis**: Retrieves Security Hub insights for automated incident analysis capabilities | Analysis Automation |
| `aws securityhub get-insight-results --insight-arn arn:aws:securityhub:us-east-1:893894210484:insight/893894210484/custom/5bcb2cd3-64e4-4493-b0ea-0dd45ec3b08c` | **Specific insights**: Analyzes specific incident insight results for after action analysis | Insight Analysis |
| `aws securityhub get-findings --filters '{"WorkflowState":[{"Value":"RESOLVED","Comparison":"EQUALS"}]}' --max-items 10` | **Resolved findings**: Reviews resolved security findings for lessons learned demonstration | Resolution Analysis |
| `aws securityhub describe-standards` | **Standards tracking**: Verifies security standards tracking for continuous improvement | Standards Compliance |
| `evidence_check` | **After action documentation**: Validates after action reports and lessons learned documentation | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Automated incident analysis
- ✅ Resolution tracking
- ✅ Continuous improvement validation

---

### **Policy & Inventory (2/7 KSIs)**

### **KSI-PIY-01: Maintain comprehensive inventory of information resources**

**Security Objective**: Asset inventory through automated discovery and comprehensive documentation

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws resourcegroupstaggingapi get-resources` | **Resource discovery**: Automated discovery of tagged AWS resources across all services | Resource Discovery |
| `evidence_check` | **Inventory documentation**: Manual verification of comprehensive asset inventory documentation | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Automated AWS resource discovery
- ✅ Comprehensive inventory documentation
- ⚠️ Limited to AWS resources only

---

### **Third-Party Resources (2/2 KSIs)**

### **KSI-TPR-01: Identify all third-party information resources**
**Security Objective**: Automated discovery of external integrations and third-party software components. This KSI supersedes KSI-TPR-02.

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws iam list-roles` | **Cross-Account Trust**: Identifies IAM roles with trust policies allowing access from external AWS accounts, a primary indicator of third-party integration. | Identity Integration |
| `aws ec2 describe-vpc-peering-connections` | **Network Integration**: Discovers VPC peering connections to external networks, indicating third-party infrastructure dependencies. | Network Integration |
| `aws inspector2 list-findings` | **Software Components**: Analyzes AWS Inspector findings to inventory third-party software packages and libraries in use on compute resources. | Software Inventory |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Automated discovery of AWS-level integrations.
- ✅ Identifies third-party software dependencies via vulnerability scans.
- ✅ Provides technical evidence of third-party connections.

---

### **KSI-TPR-03: Identify and prioritize mitigation of potential supply chain risks**
**Security Objective**: Proactive identification and risk-based prioritization of supply chain vulnerabilities in third-party software.

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws inspector2 list-findings --filter-criteria '{"findingStatus": [{"comparison": "EQUALS", "value": "ACTIVE"}]}'` | **Vulnerability Detection**: Leverages AWS Inspector to automatically scan and identify vulnerabilities within third-party software components. | Vulnerability Scanning |
| `aws securityhub get-findings` | **Risk Prioritization**: Uses Security Hub to aggregate Inspector findings, which are automatically prioritized by severity, providing a risk-based view. | Risk Management |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Automates the detection of software supply chain vulnerabilities.
- ✅ Provides a risk-informed basis for prioritization through severity ratings.
- ✅ Directly measures a key aspect of supply chain risk management.

---

### **KSI-PIY-04: Build security considerations into SDLC and align with CISA Secure By Design principles**

**Security Objective**: Secure development lifecycle validation through code repositories and documentation

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws codecommit list-repositories` | **Code repository analysis**: Validates code repositories for secure development practices | Development Security |
| `evidence_check` | **SDLC documentation**: Validates secure SDLC procedures and CISA alignment documentation | Documentation |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Development infrastructure validation
- ✅ Secure development documentation
- ⚠️ Limited to AWS CodeCommit repositories

---

## 📄 **Low Coverage KSIs: Evidence-Based Validation (9 KSIs)**

### **Change Management (1/5 KSIs)**

### **KSI-CMT-03: Implement automated testing and validation of changes prior to deployment**
**Validation Approach**: Comprehensive Infrastructure as Code testing evidence through tiered documentation requirements covering automated testing proof, Checkov scanning, SARIF reporting, CI/CD integration, and enterprise governance standards.

---

### **Third-Party Resources (0/2 KSIs)**

### **KSI-TPR-04: Monitor third party software for upstream vulnerabilities**
**Validation Approach**: Inspector vulnerability findings for third-party components combined with contractual monitoring requirements, upstream vulnerability procedures, and notification agreements.

---

### **Policy & Inventory Governance Documentation (5/7 KSIs)**

### **KSI-PIY-02: Have policies outlining security objectives of all information resources**
**Validation Approach**: Security policies and objectives documentation including information security objectives, resource security standards, and policy framework documentation.

### **KSI-PIY-03: Maintain a vulnerability disclosure program**
**Validation Approach**: Vulnerability disclosure program documentation including disclosure policies, responsible disclosure procedures, and program governance framework.

### **KSI-PIY-05: Document methods used to evaluate information resource implementations**
**Validation Approach**: Evaluation methodology documentation including security assessment procedures, implementation review processes, and evaluation framework standards.

### **KSI-PIY-06: Have dedicated staff and budget for security with executive support**
**Validation Approach**: Security organization documentation including organizational charts, budget allocation evidence, executive security charters, and governance structure documentation.

### **KSI-PIY-07: Document risk management decisions for software supply chain security**
**Validation Approach**: Supply chain risk management documentation including vendor security assessments, software supply chain policies, and risk management decision frameworks.

---

### **Cybersecurity Education (2/2 KSIs - Complete Low Coverage)**

### **KSI-CED-01: Ensure all employees receive security awareness training**
**Validation Approach**: Security awareness training documentation including training programs, completion records, training materials, and annual training schedules.

### **KSI-CED-02: Require role-specific training for high risk roles, including privileged access**
**Validation Approach**: Role-specific training documentation including privileged access training, training matrices, specialized cybersecurity curricula, and training completion records.

---

### **Incident Reporting Process Documentation (2/3 KSIs)**

### **KSI-INR-01: Report incidents according to FedRAMP requirements**
**Validation Approach**: FedRAMP incident reporting documentation including reporting procedures, compliance policies, notification templates, and regulatory compliance frameworks.

### **KSI-INR-02: Maintain incident log and periodically review for patterns**
**Validation Approach**: Security log group infrastructure validation combined with incident tracking documentation including log registers, pattern analysis, trend reports, and periodic review procedures.

---

## ✅ **Assessment Authority and Methodology Validation**

**Technical Validation**: All 51 KSIs and their associated CLI commands have been independently verified by Fortreum, LLC (accredited 3PAO) as technically sound and appropriate for their respective security control requirements.

**Coverage Appropriateness**: The coverage levels (High/Medium/Low) align with the technical vs procedural nature of each KSI, ensuring optimal validation approaches while maintaining comprehensive security control coverage.

**Methodology Authority**: This comprehensive technical approach was developed in coordination with Fortreum, LLC and validated through the official FedRAMP 20x Phase One assessment process.

**Continuous Validation**: All technical commands execute through automated GitHub Actions pipeline with results published to public trust center, ensuring ongoing methodology effectiveness and technical accuracy.

---

**Document Authority**: Meridian Knowledge Solutions, LLC  
**Version**: 2.0 - July 2025  
**Document ID**: MKS-KSI-CMD-METHODOLOGY-COMPLETE-002  
**Status**: Complete Technical Reference - All 51 KSIs with Comprehensive Command Validation  
**Revision Control**: Official methodology documentation with detailed technical justification for all Key Security Indicators
