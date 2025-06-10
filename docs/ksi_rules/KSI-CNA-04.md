# KSI-CNA-04: Use immutable infrastructure patterns

*Generated on 2025-06-10 18:09:59 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-04`
**Description:** Use immutable infrastructure patterns
**Justification:** Validates immutable infrastructure through Terraform-managed resources, versioned AMI pipelines, standardized deployment patterns, and replace-not-modify principles for traditional VM-based workloads
**Last Validation:** ✅ 2025-06-10T18:09:59.497026
**Result:** ⚠️ Minimal infrastructure automation (12%) - predominantly manual: ⚠️ No Terraform lock tables found - potential state management issues; ⚠️ No launch templates found - instances may be deployed inconsistently; ⚠️ No Auto Scaling Groups found - manual instance management; ⚠️ No custom AMIs found - using base images without customization; ✅ Serverless compute: 1 Lambda functions (inherently immutable); ⚠️ No SSM parameters found - configuration may be hardcoded; ⚠️ No CodeBuild projects found - potentially manual deployments

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json`
   **Purpose:** Analyze instance patterns for Terraform-managed immutable deployments (consistent tagging, recent launches)

2. **Command:** `aws ec2 describe-launch-templates --output json`
   **Purpose:** Check launch templates for standardized, versioned instance deployment patterns

3. **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
   **Purpose:** Validate Auto Scaling Groups for instance replacement patterns (immutable scaling)

4. **Command:** `aws ec2 describe-images --owners self --output json`
   **Purpose:** Check custom AMIs for versioned machine image pipeline (immutable base images)

5. **Command:** `aws lambda list-functions --output json`
   **Purpose:** Validate serverless functions (immutable compute even in VM-focused architectures)

6. **Command:** `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)]' --output json`
   **Purpose:** Detect Terraform state management patterns (S3 backend indicates mature IaC)

7. **Command:** `aws dynamodb list-tables --output json`
   **Purpose:** Check for Terraform state locking tables (DynamoDB indicates advanced IaC patterns)

8. **Command:** `aws codebuild list-projects --output json`
   **Purpose:** Check for CI/CD build projects (AMI pipelines, Terraform automation)

9. **Command:** `aws ssm describe-parameters --output json`
   **Purpose:** Validate Systems Manager parameters for configuration management and versioning

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json`
  - **Purpose:** Analyze instance patterns for Terraform-managed immutable deployments (consistent tagging, recent launches)
- **Command:** `aws ec2 describe-launch-templates --output json`
  - **Purpose:** Check launch templates for standardized, versioned instance deployment patterns
- **Command:** `aws autoscaling describe-auto-scaling-groups --output json`
  - **Purpose:** Validate Auto Scaling Groups for instance replacement patterns (immutable scaling)
- **Command:** `aws ec2 describe-images --owners self --output json`
  - **Purpose:** Check custom AMIs for versioned machine image pipeline (immutable base images)
- **Command:** `aws lambda list-functions --output json`
  - **Purpose:** Validate serverless functions (immutable compute even in VM-focused architectures)
- **Command:** `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)]' --output json`
  - **Purpose:** Detect Terraform state management patterns (S3 backend indicates mature IaC)
- **Command:** `aws dynamodb list-tables --output json`
  - **Purpose:** Check for Terraform state locking tables (DynamoDB indicates advanced IaC patterns)
- **Command:** `aws codebuild list-projects --output json`
  - **Purpose:** Check for CI/CD build projects (AMI pipelines, Terraform automation)
- **Command:** `aws ssm describe-parameters --output json`
  - **Purpose:** Validate Systems Manager parameters for configuration management and versioning

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_04`

**Documentation:** Terraform-Focused KSI-CNA-04: Use immutable infrastructure patterns

Validates immutable infrastructure in Terraform-managed, VM-based environments:
- Terraform state management and backend patterns
- Versioned infrastructure (AMIs, launch templates, configuration)
- Replace-not-modify patterns (Auto Scaling Groups, instance replacement)
- Standardized deployments (launch templates, consistent configurations)
- CI/CD automation (build pipelines, automated deployments)
- Configuration management (parameter stores, versioned configs)
- Immutable compute patterns (serverless functions, fresh instances)

### Rule Implementation
```python
def evaluate_KSI_CNA_04(cli_output):
    """
    Terraform-Focused KSI-CNA-04: Use immutable infrastructure patterns
    
    Validates immutable infrastructure in Terraform-managed, VM-based environments:
    - Terraform state management and backend patterns
    - Versioned infrastructure (AMIs, launch templates, configuration)
    - Replace-not-modify patterns (Auto Scaling Groups, instance replacement)
    - Standardized deployments (launch templates, consistent configurations)
    - CI/CD automation (build pipelines, automated deployments)
    - Configuration management (parameter stores, versioned configs)
    - Immutable compute patterns (serverless functions, fresh instances)
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    instances = None
    launch_templates = None
    auto_scaling_groups = None
    custom_amis = None
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use immutable infrastructure patterns

**Implementation Justification:** Validates immutable infrastructure through Terraform-managed resources, versioned AMI pipelines, standardized deployment patterns, and replace-not-modify principles for traditional VM-based workloads

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 9 commands failed execution | ⚠️ No usable output

**Commands Executed:** 9
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*