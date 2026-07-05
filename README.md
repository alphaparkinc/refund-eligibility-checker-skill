# refund-eligibility-checker-skill

> **GenPark AI Agent Skill** -- Returns & Refund eligibility rule checker.

## Quick Start

```python
from client import RefundEligibilityClient
client = RefundEligibilityClient()
res = client.check_eligibility("2026-06-01", "2026-06-10", "unopened")
print(res["status"])
```
