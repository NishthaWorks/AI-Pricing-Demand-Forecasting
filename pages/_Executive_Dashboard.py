import streamlit as st
import pandas as pd
import plotly.express as px
from src.business_alerts import generate_alerts
from src.data_loader import load_data
from src.ui import load_css

load_css()

st.set_page_config(
    page_title="Executive Dashboard",
    layout="wide"
)

# --------------------------

df = load_data()

# --------------------------

st.title("🧠 Executive Decision Center")

st.markdown("""
### AI-Powered Retail Business Intelligence

Monitor business performance, pricing opportunities,
inventory health and demand insights from one dashboard.
""")

st.divider()

# ==========================
# KPI CARDS
# ==========================

total_sales = df["Units Sold"].sum()

avg_price = df["Price"].mean()

avg_inventory = df["Inventory Level"].mean()

avg_demand = df["Demand Forecast"].mean()

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "📦 Units Sold",
    f"{total_sales:,.0f}"
)

c2.metric(
    "💰 Avg Price",
    f"${avg_price:.2f}"
)

c3.metric(
    "📈 Avg Demand",
    f"{avg_demand:.0f}"
)

c4.metric(
    "🏬 Avg Inventory",
    f"{avg_inventory:.0f}"
)

st.divider()
alerts = generate_alerts(
    avg_demand,
    avg_inventory,
    avg_price,
    avg_price - 2
)

st.subheader("🚨 Business Alerts")

for alert in alerts:
    st.warning(alert)

# ==========================
# CHARTS
# ==========================

left,right = st.columns(2)

with left:

    category = (
        df.groupby("Category")["Units Sold"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category,
        x="Category",
        y="Units Sold",
        title="Units Sold by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    region = (
        df.groupby("Region")["Demand Forecast"]
        .mean()
        .reset_index()
    )

    fig = px.pie(
        region,
        names="Region",
        values="Demand Forecast",
        title="Demand Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================
# BUSINESS HEALTH
# ==========================

health = 94

st.subheader("📈 Executive Business Health")

progress = health/100

st.progress(progress)

st.metric(
    "Overall Business Score",
    f"{health}/100"
)

if health>90:

    st.success(
        "Business performance is excellent. Continue current pricing strategy while monitoring inventory levels."
    )

elif health>75:

    st.warning(
        "Business is healthy but there are opportunities for optimization."
    )

else:

    st.error(
        "Immediate business intervention recommended."
    )

st.divider()

# ==========================
# AI INSIGHTS
# ==========================

st.subheader("🤖 AI Executive Insights")

st.info("""
• Demand remains consistently strong.

• Inventory levels are stable across most regions.

• Competitor pricing indicates opportunity for selective price increases.

• Business Health Score suggests low operational risk.

• Focus on Technology products for maximum revenue growth.
""")

st.divider()

st.caption(
    "Retail AI Control Tower | Executive Dashboard | Built by Nishtha"
)