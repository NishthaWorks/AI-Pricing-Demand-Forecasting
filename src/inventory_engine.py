import math


def calculate_inventory_metrics(
    inventory_level,
    predicted_demand,
    units_ordered
):
    """
    Calculate inventory intelligence metrics.
    """

    # Prevent division by zero
    daily_demand = max(predicted_demand / 30, 1)

    # Days inventory will last
    days_left = inventory_level / daily_demand

    # Safety stock (20% of monthly demand)
    safety_stock = predicted_demand * 0.20

    # Stockout Risk Score
    stockout_risk = max(
        0,
        min(
            100,
            round(
                (1 - inventory_level / max(predicted_demand, 1)) * 100,
                1
            )
        )
    )

    # Overstock Risk Score
    overstock_risk = max(
        0,
        min(
            100,
            round(
                ((inventory_level - predicted_demand) / max(predicted_demand, 1)) * 100,
                1
            )
        )
    )

    # Recommended Reorder Quantity
    reorder_qty = max(
        0,
        math.ceil(predicted_demand + safety_stock - inventory_level)
    )

    # Priority
    if stockout_risk >= 70:
        priority = "🔴 Urgent"

    elif stockout_risk >= 40:
        priority = "🟡 Medium"

    else:
        priority = "🟢 Low"

    return {
        "days_left": round(days_left, 1),
        "safety_stock": round(safety_stock),
        "stockout_risk": stockout_risk,
        "overstock_risk": max(0, overstock_risk),
        "reorder_qty": reorder_qty,
        "priority": priority
    }