import streamlit as st
from src.ui import load_css

load_css()
from src.pricing_engine import pricing_recommendation
st.set_page_config(
    page_title="Dynamic Pricing",
    layout="wide"
)

st.title("💰 AI Dynamic Pricing Advisor")

st.markdown(
    "Get AI-powered pricing recommendations based on demand and competition."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    current_price = st.number_input(
        "Current Price",
        value=50.0
    )

    competitor_price = st.number_input(
        "Competitor Price",
        value=55.0
    )

with col2:

    predicted_demand = st.number_input(
        "Predicted Demand",
        value=180
    )

    inventory = st.number_input(
        "Inventory Level",
        value=120
    )

st.divider()

recommend = st.button(
    "🚀 Generate Pricing Recommendation"
)

if recommend:

    result = pricing_recommendation(
        current_price=current_price,
        competitor_price=competitor_price,
        predicted_demand=predicted_demand,
        inventory=inventory
    )

    st.divider()

    st.subheader("🤖 AI Pricing Recommendation")

    st.success(result["recommendation"])

    st.write("### Why?")

    st.info(result["reason"])

    st.write(f"**Risk Level:** {result['risk']}")