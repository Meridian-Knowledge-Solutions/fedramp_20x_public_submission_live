# KSI-CNA-02: Design systems to minimize the attack surface and minimize lateral movement if compromised

*Generated on 2025-06-10 15:04:05 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-02`
**Description:** Design systems to minimize the attack surface and minimize lateral movement if compromised
**Justification:** Validates comprehensive attack surface reduction through network segmentation, workload isolation, service minimization, and lateral movement prevention across traditional and modern cloud-native architectures
**Last Validation:** ✅ 2025-06-10T15:04:05.261518
**Result:** ⚠️ Minimal isolation controls (15%) - major enhancements required: ⚠️ Default VPC configuration: All 6 subnets are public (standard AWS design); ✅ Excellent AZ segmentation: 6 subnets across 6 availability zones; ⚠️ Default security group usage: Using default security groups only; ✅ Lateral movement barriers: 1/1 security groups with specific rules; ℹ️ No EC2 instances found; ℹ️ No RDS instances found; ℹ️ No load balancers found; ℹ️ No EKS clusters found; ⚠️ Lambda exposure: 1 functions not in VPC (limited network isolation); ⚠️ Using default Network ACLs only (no additional subnet isolation)

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-subnets --output json`
   **Purpose:** Analyze subnet segmentation for attack surface isolation (public vs private)

2. **Command:** `aws ec2 describe-security-groups --output json`
   **Purpose:** Evaluate micro-segmentation and lateral movement prevention through security group rules

3. **Command:** `aws ec2 describe-instances --output json`
   **Purpose:** Assess compute workload exposure and placement for attack surface minimization

4. **Command:** `aws ec2 describe-network-acls --output json`
   **Purpose:** Check Network ACLs for subnet-level isolation and lateral movement barriers

5. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Analyze load balancer exposure patterns (internal vs internet-facing)

6. **Command:** `aws eks describe-cluster --name $(aws eks list-clusters --query 'clusters[0]' --output text) --output json 2>/dev/null || echo '{"cluster":null}'`
   **Purpose:** Check EKS cluster configuration for container workload isolation

7. **Command:** `aws ecs list-clusters --output json`
   **Purpose:** Evaluate ECS container workload segmentation and isolation

8. **Command:** `aws lambda list-functions --output json`
   **Purpose:** Assess Lambda function isolation and VPC configuration for attack surface reduction

9. **Command:** `aws rds describe-db-instances --output json`
   **Purpose:** Check database placement and exposure (should be in private subnets)

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-subnets --output json`
  - **Purpose:** Analyze subnet segmentation for attack surface isolation (public vs private)
- **Command:** `aws ec2 describe-security-groups --output json`
  - **Purpose:** Evaluate micro-segmentation and lateral movement prevention through security group rules
- **Command:** `aws ec2 describe-instances --output json`
  - **Purpose:** Assess compute workload exposure and placement for attack surface minimization
- **Command:** `aws ec2 describe-network-acls --output json`
  - **Purpose:** Check Network ACLs for subnet-level isolation and lateral movement barriers
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Analyze load balancer exposure patterns (internal vs internet-facing)
- **Command:** `aws eks describe-cluster --name $(aws eks list-clusters --query 'clusters[0]' --output text) --output json 2>/dev/null || echo '{"cluster":null}'`
  - **Purpose:** Check EKS cluster configuration for container workload isolation
- **Command:** `aws ecs list-clusters --output json`
  - **Purpose:** Evaluate ECS container workload segmentation and isolation
- **Command:** `aws lambda list-functions --output json`
  - **Purpose:** Assess Lambda function isolation and VPC configuration for attack surface reduction
- **Command:** `aws rds describe-db-instances --output json`
  - **Purpose:** Check database placement and exposure (should be in private subnets)

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_02`

**Documentation:** FIXED KSI-CNA-02: Design systems to minimize the attack surface and minimize lateral movement if compromised

Validates comprehensive attack surface reduction and lateral movement prevention:
- Attack surface minimization (private placement, service exposure, workload isolation)
- Network segmentation (subnets, security groups, NACLs)
- Lateral movement barriers (micro-segmentation, isolation boundaries)
- Modern cloud-native security (containers, serverless, service mesh)
- Defense-in-depth architecture

FIXES APPLIED:
- Removed unfair penalties for default VPC configurations
- No penalty for public subnets in default VPC (AWS standard design)
- No penalty for using default security groups if properly configured
- Maintains comprehensive assessment with fair scoring

### Rule Implementation
```python
def evaluate_KSI_CNA_02(cli_output):
    """
    FIXED KSI-CNA-02: Design systems to minimize the attack surface and minimize lateral movement if compromised
    
    Validates comprehensive attack surface reduction and lateral movement prevention:
    - Attack surface minimization (private placement, service exposure, workload isolation)
    - Network segmentation (subnets, security groups, NACLs)
    - Lateral movement barriers (micro-segmentation, isolation boundaries)
    - Modern cloud-native security (containers, serverless, service mesh)
    - Defense-in-depth architecture
    
    FIXES APPLIED:
    - Removed unfair penalties for default VPC configurations
    - No penalty for public subnets in default VPC (AWS standard design)
    - No penalty for using default security groups if properly configured
    - Maintains comprehensive assessment with fair scoring
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Design systems to minimize the attack surface and minimize lateral movement if compromised

**Implementation Justification:** Validates comprehensive attack surface reduction through network segmentation, workload isolation, service minimization, and lateral movement prevention across traditional and modern cloud-native architectures

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 9 commands failed execution | ⚠️ No usable output

**Commands Executed:** 9
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*