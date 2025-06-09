# KSI-CNA-04: Use immutable infrastructure patterns

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-04`
**Description:** Use immutable infrastructure patterns
**Justification:** Validates immutable infrastructure through Terraform-managed resources, versioned AMI pipelines, standardized deployment patterns, and replace-not-modify principles for traditional VM-based workloads
**Last Validation:** ❌ 2025-06-09T21:56:37.301195
**Result:** ❌ No Infrastructure as Code patterns found

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

**Documentation:** Simple rule for KSI-CNA-04: Infrastructure as Code patterns
Expected: CloudFormation + Launch Templates

### Rule Implementation
```python
def evaluate_KSI_CNA_04(cli_output):
    """
    Simple rule for KSI-CNA-04: Infrastructure as Code patterns
    Expected: CloudFormation + Launch Templates
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    cloudformation_stacks = None
    launch_templates = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "list-stacks" in cli_command:
            cloudformation_stacks = raw_output.get("StackSummaries", [])
        elif "describe-launch-templates" in cli_command:
            launch_templates = raw_output.get("LaunchTemplates", [])
    active_stacks = len(cloudformation_stacks) if cloudformation_stacks else 0
    templates = len(launch_templates) if launch_templates else 0
    if active_stacks > 0 or templates > 0:
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