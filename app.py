import streamlit as st
from src.ui import load_css

load_css()

st.set_page_config(
    page_title="Retail AI Control Tower",
    page_icon="🛒",
    layout="wide"
)
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:18px;
    box-shadow:0 3px 12px rgba(0,0,0,0.08);
}

h1{
    color:#2563EB;
}

</style>
""",unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("🛒 Retail AI Control Tower")

st.sidebar.markdown("---")

st.sidebar.success("AI Decision Intelligence Platform")

st.sidebar.markdown("""
### Available Modules

📈 Demand Forecasting

💰 Dynamic Pricing

📦 Inventory Optimization

🤖 AI Business Advisor

🎮 What-if Simulator

📊 Executive Dashboard
""")

st.sidebar.markdown("---")

st.sidebar.success("Retail AI Platform")

st.sidebar.caption("""
Version 1.0

AI for Business

Machine Learning

Decision Intelligence
""")

st.sidebar.caption("Developed by Nishtha")

# -------------------------------
# Header
# -------------------------------


st.markdown("""
# 🛒 Retail AI Control Tower

### AI-Powered Decision Intelligence Platform

Forecast demand, optimize pricing, reduce inventory risks and help executives make smarter retail decisions using Machine Learning.

""")

st.divider()

# -------------------------------
# KPI Cards
# -------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Dataset",
    "73,100 Rows"
)

c2.metric(
    "ML Model",
    "Random Forest"
)

c3.metric(
    "Business Modules",
    "6"
)

c4.metric(
    "Status",
    "Ready ✅"
)

st.divider()

# -------------------------------
# Features
# -------------------------------

st.subheader("🚀 Platform Capabilities")

col1, col2 = st.columns(2)

with col1:

    st.info("""
📈 Demand Forecasting

Predict future product demand using Machine Learning.
""")

    st.info("""
💰 Dynamic Pricing

Recommend pricing strategies based on demand and competitors.
""")

    st.info("""
📦 Inventory Optimization

Reduce stockouts and overstock situations.
""")

with col2:

    st.info("""
🤖 AI Business Advisor

Generate executive recommendations automatically.
""")

    st.info("""
🎮 What-if Simulator

Simulate pricing decisions before implementation.
""")

    st.info("""
📊 Executive Dashboard

Monitor KPIs and business health in real time.
""")

st.divider()

# -------------------------------
# Footer
# -------------------------------

st.info("""
### 🚀 Ready to Explore

Use the sidebar to open each AI module and interact with the platform.

Each module represents one stage of retail decision intelligence.
""")
st.divider()

st.caption(
    "Retail AI Control Tower | AI-Powered Decision Intelligence Platform | Developed by Nishtha"
)