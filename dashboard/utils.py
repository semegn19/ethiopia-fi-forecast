import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    data = pd.read_excel(
        "../data/processed/ethiopia_fi_enriched.xlsx",
        sheet_name="Data"
    )

    impact = pd.read_excel(
        "../data/processed/ethiopia_fi_enriched.xlsx",
        sheet_name="Impact_sheet"
    )

    forecast = pd.read_csv(
        "../data/processed/forecast_results.csv"
    )

    return data, impact, forecast