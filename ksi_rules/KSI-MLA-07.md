# KSI-MLA-07: Maintain a list of information resources and event types that will be monitored, logged, and audited

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** FAIL
**Last Check:** 2025-09-20 02:58

**What it validates:** Maintain a list of information resources and event types that will be monitored, logged, and audited

**Why it matters:** Validates comprehensive monitoring inventory management through automated resource discovery, event categorization, audit trail coverage, and documentation maintenance covering log infrastructure, monitoring scope, and automated inventory systems

## Validation Method

1. `aws logs describe-log-groups --output json`
   *Inventory logging resources and analyze event categorization across AWS services*

2. `aws cloudtrail describe-trails --output json`
   *Validate audit trail coverage and event monitoring scope*

3. `aws config describe-configuration-recorders --output json`
   *Check automated discovery and continuous monitoring of information resources*

4. `aws cloudwatch describe-alarms --output json`
   *Validate active monitoring and alerting for tracked resources and events*

5. **Manual Review:** Monitoring inventory documentation, resource lists, and event type categorization

## Latest Results

- FAIL Insufficient automated monitoring inventory (0%): 

---
*Generated 2025-09-20 02:58 UTC*