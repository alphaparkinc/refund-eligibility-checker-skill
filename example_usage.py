"""
example_usage.py -- Demonstrates RefundEligibilityClient
"""
from client import RefundEligibilityClient

def main():
    client = RefundEligibilityClient()
    result = client.check_eligibility(
        purchase_date="2026-06-01",
        claim_date="2026-06-15",
        item_condition="opened_unused",
        product_category="electronics"
    )
    print("[Refund Eligibility Checker Result]")
    print(f"Status: {result['status'].upper()}")
    print(f"Reason: {result['reason']}")

if __name__ == "__main__":
    main()
