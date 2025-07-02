# KSI Command Validation Technical Methodology

**Official Technical Reference for FedRAMP 20x Phase One Assessment**

**Document Version**: 2.0  
**Date**: July 2025  
**Authority**: Meridian Knowledge Solutions, LLC  
**Assessment Partner**: Fortreum, LLC (3PAO)  
**FedRAMP Authorization**: Low Impact Level

---

## 📋 **Document Purpose**

This technical methodology document provides the **official justification** for the CLI command approach used in the Meridian Knowledge Solutions FedRAMP 20x assessment. It demonstrates that:

1. **CLI commands are technically valid** and appropriate for each KSI requirement
2. **Command combinations provide comprehensive coverage** of security control objectives
3. **Direct system property validation** offers superior evidence to document-based approaches
4. **Automation methodology aligns** with FedRAMP 20x pilot goals

**Intended Audience**: 3PAO assessors, FedRAMP PMO reviewers, federal agency stakeholders

---

## 🎯 **CLI Validation Methodology**

### **Core Principle: Direct System Property Validation**

Traditional FedRAMP assessments rely on **narrative documentation** describing security controls. The FedRAMP 20x pilot emphasizes **machine-readable validation** of actual system configurations and capabilities.

**CLI Command Approach Benefits**:
- ✅ **Real-time validation** of current system state
- ✅ **Eliminates documentation lag** between implementation and assessment
- ✅ **Provides concrete evidence** of security control effectiveness
- ✅ **Enables continuous monitoring** and automated compliance verification
- ✅ **Reduces assessment time** through automated evidence collection

### **Command Selection Criteria**

Each CLI command was selected based on:
1. **Direct relevance** to the KSI security objective
2. **Technical accuracy** in validating the control implementation
3. **Comprehensive coverage** when combined with other commands
4. **Reliability** in AWS cloud environments
5. **Auditability** through detailed JSON output

---

## 📊 **KSI Command Coverage Matrix**

### **Coverage Level Definitions**

| Coverage Level | Command Count | Technical Validation | Documentation Required |
|---------------|---------------|---------------------|----------------------|
| **High Coverage** | 6-10 commands | 80%+ technical validation | Minimal documentation |
| **Medium Coverage** | 3-5 commands | 50-79% technical validation | Hybrid CLI + documentation |
| **Low Coverage** | 1-2 commands | <50% technical validation | Primary documentation |

### **Coverage Distribution by Category**

| Category | High Coverage KSIs | Medium Coverage KSIs | Low Coverage KSIs | Primary Validation Method |
|----------|-------------------|---------------------|-------------------|---------------------------|
| **Cloud Native Architecture (CNA)** | CNA-01, CNA-03, CNA-06 | CNA-02, CNA-04 | CNA-05, CNA-07 | Multi-command technical validation |
| **Service Configuration (SVC)** | SVC-02, SVC-03, SVC-04, SVC-06 | SVC-01, SVC-05, SVC-07 | - | AWS service configuration analysis |
| **Identity & Access Management (IAM)** | IAM-01, IAM-04, IAM-05, IAM-06 | IAM-02, IAM-03 | - | Federated identity + traditional IAM |
| **Monitoring, Logging & Auditing (MLA)** | MLA-01, MLA-04, MLA-05 | MLA-02, MLA-03 | MLA-06 | CloudTrail + centralized logging |
| **Third-Party Resources (TPR)** | - | TPR-01, TPR-02, TPR-04 | TPR-03 | Hybrid CLI + documentation |
| **Policy & Inventory (PIY)** | - | PIY-01 | PIY-02 through PIY-07 | Hybrid CLI + documentation |
| **Change Management (CMT)** | CMT-02 | CMT-01 | CMT-03, CMT-04, CMT-05 | IaC validation + documentation |
| **Cybersecurity Education (CED)** | - | - | CED-01, CED-02 | Evidence-based validation |
| **Recovery Planning (RPL)** | RPL-03 | RPL-01, RPL-02, RPL-04 | - | Backup systems + documentation |
| **Incident Reporting (INR)** | - | INR-02, INR-03 | INR-01 | Logging systems + documentation |

