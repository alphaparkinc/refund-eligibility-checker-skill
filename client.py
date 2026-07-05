"""
refund-eligibility-checker-skill: Client SDK
Evaluates return window constraints and item condition policies to approve/deny refunds.
"""
from __future__ import annotations
from datetime import datetime, date


class RefundEligibilityClient:
    """
    SDK for processing return and refund policies.
    """

    def check_eligibility(
        self,
        purchase_date: str,
        claim_date: str,
        item_condition: str,
        product_category: str = "general",
    ) -> dict:
        try:
            p_dt = datetime.fromisoformat(purchase_date).date()
            c_dt = datetime.fromisoformat(claim_date).date()
        except ValueError:
            return {"status": "manual_review", "reason": "Invalid date format parsed."}

        days_elapsed = (c_dt - p_dt).days
        
        # Policy rules
        non_returnable_cats = ["underwear", "swimwear", "perishables", "cosmetics"]
        if product_category.lower() in non_returnable_cats and item_condition != "unopened":
            return {
                "status": "denied",
                "reason": f"Items in the {product_category} category cannot be returned unless unopened."
            }

        if days_elapsed > 30:
            return {
                "status": "denied",
                "reason": f"Returned outside the 30-day window (elapsed: {days_elapsed} days)."
            }

        if item_condition == "damaged":
            return {
                "status": "denied",
                "reason": "Damaged items are ineligible for policy refunds unless reported upon delivery."
            }
        elif item_condition == "opened_used":
            return {
                "status": "manual_review",
                "reason": "Item has been opened and used. Requires support review to approve partial credit."
            }

        return {
            "status": "approved",
            "reason": f"Returned within the 30-day policy window in {item_condition} condition."
        }
