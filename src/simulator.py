def simulate_price_change(
    current_price,
    new_price,
    predicted_demand,
    inventory
):
    """
    Simulate business impact after changing price.
    """

    # Percentage price change
    price_change = ((new_price - current_price) / current_price) * 100

    # Simple price elasticity assumption
    elasticity = -0.8

    demand_change = elasticity * price_change

    simulated_demand = max(
        1,
        round(
            predicted_demand * (1 + demand_change / 100)
        )
    )

    current_revenue = current_price * predicted_demand

    new_revenue = new_price * simulated_demand

    inventory_after_sales = max(
        0,
        inventory - simulated_demand
    )

    return {
        "simulated_demand": simulated_demand,
        "current_revenue": round(current_revenue, 2),
        "new_revenue": round(new_revenue, 2),
        "inventory_remaining": inventory_after_sales
    }