---

## 🏗️ **High Coverage Examples: Cloud Native Architecture**

### **KSI-CNA-01: Configure ALL information resources to limit inbound and outbound traffic**

**Security Objective**: Comprehensive traffic controls across all AWS resources through multi-layered network security

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-security-groups` | **Instance-level controls**: Validates ingress/egress rules per EC2 instance, including restrictive configurations and least-privilege access | Network Layer 3/4 |
| `aws ec2 describe-network-acls` | **Subnet-level filtering**: Provides defense-in-depth through subnet-wide traffic controls, validates custom rules beyond defaults | Network Layer 3 |
| `aws ec2 describe-route-tables` | **Traffic routing validation**: Ensures controlled egress paths and prevents unintended internet routing from private subnets | Network Routing |
| `aws ec2 describe-nat-gateways` | **Managed egress control**: Validates controlled outbound internet access from private subnets through managed NAT infrastructure | Egress Control |
| `aws ec2 describe-vpc-endpoints` | **Private service access**: Confirms AWS services are accessed privately without internet routing, reducing attack surface | Service Access |
| `aws wafv2 list-web-acls` | **Application-layer protection**: Validates Layer 7 traffic filtering and protection against web-based attacks | Application Layer |
| `aws elbv2 describe-load-balancers` | **Traffic distribution controls**: Confirms proper traffic distribution patterns and public/private load balancer placement | Traffic Management |
| `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs` | **Traffic monitoring**: Validates VPC Flow Logs for traffic visibility and security monitoring capabilities | Monitoring/Visibility |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ All network layers covered (L3-L7)
- ✅ Both ingress and egress validation
- ✅ Defense-in-depth approach
- ✅ Monitoring and visibility included

### **KSI-CNA-03: Use logical networking and related capabilities to enforce traffic flow controls**

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

## 🛡️ **High Coverage Examples: Identity & Access Management**

### **KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication**

**Security Objective**: Automated federated identity validation with upstream MFA enforcement

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws iam list-users` | **Traditional IAM analysis**: Identifies direct IAM users vs federated authentication patterns | User Inventory |
| `aws iam list-mfa-devices` | **MFA device validation**: Documents traditional MFA implementations for service accounts | Device Inventory |
| `aws sso-admin list-instances` | **Identity Center detection**: Validates AWS Identity Center deployment for centralized identity management | Federated Identity |
| `aws identitystore list-users` | **Federated user patterns**: Detects SCIM provisioning and external IdP integration (e.g., Okta user ID patterns) | External Identity |

**Technical Innovation**: **EXCEPTIONAL**
- ✅ **Recognizes modern federated architectures** (SCIM, external IdP)
- ✅ **Automated detection of Okta integration** through user ID patterns
- ✅ **Context-aware assessment** distinguishing service accounts from human users
- ✅ **Upstream MFA enforcement verification** through identity provider integration

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ All authentication paths validated
- ✅ Modern identity architecture recognition
- ✅ Comprehensive federated identity detection

### **KSI-IAM-06: Automatically disable or secure accounts with privileged access in response to suspicious activity**

**Security Objective**: Automated security response for privileged account protection

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws events list-rules` | **Automated response triggers**: Validates EventBridge rules for security response automation | Response Automation |
| `aws guardduty list-detectors` | **Threat detection service**: Confirms GuardDuty for suspicious activity identification | Threat Detection |
| `aws securityhub describe-hub` | **Centralized security coordination**: Validates Security Hub for automated response coordination | Security Orchestration |
| `aws sso-admin list-instances` | **Identity Center automation**: Confirms built-in automated session and access controls | Access Automation |
| `aws lambda list-functions` | **Response function validation**: Identifies automated response functions for account security actions | Response Functions |
| `aws cloudwatch describe-alarms` | **Activity monitoring**: Validates CloudWatch alarms for privileged account activity monitoring | Activity Monitoring |

**Technical Coverage Assessment**: **HIGH COVERAGE**
- ✅ End-to-end automation validation
- ✅ Threat detection integration
- ✅ Response coordination verification

---

## 📊 **Medium Coverage Examples: Service Configuration**

### **KSI-SVC-01: Use current, supported versions of all software**

**Security Objective**: Current software version validation and lifecycle management

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws ec2 describe-images --owners self` | **AMI version tracking**: Validates custom AMI currency and version management practices | Image Currency |
| `aws lambda list-functions` | **Runtime version validation**: Confirms current Lambda runtime versions and supported configurations | Runtime Management |
| `aws rds describe-db-instances` | **Database version tracking**: Validates RDS engine versions and patch levels | Database Currency |
| `aws eks describe-cluster` | **Container orchestration versions**: Confirms EKS cluster versions and supported Kubernetes releases | Container Platforms |
| `aws ssm describe-instance-information` | **System patch status**: Validates Systems Manager agent versions and patch compliance | System Updates |

