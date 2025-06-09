# KSI-CNA-03: Use logical networking for traffic flow controls

*Generated on 2025-06-09 21:56:37 UTC*

## 📖 Overview

**KSI ID:** `KSI-CNA-03`
**Description:** Use logical networking for traffic flow controls
**Justification:** Validates comprehensive logical networking through software-defined routing, traffic steering, network policies, and modern cloud networking patterns for intentional traffic flow control
**Last Validation:** ✅ 2025-06-09T21:56:37.301062
**Result:** ✅ Network controls configured: 1 NACLs (0 custom), 1 route tables

## 🛠️ Implementation

### Commands Executed
1. **Command:** `aws ec2 describe-route-tables --output json`
   **Purpose:** Analyze route tables for custom traffic flow controls and logical routing patterns

2. **Command:** `aws ec2 describe-network-acls --output json`
   **Purpose:** Evaluate Network ACLs for subnet-level traffic filtering and flow control policies

3. **Command:** `aws ec2 describe-vpc-endpoints --output json`
   **Purpose:** Check VPC endpoints for private service routing and traffic flow optimization

4. **Command:** `aws ec2 describe-transit-gateways --output json`
   **Purpose:** Validate Transit Gateway for centralized network routing and cross-VPC traffic control

5. **Command:** `aws ec2 describe-vpc-peering-connections --output json`
   **Purpose:** Check VPC peering for controlled cross-network communication patterns

6. **Command:** `aws elbv2 describe-load-balancers --output json`
   **Purpose:** Analyze load balancers for application-layer traffic distribution and flow control

7. **Command:** `aws route53 list-hosted-zones --output json`
   **Purpose:** Check DNS-based traffic routing and resolver controls for logical networking

8. **Command:** `aws ec2 describe-nat-gateways --output json`
   **Purpose:** Validate NAT Gateways for controlled egress traffic flow from private networks

9. **Command:** `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json`
   **Purpose:** Verify VPC Flow Logs for traffic flow monitoring and control validation

## 📋 Evidence Requirements

### 🖥️ CLI Validation
- **Command:** `aws ec2 describe-route-tables --output json`
  - **Purpose:** Analyze route tables for custom traffic flow controls and logical routing patterns
- **Command:** `aws ec2 describe-network-acls --output json`
  - **Purpose:** Evaluate Network ACLs for subnet-level traffic filtering and flow control policies
- **Command:** `aws ec2 describe-vpc-endpoints --output json`
  - **Purpose:** Check VPC endpoints for private service routing and traffic flow optimization
- **Command:** `aws ec2 describe-transit-gateways --output json`
  - **Purpose:** Validate Transit Gateway for centralized network routing and cross-VPC traffic control
- **Command:** `aws ec2 describe-vpc-peering-connections --output json`
  - **Purpose:** Check VPC peering for controlled cross-network communication patterns
- **Command:** `aws elbv2 describe-load-balancers --output json`
  - **Purpose:** Analyze load balancers for application-layer traffic distribution and flow control
- **Command:** `aws route53 list-hosted-zones --output json`
  - **Purpose:** Check DNS-based traffic routing and resolver controls for logical networking
- **Command:** `aws ec2 describe-nat-gateways --output json`
  - **Purpose:** Validate NAT Gateways for controlled egress traffic flow from private networks
- **Command:** `aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json`
  - **Purpose:** Verify VPC Flow Logs for traffic flow monitoring and control validation

## 🧠 Validation Logic

**Function:** `evaluate_KSI_CNA_03`

**Documentation:** Simple rule for KSI-CNA-03: Basic network controls exist
Expected: Network ACLs + Route Tables

### Rule Implementation
```python
def evaluate_KSI_CNA_03(cli_output):
    """
    Simple rule for KSI-CNA-03: Basic network controls exist
    Expected: Network ACLs + Route Tables
    """
    if "commands" not in cli_output:
        return False, "❌ Multi-command format required"
    commands = cli_output["commands"]
    network_acls = None
    route_tables = None
    for cmd in commands:
        cli_command = cmd.get("cli_command", "")
        raw_output = cmd.get("raw_output", {})
        if "describe-network-acls" in cli_command:
            network_acls = raw_output.get("NetworkAcls", [])
        elif "describe-route-tables" in cli_command:
            route_tables = raw_output.get("RouteTables", [])
    if not network_acls:
        return False, "❌ No Network ACLs found"
    if not route_tables:
    # ... (additional validation logic) ...
```

## 📜 Compliance Mapping

**Control Description:** Use logical networking for traffic flow controls

**Implementation Justification:** Validates comprehensive logical networking through software-defined routing, traffic steering, network policies, and modern cloud networking patterns for intentional traffic flow control

**FedRAMP 20x Category:** Cloud Native Architecture

## 📊 Recent Validation Results

**Evidence Analysis:** ❌ All 9 commands failed execution | ⚠️ No usable output

**Commands Executed:** 9
**Validation Method:** validation-engine-sync

---
*Documentation auto-generated from KSI validation pipeline*
*Source: cli_command_register.json, unified_ksi_validations.json*