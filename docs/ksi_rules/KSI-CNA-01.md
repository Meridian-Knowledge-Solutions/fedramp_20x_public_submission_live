# KSI-CNA-01: Configure ALL information resources to limit inbound and outbound traffic

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-01`
**Description:** Configure ALL information resources to limit inbound and outbound traffic
**Justification:** Validates comprehensive traffic controls across all AWS resources through multi-layered network security including ingress/egress controls, application-layer protection, and traffic monitoring
**Last Validation:** ❌ 2025-06-09T21:56:37.300680
**Result:** ❌ No VPCs found

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-security-groups --output json`
   **Purpose:** Analyze security groups for comprehensive ingress AND egress traffic controls

2. **Command:** `aws ec2 describe-network-acls --output json`
   **Purpose:** Check Network ACLs for subnet-level traffic filtering (defense in depth)

3. **Command:** `aws ec2 describe-route-tables --output json`
   **Purpose:** Validate route tables for controlled traffic routing and egress paths

4. **Command:** `aws ec2 describe-nat-gateways --output json`
   **Purpose:** Check NAT Gateways for controlled egress traffic from private subnets

5. **Command:** `aws ec2 describe-vpc-endpoints --output json`
   **Purpose:** Validate VPC endpoints for private service access (avoiding internet routing)

6. **Command:** `aws wafv2 list-web-acls --scope REGIONAL --output json`
   **Purpose:** Check WAF for application-layer traffic filtering and protection

7. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Analyze load balancers for traffic distribution and access controls

8. **Command:** `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json`
   **Purpose:** Verify VPC Flow Logs for traffic monitoring and visibility

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-security-groups --output json`
  - **Purpose:** Analyze security groups for comprehensive ingress AND egress traffic controls
- **Command:** `aws ec2 describe-network-acls --output json`
  - **Purpose:** Check Network ACLs for subnet-level traffic filtering (defense in depth)
- **Command:** `aws ec2 describe-route-tables --output json`
  - **Purpose:** Validate route tables for controlled traffic routing and egress paths
- **Command:** `aws ec2 describe-nat-gateways --output json`
  - **Purpose:** Check NAT Gateways for controlled egress traffic from private subnets
- **Command:** `aws ec2 describe-vpc-endpoints --output json`
  - **Purpose:** Validate VPC endpoints for private service access (avoiding internet routing)
- **Command:** `aws wafv2 list-web-acls --scope REGIONAL --output json`
  - **Purpose:** Check WAF for application-layer traffic filtering and protection
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Analyze load balancers for traffic distribution and access controls
- **Command:** `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json`
  - **Purpose:** Verify VPC Flow Logs for traffic monitoring and visibility

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_01`

**Documentation:** Simple rule for KSI-CNA-01: Basic traffic controls configured
Expected: Security Groups + VPC

### Rule Implementation
```python
def evaluate_KSI_CNA_01(cli_output):
    """
    Simple rule for KSI-CNA-01: Basic traffic controls configured
    Expected: Security Groups + VPC
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    security_groups = None
    vpcs = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-security-groups" in cli_command:
            security_groups = raw_output.get("SecurityGroups", [])
        elif "describe-vpcs" in cli_command:
            vpcs = raw_output.get("Vpcs", [])
    if not security_groups:
        return False, "❌ No security groups found"
    if not vpcs:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Configure ALL information resources to limit inbound and outbound traffic

**Implementation Justification:** Validates comprehensive traffic controls across all AWS resources through multi-layered network security including ingress/egress controls, application-layer protection, and traffic monitoring

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 8 commands failed execution | ⚠️ No usable output

**Commands Executed:** 8
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*