**Technical Coverage Assessment**: **MEDIUM COVERAGE**
- ✅ Multi-service version validation
- ✅ Automated currency checking
- ⚠️ Requires additional documentation for comprehensive lifecycle management

---

## 🔧 **Low Coverage Examples: Policy & Inventory**

### **KSI-PIY-01: Maintain a comprehensive inventory of information resources**

**Security Objective**: Complete resource inventory and classification

| Command | Technical Justification | Coverage Area |
|---------|------------------------|---------------|
| `aws resourcegroupstaggingapi get-resources` | **Resource discovery**: Automated discovery of tagged AWS resources across services | Resource Discovery |
| `evidence_check` | **Inventory documentation**: Manual verification of comprehensive inventory documentation | Documentation |

**Technical Coverage Assessment**: **LOW COVERAGE**
- ✅ Basic automated resource discovery
- ⚠️ Requires comprehensive manual documentation
- ⚠️ Limited to AWS resources only

---

## 🎯 **Technical Validation Quality Standards**

### **Command Selection Methodology**

#### **High Coverage Validation (6-10 Commands)**
- **Multi-command defense-in-depth**: 6-10 complementary commands per KSI
- **Operational verification**: Both configuration AND runtime status validation
- **Service redundancy**: Multiple validation paths prevent single points of failure
- **Error resilience**: Graceful handling of unavailable AWS services

#### **Medium Coverage Validation (3-5 Commands)**
- **Hybrid validation**: CLI technical validation + manual evidence requirements
- **Core infrastructure validation**: Key services validated through CLI
- **Documentation supplement**: Policy and procedural evidence required

#### **Low Coverage Validation (1-2 Commands)**
- **Evidence-based validation**: Primarily manual documentation requirements
- **Limited CLI enhancement**: Basic technical validation where applicable
- **Process-oriented**: Inherently organizational requirements

### **Validation Approaches by Coverage Level**

| Validation Quality | Command Count | Error Handling | Context Awareness | Technical Focus |
|-------------------|---------------|----------------|-------------------|-----------------|
| **High Coverage** | 6-10 complementary | Multiple fallbacks | Environment-specific | Technical architecture validation |
| **Medium Coverage** | 3-5 related | Robust error handling | Good adaptation | Hybrid technical + procedural |
| **Low Coverage** | 1-2 basic | Basic error handling | Limited adaptation | Process and documentation focus |

---

## 🏗️ **Multi-Command Validation Patterns**

### **Defense-in-Depth Pattern (High Coverage)**

**Example: Network Security Validation**
```python
def validate_network_security():
    # Layer 1: Instance-level controls
    security_groups = aws_ec2_describe_security_groups()
    
    # Layer 2: Subnet-level controls  
    network_acls = aws_ec2_describe_network_acls()
    
    # Layer 3: VPC-level routing
    route_tables = aws_ec2_describe_route_tables()
    
    # Layer 4: Application-level protection
    web_acls = aws_wafv2_list_web_acls()
    
    # Layer 5: Monitoring and visibility
    flow_logs = aws_logs_describe_log_groups()
    
    return aggregate_coverage_assessment(all_layers)
```

### **Service Integration Pattern (Medium Coverage)**

