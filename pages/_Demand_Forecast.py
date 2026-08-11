import streamlit as st
import pandas as pd
from src.ui import load_css

load_css()
from src.forecasting import predict_demand

st.set_page_config(
    page_title="Demand Forecast",
    layout="wide"
)

st.title("📈 AI Demand Forecast")

st.markdown(
    "Predict product demand using the trained AI model."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    category = st.selectbox(
        "Category",
        [
            "Electronics",
            "Furniture",
            "Groceries",
            "Clothing",
            "Toys"
        ]
    )

    region = st.selectbox(
        "Region",
        [
            "North",
            "South",
            "East",
            "West"
        ]
    )

    weather = st.selectbox(
        "Weather",
        [
            "Sunny",
            "Rainy",
            "Cloudy",
            "Snowy"
        ]
    )

    season = st.selectbox(
        "Season",
        [
            "Spring",
            "Summer",
            "Autumn",
            "Winter"
        ]
    )

with col2:

    inventory = st.number_input(
        "Inventory Level",
        value=200
    )

    units_sold = st.number_input(
        "Units Sold",
        value=120
    )

    units_ordered = st.number_input(
        "Units Ordered",
        value=250
    )

    price = st.number_input(
        "Price",
        value=50.0
    )

    discount = st.slider(
        "Discount %",
        0,
        20,
        10
    )

    promotion = st.selectbox(
        "Holiday / Promotion",
        [0, 1]
    )

    competitor = st.number_input(
        "Competitor Price",
        value=55.0
    )

st.divider()

predict_button = st.button("🚀 Predict Demand")