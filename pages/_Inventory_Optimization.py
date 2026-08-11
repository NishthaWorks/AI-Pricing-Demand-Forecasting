import streamlit as st
from src.ui import load_css

load_css()

from src.inventory_engine import calculate_inventory_metrics

st.set_page_config(
    page_title="Inventory Optimization",
    layout="wide"
)

st.title("📦 Inventory Optimization Engine")

st.markdown(
    "AI-powered inventory intelligence for retail decision making."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    inventory = st.number_input(
        "Current Inventory",
        min_value=0,
        value=120
    )

    predicted_demand = st.number_input(
        "Predicted Monthly Demand",
        min_value=1,
        value=180
    )

with col2:

    units_ordered = st.number_input(
        "Units Ordered",
        min_value=0,
        value=100
    )

generate = st.button("🚀 Analyze Inventory")

if generate:

    result = calculate_inventory_metrics(
        inventory,
        predicted_demand,
        units_ordered
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "📅 Days Left",
        f"{result['days_left']} days"
    )

    c2.metric(
        "🛡 Safety Stock",
        result["safety_stock"]
    )

    c3.metric(
        "🚚 Reorder Quantity",
        result["reorder_qty"]
    )

    st.divider()

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "⚠️ Stockout Risk",
        f"{result['stockout_risk']}%"
    )

    c5.metric(
        "📦 Overstock Risk",
        f"{result['overstock_risk']}%"
    )

    c6.metric(
        "🔥 Priority",
        result["priority"]
    )