**Example: Backup and Recovery Validation**
```python
def validate_backup_recovery():
    # Primary: Centralized backup service
    backup_plans = aws_backup_list_backup_plans()
    
    # Secondary: Database-specific backups
    rds_backups = aws_rds_describe_db_snapshots()
    
    # Tertiary: Volume-level backups
    ebs_snapshots = aws_ec2_describe_snapshots()
    
    # Documentation: Recovery procedures
    recovery_docs = evidence_check()
    
    return hybrid_coverage_assessment(technical, documentation)
```

### **Discovery Pattern (Low Coverage)**

**Example: Resource Inventory**
```python
def validate_resource_inventory():
    # Automated: AWS resource discovery
    aws_resources = aws_resourcegroupstaggingapi_get_resources()
    
    # Manual: Comprehensive inventory documentation
    inventory_docs = evidence_check()
    
    return documentation_primary_assessment(limited_cli, comprehensive_docs)
```

---

## 🔍 **Error Handling and Robustness**

### **Service Availability Resilience**

**Problem**: AWS services may be unavailable due to configuration, permissions, or subscription requirements.

**CLI Solution Framework**:
```python
def resilient_validation(primary_commands, fallback_commands, documentation):
    try:
        return execute_primary_validation(primary_commands)
    except ServiceUnavailable:
        return execute_fallback_validation(fallback_commands)
    except PermissionDenied:
        return documentation_based_validation(documentation)
    except ConfigurationMissing:
        return provide_setup_guidance()
```

### **Command Failure Handling**

| Failure Type | CLI Response | Coverage Impact | Resolution Path |
|--------------|-------------|-----------------|-----------------|
| **Service Not Configured** | Graceful degradation to alternative commands | Reduced technical coverage | Clear setup guidance |
| **Permission Denied** | Document permission requirements | Alternative validation paths | Permission remediation |
| **Service Unavailable** | Fallback to related services | Maintain validation capability | Service configuration |
| **Invalid Parameters** | Error logging with parameter correction | Technical improvement opportunity | Parameter optimization |

---

## 📚 **Assessment Methodology Standards**

### **Technical Validation Success Factors**

1. **Multi-command defense-in-depth**: Successfully implemented across high-coverage KSIs
2. **Service redundancy**: Multiple validation paths prevent single points of failure
3. **Operational verification**: Both configuration AND runtime status validation
4. **Error resilience**: Graceful handling of unavailable AWS services
5. **Context awareness**: Environment-specific validation logic

### **Coverage Quality Metrics**

| Quality Indicator | High Coverage | Medium Coverage | Low Coverage |
|------------------|---------------|-----------------|--------------|
| **Command Diversity** | 6-10 complementary services | 3-5 related services | 1-2 basic services |
| **Technical Depth** | Configuration + operational | Configuration focus | Basic discovery |
| **Error Handling** | Multiple fallback paths | Some error handling | Limited error handling |
| **Automation Level** | Fully automated assessment | Hybrid assessment | Documentation-primary |

---

## 🎯 **Command Technical Validation Examples**

### **Security Group Analysis Technical Validation**

```json
{
  "command": "aws ec2 describe-security-groups --output json",
  "validation_objective": "Validate ingress/egress traffic controls",
  "technical_properties_validated": [
    "IpPermissions (ingress rules)",
    "IpPermissionsEgress (egress rules)", 
    "Source/destination restrictions",
    "Port/protocol specifications",
    "VPC association and scope"
  ],
  "security_assessment": {
    "restrictive_ingress": "Empty IpPermissions[] = most restrictive",
    "restrictive_egress": "Empty IpPermissionsEgress[] = most restrictive", 
    "least_privilege": "Specific port/protocol combinations vs 0.0.0.0/0:all"
  }
}
```

**Technical Validity Justification**:
- **Direct system query**: Returns actual configured rules, not documentation
- **Real-time accuracy**: Reflects current state, not historical configurations
- **Comprehensive data**: Includes all ingress/egress rules with specific parameters
- **Machine-readable**: JSON output enables automated analysis

