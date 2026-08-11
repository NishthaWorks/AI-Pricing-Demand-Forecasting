def pricing_recommendation(
    current_price,
    competitor_price,
    predicted_demand,
    inventory
):
    """
    Generate pricing recommendation based on business rules.
    """

    recommendation = "Keep Current Price"
    reason = "Market conditions are balanced."
    risk = "Medium"

    # High demand + Low inventory
    if predicted_demand > 180 and inventory < 120:
        recommendation = "Increase Price by 8%"
        reason = (
            "Demand is strong while inventory is limited. "
            "A moderate price increase can improve margins."
        )
        risk = "Low"

    # Low demand + High inventory
    elif predicted_demand < 100 and inventory > 250:
        recommendation = "Decrease Price by 10%"
        reason = (
            "Demand is weak and inventory is high. "
            "Reducing price may improve sales velocity."
        )
        risk = "Medium"

    # Competitor significantly cheaper
    elif competitor_price < current_price - 5:
        recommendation = "Review Pricing"
        reason = (
            "Competitor pricing is noticeably lower. "
            "Consider promotions or targeted discounts."
        )
        risk = "High"

    return {
        "recommendation": recommendation,
        "reason": reason,
        "risk": risk
    }