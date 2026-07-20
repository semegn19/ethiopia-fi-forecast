import plotly.express as px
import streamlit as st
import pandas as pd

data = pd.read_excel(
    "../data/processed/ethiopia_fi_enriched.xlsx",
    sheet_name="Data"
)

st.title("Historical Trends")

indicator = st.selectbox(
    "Indicator",
    [
        "ACC_OWNERSHIP",
        "USG_DIGITAL_PAYMENT"
    ]
)

plot = data[
    data["indicator_code"]==indicator
]

years = st.slider(
    "Year",
    2011,
    2027,
    (2011,2024)
)

plot = plot[
    plot["fiscal_year"].between(
        years[0],
        years[1]
    )
]

fig = px.line(
    plot,
    x="fiscal_year",
    y="value_numeric",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

compare = data[
    data["indicator_code"].isin(
        [
            "ACC_OWNERSHIP",
            "USG_DIGITAL_PAYMENT",
            "ACC_MM_ACCOUNT"
        ]
    )
]

fig = px.line(
    compare,
    x="fiscal_year",
    y="value_numeric",
    color="indicator"
)

st.plotly_chart(fig)