def generate_alerts(
    demand,
    inventory,
    current_price,
    competitor_price
):
    alerts = []

    if demand > 250:
        alerts.append("📈 High demand expected. Monitor inventory closely.")

    if inventory < 100:
        alerts.append("📦 Inventory is running low. Replenishment recommended.")

    if competitor_price < current_price:
        alerts.append("💰 Competitor pricing is lower. Review pricing strategy.")

    if not alerts:
        alerts.append("✅ No critical business alerts.")

    return alerts