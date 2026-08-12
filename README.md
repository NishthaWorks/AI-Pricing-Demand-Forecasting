# 📈 AI Pricing & Demand Forecasting Platform

An AI-powered retail decision intelligence platform designed to help businesses make better decisions across **demand forecasting, pricing, inventory management and executive planning**.

The project combines machine learning with business intelligence to transform historical retail data into actionable commercial insights.

---

## 🎯 Business Problem

Retail businesses continuously need to answer questions such as:

- How much demand should we expect?
- Should we increase or decrease prices?
- Are inventory levels sufficient?
- Is there a risk of stockouts or overstocking?
- How could a pricing decision affect revenue?
- What should management prioritise?

This platform brings these decisions together into a single AI-powered business environment.

---

## 🚀 Key Capabilities

### 📈 Demand Forecasting

A machine-learning based demand forecasting pipeline predicts expected product demand using historical retail data and engineered business features.

The forecasting workflow includes:

- Data understanding
- Exploratory data analysis
- Business analysis
- Feature engineering
- Categorical encoding
- Model training
- Model evaluation
- Demand prediction

---

### 💰 Dynamic Pricing Intelligence

The pricing module evaluates:

- Current price
- Competitor price
- Predicted demand
- Inventory position

and generates pricing recommendations designed to support revenue and demand decisions.

---

### 📦 Inventory Optimization

The inventory engine evaluates the relationship between:

**Inventory → Forecast Demand → Stockout Risk → Overstock Risk**

and provides recommendations such as:

- Replenish inventory
- Maintain current inventory
- Reduce purchasing

---

### 🤖 AI Business Advisor

The AI Business Advisor combines:

- Demand intelligence
- Pricing intelligence
- Inventory intelligence
- Business health scoring

to generate executive-level recommendations.

It provides:

- Business Health Score
- Stockout Risk
- Overstock Risk
- Priority Level
- Executive Recommendations

---

### 🎮 What-if Business Simulator

The simulator allows users to test pricing scenarios before making business decisions.

Users can change:

- Current price
- Proposed price
- Forecast demand
- Inventory

The simulator then evaluates:

- Current revenue
- Simulated revenue
- Revenue change
- Simulated demand
- Inventory remaining
- Business impact

This creates a practical decision-support layer on top of the forecasting and pricing models.

---

### 🧠 Executive Decision Center

The executive dashboard provides a consolidated view of:

- Units sold
- Forecast demand
- Pricing
- Competitor pricing
- Inventory
- Category performance
- Regional demand
- Business alerts
- Business health
- AI-generated executive insights

---

## 🏗️ Project Architecture

```text
AI-Pricing-Demand-Forecasting/
│
├── app.py
│
├── data/
│   └── raw/
│       └── retail_store_inventory (1).csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_business_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_demand_forecasting_model.ipynb
│   ├── 06_dynamic_pricing_engine.ipynb
│   └── 07_inventory_optimization.ipynb
│
├── pages/
│   ├── _Executive_Dashboard.py
│   ├── _Demand_Forecast.py
│   ├── _Dynamic_Pricing.py
│   ├── _Inventory_Optimization.py
│   ├── _AI_Business_Advisor.py
│   ├── _What_If_Simulator.py
│   └── _Business_Analytics.py
│
├── src/
│   ├── business_advisor.py
│   ├── business_alerts.py
│   ├── business_score.py
│   ├── charts.py
│   ├── data_loader.py
│   ├── explainability.py
│   ├── forecasting.py
│   ├── inventory_engine.py
│   ├── preprocessing.py
│   ├── pricing_engine.py
│   ├── report_generator.py
│   ├── simulator.py
│   ├── ui.py
│   └── utils.py
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
├── requirements.txt
└── README.md