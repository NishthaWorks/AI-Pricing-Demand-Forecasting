def calculate_business_health(
    stockout_risk,
    overstock_risk,
    predicted_demand,
    competitor_price,
    current_price
):
    """
    Calculate overall business health score.
    """

    score = 100

    # Stockout penalty
    score -= stockout_risk * 0.25

    # Overstock penalty
    score -= overstock_risk * 0.15

    # Demand bonus
    if predicted_demand > 200:
        score += 8
    elif predicted_demand > 150:
        score += 4

    # Pricing opportunity
    if competitor_price > current_price:
        score += 5
    else:
        score -= 3

    score = max(0, min(100, round(score)))

    if score >= 85:
        status = "🟢 Excellent"

    elif score >= 70:
        status = "🟡 Good"

    elif score >= 50:
        status = "🟠 Moderate"

    else:
        status = "🔴 Critical"

    return score, status