def generate_executive_summary(
    predicted_demand,
    stockout_risk,
    overstock_risk,
    current_price,
    competitor_price
):
    """
    Generate executive business recommendations
    using demand, inventory and pricing signals.
    """

    recommendations = []

    # -------------------------
    # Demand Analysis
    # -------------------------

    if predicted_demand > 180:

        recommendations.append(
            "📈 Demand is expected to remain strong over the next business cycle."
        )

    elif predicted_demand < 100:

        recommendations.append(
            "📉 Demand is relatively weak. Consider reviewing promotions and pricing."
        )

    else:

        recommendations.append(
            "📊 Demand is currently moderate. Continue monitoring future sales trends."
        )

    # -------------------------
    # Inventory Analysis
    # -------------------------

    if stockout_risk > 70:

        recommendations.append(
            "🚨 Inventory levels are critically low. "
            "Immediate replenishment is recommended."
        )

    elif stockout_risk > 40:

        recommendations.append(
            "⚠️ Stockout risk is elevated. "
            "Consider increasing inventory before demand peaks."
        )

    if overstock_risk > 50:

        recommendations.append(
            "📦 Inventory exceeds expected demand. "
            "Consider slowing future purchasing."
        )

    elif overstock_risk > 25:

        recommendations.append(
            "⚠️ Overstock risk is increasing. "
            "Review purchasing quantities carefully."
        )

    if stockout_risk <= 40 and overstock_risk <= 25:

        recommendations.append(
            "✅ Inventory position is relatively balanced against expected demand."
        )

    # -------------------------
    # Pricing Analysis
    # -------------------------

    if competitor_price > current_price:

        difference = competitor_price - current_price

        recommendations.append(
            f"💰 Competitor pricing is ${difference:.2f} higher. "
            "There may be an opportunity for a controlled price increase."
        )

    elif competitor_price < current_price:

        difference = current_price - competitor_price

        recommendations.append(
            f"💰 Current price is ${difference:.2f} higher than the competitor. "
            "Review pricing strategy to protect competitiveness."
        )

    else:

        recommendations.append(
            "💰 Current pricing is aligned with competitor pricing."
        )

    return recommendations