### **Federated Identity Detection Technical Validation**

```json
{
  "command": "aws identitystore list-users --output json",
  "validation_objective": "Detect federated identity patterns",
  "technical_properties_validated": [
    "ExternalIds with SCIM issuer",
    "User ID patterns (e.g., Okta 00u... format)",
    "Federated user provisioning evidence", 
    "External IdP integration patterns"
  ],
  "security_assessment": {
    "scim_provisioning": "ExternalIds indicate external IdP provisioning",
    "okta_integration": "User ID format 00u... indicates Okta authentication",
    "upstream_mfa": "External IdP handles MFA enforcement"
  }
}
```

**Technical Validity Justification**:
- **Modern architecture recognition**: Detects cloud-native identity patterns
- **Automated validation**: No manual verification of IdP configurations required
- **Technical accuracy**: SCIM patterns reliably indicate federated authentication
- **Context awareness**: Distinguishes federated from traditional authentication

---

## 📋 **FedRAMP 20x Alignment**

### **Pilot Objectives and CLI Command Alignment**

| Pilot Goal | CLI Command Approach | Technical Benefit |
|------------|---------------------|-------------------|
| **Machine-readable compliance** | JSON output enables automated processing | Eliminates manual interpretation |
| **Reduced narrative documentation** | Direct system validation vs document review | Real-time accuracy |
| **Continuous monitoring** | Real-time command execution | Always-current validation |
| **Automated assessment** | Rule-based validation logic | Consistent, repeatable results |
| **Transparency** | Public dashboard with command visibility | Auditable methodology |

### **Low Impact Level Calibration**

**Technical Approach Alignment**:
- ✅ **Service capability demonstration** over operational maturity requirements
- ✅ **Cost-optimization awareness** for development and pilot environments
- ✅ **Practical implementation focus** vs enterprise-grade operational requirements
- ✅ **Graduated assessment** recognizing partial implementation and incremental improvement

---

## ✅ **Assessor Technical Verification Guidelines**

### **Command Technical Validity Checklist**

- [ ] Each CLI command directly queries relevant AWS service APIs
- [ ] Command outputs provide machine-readable JSON data
- [ ] Commands can be independently executed and verified by assessors
- [ ] Output data directly supports security control validation objectives

### **Coverage Completeness Assessment**
- [ ] Command combinations address all technical aspects of KSI requirement
- [ ] Multi-layer validation provides defense-in-depth assessment where applicable
- [ ] Alternative validation paths exist for service unavailability scenarios
- [ ] Coverage level appropriately matches KSI technical vs procedural nature

### **Automation Effectiveness Validation**
- [ ] Validation logic is deterministic and repeatable
- [ ] Error handling provides graceful degradation with clear guidance
- [ ] Technical thresholds are appropriate for Low Impact level
- [ ] Results provide actionable technical remediation guidance

---

## 📚 **Supporting Documentation References**

### **Primary Technical Documentation**
- **KSI Standard**: June 2025 Key Security Indicators (KSIs)
- **Assessment Methodology**: FedRAMP 20x Phase One Technical Requirements
- **3PAO Validation**: Fortreum, LLC Technical Assessment Methodology

### **Implementation Evidence**
- **Command Register**: `cli_command_register.json` - Complete command mapping and justification
- **Validation Logic**: `cli_assertion_rules_full.py` - Technical rule implementations
- **Evidence Archive**: `evidence_v2/` - Raw CLI outputs organized by KSI

### **Continuous Validation Infrastructure**
- **Public Dashboard**: Real-time technical validation visibility
- **GitHub Actions**: Automated daily validation pipeline
- **Version Control**: Complete audit trail of technical methodology changes

---

**Document Authority**: This technical methodology was developed in coordination with Fortreum, LLC (3PAO) and validated through the official FedRAMP 20x Phase One assessment process. All CLI commands and validation logic have been independently verified by the 3PAO as technically sound and appropriate for their respective KSI requirements.

**Revision Control**: Version 2.0 - July 2025 | Document ID: MKS-KSI-CMD-METHODOLOGY-002
