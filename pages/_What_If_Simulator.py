import streamlit as st

from src.ui import load_css
from src.simulator import simulate_price_change

load_css()

st.set_page_config(
    page_title="What-if Simulator",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 AI What-if Business Simulator")

st.markdown(
    """
    ### Test pricing decisions before making them in the real world.

    Adjust price, demand and inventory assumptions to understand
    the potential business impact of a pricing decision.
    """
)

st.divider()

# =========================================================
# INPUTS
# =========================================================

st.subheader("🎛️ Business Scenario")

col1, col2 = st.columns(2)

with col1:

    current_price = st.slider(
        "Current Price",
        min_value=10,
        max_value=100,
        value=55
    )

    new_price = st.slider(
        "Proposed New Price",
        min_value=10,
        max_value=100,
        value=60
    )

with col2:

    predicted_demand = st.slider(
        "Predicted Monthly Demand",
        min_value=50,
        max_value=500,
        value=220
    )

    inventory = st.slider(
        "Current Inventory",
        min_value=0,
        max_value=500,
        value=250
    )

st.divider()

run = st.button(
    "🚀 Run AI Simulation",
    use_container_width=True
)

# =========================================================
# SIMULATION
# =========================================================

if run:

    result = simulate_price_change(
        current_price,
        new_price,
        predicted_demand,
        inventory
    )

    current_revenue = result["current_revenue"]
    new_revenue = result["new_revenue"]

    revenue_change = new_revenue - current_revenue

    if current_revenue != 0:
        revenue_change_pct = (
            revenue_change / current_revenue
        ) * 100
    else:
        revenue_change_pct = 0

    # =====================================================
    # EXECUTIVE RESULT
    # =====================================================

    st.subheader("📊 Simulation Results")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Current Revenue",
            f"${current_revenue:,.0f}"
        )

    with c2:
        st.metric(
            "Simulated Revenue",
            f"${new_revenue:,.0f}",
            delta=f"{revenue_change_pct:+.1f}%"
        )

    with c3:
        st.metric(
            "Simulated Demand",
            f"{result['simulated_demand']:,.0f}"
        )

    with c4:
        st.metric(
            "Inventory Remaining",
            f"{result['inventory_remaining']:,.0f}"
        )

    st.divider()

    # =====================================================
    # BEFORE VS AFTER
    # =====================================================

    st.subheader("🔄 Before vs After")

    comparison_data = {
        "Metric": [
            "Price",
            "Demand",
            "Revenue"
        ],
        "Current Scenario": [
            f"${current_price:.2f}",
            f"{predicted_demand:,.0f}",
            f"${current_revenue:,.0f}"
        ],
        "Proposed Scenario": [
            f"${new_price:.2f}",
            f"{result['simulated_demand']:,.0f}",
            f"${new_revenue:,.0f}"
        ]
    }

    st.table(comparison_data)

    st.divider()

    # =====================================================
    # AI DECISION
    # =====================================================

    st.subheader("🤖 AI Decision Support")

    if revenue_change_pct >= 10:

        st.success(
            f"""
            🟢 **Strong Opportunity**

            The proposed pricing scenario is projected to increase
            revenue by **{revenue_change_pct:.1f}%**.

            The scenario appears commercially attractive, subject
            to inventory and competitive considerations.
            """
        )

    elif revenue_change_pct > 0:

        st.info(
            f"""
            🔵 **Potential Opportunity**

            The proposed price change is projected to increase
            revenue by **{revenue_change_pct:.1f}%**.

            Consider testing the change on a limited segment
            before implementing it broadly.
            """
        )

    elif revenue_change_pct == 0:

        st.warning(
            """
            🟡 **Neutral Scenario**

            The proposed pricing change produces approximately
            the same projected revenue as the current scenario.
            """
        )

    else:

        st.error(
            f"""
            🔴 **Potential Revenue Risk**

            The proposed pricing scenario is projected to reduce
            revenue by **{abs(revenue_change_pct):.1f}%**.

            Consider maintaining the current price or testing
            a smaller price adjustment.
            """
        )

    # =====================================================
    # INVENTORY WARNING
    # =====================================================

    if result["inventory_remaining"] < 0:

        st.error(
            "🚨 Inventory Warning: Projected demand exceeds available inventory."
        )

    elif result["inventory_remaining"] < predicted_demand * 0.2:

        st.warning(
            "⚠️ Inventory Warning: Remaining inventory is relatively low. "
            "Replenishment may be required."
        )

    else:

        st.success(
            "📦 Inventory Status: Sufficient inventory is available "
            "under the simulated scenario."
        )


st.divider()

st.caption(
    "Retail AI Control Tower | AI-Powered Decision Intelligence Platform"
)