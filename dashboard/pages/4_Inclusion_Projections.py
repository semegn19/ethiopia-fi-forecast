import streamlit as st
import plotly.express as px
import pandas as pd

forecast_df = pd.read_csv(
    "../data/processed/forecast_results.csv"
)

scenario = st.selectbox(
    "Scenario",
    [
        "Optimistic",
        "Base",
        "Pessimistic"
    ]
)

target = 60

forecast = 55

st.progress(
    forecast/target
)

st.metric(
    "Progress Toward 60%",
    f"{forecast}%",
    f"{forecast-target}%"
)

fig = px.line(
    forecast_df,
    x="Year",
    y="Access Forecast"
)

st.plotly_chart(fig)

st.subheader("Key Findings")

st.success("""
What drives financial inclusion?

• Digital infrastructure

• Mobile money

• Regulatory reforms

• Competition

• Smartphone adoption
""")

st.info("""
Largest projected impacts:

Telebirr

M-Pesa

NFIS-II

Fayda
""")

st.download_button(
    label="Download Forecast",
    data=forecast_df.to_csv(index=False),
    file_name="forecast.csv",
    mime="text/csv"
)