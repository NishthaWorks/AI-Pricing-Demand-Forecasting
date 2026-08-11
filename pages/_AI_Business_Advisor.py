import streamlit as st

from src.business_score import calculate_business_health
from src.business_advisor import generate_executive_summary
from src.inventory_engine import calculate_inventory_metrics
from src.report_generator import generate_report


st.set_page_config(
    page_title="AI Business Advisor",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Business Advisor")

st.write(
    "AI-powered executive recommendations using "
    "pricing, demand and inventory intelligence."
)

st.divider()


# =========================================================
# INPUTS
# =========================================================

col1, col2 = st.columns(2)


with col1:

    predicted_demand = st.slider(
        "📈 Predicted Monthly Demand",
        min_value=50,
        max_value=500,
        value=220
    )

    inventory = st.slider(
        "📦 Inventory Level",
        min_value=0,
        max_value=500,
        value=120
    )


with col2:

    current_price = st.slider(
        "💰 Current Price",
        min_value=10,
        max_value=100,
        value=55
    )

    competitor_price = st.slider(
        "🏷️ Competitor Price",
        min_value=10,
        max_value=100,
        value=60
    )


st.divider()


generate = st.button(
    "🚀 Generate AI Business Report",
    use_container_width=True
)


# =========================================================
# ONLY RUN ANALYSIS AFTER BUTTON CLICK
# =========================================================

if generate:

    # -----------------------------------------------------
    # INVENTORY
    # -----------------------------------------------------

    inventory_result = calculate_inventory_metrics(
        inventory,
        predicted_demand,
        predicted_demand
    )


    # -----------------------------------------------------
    # BUSINESS SCORE
    # -----------------------------------------------------

    score, status = calculate_business_health(
        inventory_result["stockout_risk"],
        inventory_result["overstock_risk"],
        predicted_demand,
        competitor_price,
        current_price
    )


    # -----------------------------------------------------
    # EXECUTIVE SUMMARY
    # -----------------------------------------------------

    summary = generate_executive_summary(
        predicted_demand,
        inventory_result["stockout_risk"],
        inventory_result["overstock_risk"],
        current_price,
        competitor_price
    )


    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    st.subheader("📊 Executive Recommendations")

    for item in summary:

        st.success(item)


    # =====================================================
    # RISK METRICS
    # =====================================================

    st.divider()

    st.subheader("📊 Business Risk Overview")

    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "⚠️ Stockout Risk",
            f"{inventory_result['stockout_risk']:.1f}%"
        )


    with c2:

        st.metric(
            "📦 Overstock Risk",
            f"{inventory_result['overstock_risk']:.1f}%"
        )


    with c3:

        st.metric(
            "🔥 Priority",
            inventory_result["priority"]
        )


    # =====================================================
    # BUSINESS HEALTH
    # =====================================================

    st.divider()

    st.subheader("📈 Business Health")


    st.metric(
        "Overall Business Score",
        f"{score}/100"
    )


    st.progress(
        max(0.0, min(score / 100, 1.0))
    )


    if score >= 90:

        st.success(
            f"🟢 {status}"
        )

    elif score >= 75:

        st.warning(
            f"🟡 {status}"
        )

    else:

        st.error(
            f"🔴 {status}"
        )


    # =====================================================
    # PDF REPORT
    # =====================================================

    st.divider()

    st.subheader("📄 Executive Report")


    recommendation_text = " ".join(summary)


    report_file = generate_report(
        business_score=score,
        demand=predicted_demand,
        stockout_risk=inventory_result["stockout_risk"],
        overstock_risk=inventory_result["overstock_risk"],
        recommendation=recommendation_text
    )


    with open(report_file, "rb") as file:

        st.download_button(
            label="📄 Download Executive PDF Report",
            data=file,
            file_name="Retail_AI_Executive_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )


st.divider()


st.caption(
    "Retail AI Control Tower | AI-Powered Decision Intelligence Platform"
)