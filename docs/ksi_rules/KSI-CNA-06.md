# KSI-CNA-06: Design for high availability and recovery

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-06`
**Description:** Design for high availability and recovery
**Justification:** Validates comprehensive high availability through multi-AZ deployments, redundant infrastructure, automated failover, backup strategies, and disaster recovery capabilities across all service layers
**Last Validation:** ✅ 2025-06-09T21:56:37.301538
**Result:** ✅ HA design (excellent): 6 subnets across 6 AZs, 2 backup plans

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-subnets --output json`
   **Purpose:** Analyze subnet distribution across availability zones for network-level HA

2. **Command:** `aws ec2 describe-availability-zones --output json`
   **Purpose:** Check available AZs in region for HA planning and validation

3. **Command:** `aws rds describe-db-instances --output json`
   **Purpose:** Validate RDS Multi-AZ deployments and database high availability

4. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Check load balancers for application-layer HA and traffic distribution

5. **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
   **Purpose:** Validate Auto Scaling Groups for compute resilience and multi-AZ distribution

6. **Command:** `aws backup list-backup-plans --output json`
   **Purpose:** Check backup plans for data protection and recovery capabilities

7. **Command:** `aws ec2 describe-snapshots --owner-ids self --output json`
   **Purpose:** Validate EBS snapshot strategy for storage recovery

8. **Command:** `aws s3api list-buckets --output json`
   **Purpose:** Check S3 buckets for storage redundancy and cross-region replication

9. **Command:** `aws route53 list-hosted-zones --output json`
   **Purpose:** Validate DNS redundancy and health check capabilities

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-subnets --output json`
  - **Purpose:** Analyze subnet distribution across availability zones for network-level HA
- **Command:** `aws ec2 describe-availability-zones --output json`
  - **Purpose:** Check available AZs in region for HA planning and validation
- **Command:** `aws rds describe-db-instances --output json`
  - **Purpose:** Validate RDS Multi-AZ deployments and database high availability
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Check load balancers for application-layer HA and traffic distribution
- **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
  - **Purpose:** Validate Auto Scaling Groups for compute resilience and multi-AZ distribution
- **Command:** `aws backup list-backup-plans --output json`
  - **Purpose:** Check backup plans for data protection and recovery capabilities
- **Command:** `aws ec2 describe-snapshots --owner-ids self --output json`
  - **Purpose:** Validate EBS snapshot strategy for storage recovery
- **Command:** `aws s3api list-buckets --output json`
  - **Purpose:** Check S3 buckets for storage redundancy and cross-region replication
- **Command:** `aws route53 list-hosted-zones --output json`
  - **Purpose:** Validate DNS redundancy and health check capabilities

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_06`

**Documentation:** FINAL FIX: KSI-CNA-06: Basic HA design

ISSUE: Still showing 0 AZ(s), 0 subnets despite evidence showing 6 items + 2 backup plans
ROOT CAUSE: The AWS query format is returning data differently than expected
SOLUTION: Debug the actual response format and handle all variations

### Rule Implementation
```python
def evaluate_KSI_CNA_06(cli_output):
    """
    FINAL FIX: KSI-CNA-06: Basic HA design
    
    ISSUE: Still showing 0 AZ(s), 0 subnets despite evidence showing 6 items + 2 backup plans
    ROOT CAUSE: The AWS query format is returning data differently than expected
    SOLUTION: Debug the actual response format and handle all variations
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    subnets_data = None
    backup_plans = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if not isinstance(raw_output, dict):
            continue
        if "describe-subnets" in cli_command:
            subnets_data = raw_output
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Design for high availability and recovery

**Implementation Justification:** Validates comprehensive high availability through multi-AZ deployments, redundant infrastructure, automated failover, backup strategies, and disaster recovery capabilities across all service layers

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 9 commands failed execution | ⚠️ No usable output

**Commands Executed:** 9
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*