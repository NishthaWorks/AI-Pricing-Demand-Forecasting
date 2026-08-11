import streamlit as st
import plotly.express as px
from src.data_loader import load_data
from src.ui import load_css

load_css()
st.set_page_config(page_title="Business Analytics", layout="wide")

st.title("📊 Business Analytics")

df = load_data()

st.markdown("### Category-wise Average Demand")

category_demand = (
    df.groupby("Category")["Demand Forecast"]
    .mean()
    .reset_index()
)

fig = px.bar(
    category_demand,
    x="Category",
    y="Demand Forecast",
    color="Category",
    text_auto=".1f"
)

fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

st.markdown("### Region-wise Average Price")

region_price = (
    df.groupby("Region")["Price"]
    .mean()
    .reset_index()
)

fig2 = px.pie(
    region_price,
    names="Region",
    values="Price",
    hole=0.45
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("### Inventory Distribution")

fig3 = px.histogram(
    df,
    x="Inventory Level",
    nbins=40
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.subheader("🧠 Executive Insights")

highest_category = category_demand.sort_values(
    "Demand Forecast",
    ascending=False
).iloc[0]

highest_region = region_price.sort_values(
    "Price",
    ascending=False
).iloc[0]

st.info(
    f"""
• Highest demand category: **{highest_category['Category']}**

• Highest average price region: **{highest_region['Region']}**

• Average inventory level: **{df['Inventory Level'].mean():.0f} units**
"""
)

