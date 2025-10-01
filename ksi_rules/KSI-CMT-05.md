# KSI-CMT-05: Evaluate the risk and potential impact of any change using a generated deployment manifest

## Overview

**Category:** Change Management
**Status:** FAIL
**Last Check:** 2025-10-01 03:22

**What it validates:** Evaluate the risk and potential impact of any change using a generated deployment manifest

**Why it matters:** Validates impact assessment by querying the final output of successful Step Function executions to confirm an impact manifest was generated.

## Validation Method

1. `aws stepfunctions list-executions --state-machine-arn <YOUR_STATE_MACHINE_ARN> --status-filter SUCCEEDED`
   *Lists recent successful executions of the deployment workflow.*

2. `aws stepfunctions describe-execution --execution-arn <EXECUTION_ARN_PLACEHOLDER>`
   *Retrieves the detailed output of a specific execution. Your 'run_all_cli_commands.py' script will need to run this for each execution found by the first command.*

## Latest Results

- FAIL: No recent successful deployment workflow executions were found.

---
*Generated 2025-10-01 03:22 UTC*