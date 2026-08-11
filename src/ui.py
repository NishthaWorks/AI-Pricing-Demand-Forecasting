import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =====================================================
           GLOBAL APP
        ===================================================== */

        .stApp {
            background: #F7F9FC;
        }

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1400px;
        }


        /* =====================================================
           TYPOGRAPHY
        ===================================================== */

        h1 {
            color: #172554;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        h2 {
            color: #1E3A8A;
            font-weight: 750;
        }

        h3 {
            color: #334155;
            font-weight: 700;
        }

        p {
            color: #475569;
        }


        /* =====================================================
           KPI CARDS
        ===================================================== */

        div[data-testid="metric-container"] {

            background: #FFFFFF;

            border: 1px solid #E2E8F0;

            border-radius: 16px;

            padding: 20px;

            box-shadow:
                0px 4px 12px rgba(15, 23, 42, 0.04);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }


        div[data-testid="metric-container"]:hover {

            transform: translateY(-3px);

            box-shadow:
                0px 10px 25px rgba(15, 23, 42, 0.08);
        }


        div[data-testid="stMetricLabel"] {

            color: #64748B;

            font-weight: 600;
        }


        div[data-testid="stMetricValue"] {

            color: #0F172A;

            font-weight: 800;
        }


        /* =====================================================
           BUTTONS
        ===================================================== */

        .stButton > button {

            background: #2563EB;

            color: white;

            border: none;

            border-radius: 12px;

            font-weight: 700;

            min-height: 48px;

            padding: 0 22px;

            box-shadow:
                0px 6px 15px rgba(37, 99, 235, 0.20);

            transition:
                all 0.2s ease;
        }


        .stButton > button:hover {

            background: #1D4ED8;

            transform: translateY(-2px);

            box-shadow:
                0px 10px 20px rgba(37, 99, 235, 0.25);
        }


        /* =====================================================
           DOWNLOAD BUTTON
        ===================================================== */

        .stDownloadButton > button {

            border-radius: 12px;

            font-weight: 700;

            min-height: 48px;
        }


        /* =====================================================
           SIDEBAR
        ===================================================== */

        section[data-testid="stSidebar"] {

            background: #0F172A;

            border-right: 1px solid #1E293B;
        }


        section[data-testid="stSidebar"] * {

            color: #E2E8F0;
        }


        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {

            color: #FFFFFF;
        }


        /* =====================================================
           ALERT / INFO BOXES
        ===================================================== */

        div[data-testid="stAlert"] {

            border-radius: 12px;

            border-width: 1px;

            padding: 14px 18px;
        }


        /* =====================================================
           SLIDERS
        ===================================================== */

        div[data-baseweb="slider"] {

            padding-top: 10px;

            padding-bottom: 10px;
        }


        /* =====================================================
           DATAFRAMES / TABLES
        ===================================================== */

        div[data-testid="stDataFrame"] {

            border-radius: 14px;

            overflow: hidden;

            border: 1px solid #E2E8F0;
        }


        /* =====================================================
           TABS
        ===================================================== */

        button[data-baseweb="tab"] {

            font-weight: 600;
        }


        /* =====================================================
           DIVIDERS
        ===================================================== */

        hr {

            border: none;

            border-top: 1px solid #E2E8F0;

            margin: 1.5rem 0;
        }


        /* =====================================================
           FOOTER
        ===================================================== */

        footer {

            visibility: hidden;
        }


        /* =====================================================
           MOBILE / SMALL SCREEN
        ===================================================== */

        @media (max-width: 768px) {

            .main .block-container {

                padding-left: 1rem;

                padding-right: 1rem;
            }

            h1 {

                font-size: 2rem;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )