import streamlit as st
import pandas as pd
import plotly.express as px

forecast = pd.read_csv(
    "../data/processed/forecast_results.csv"
)

st.title("Forecasts")

model = st.radio(
    "Forecast",
    [
        "Trend",
        "Event-Augmented"
    ]
)

fig = px.line(
    forecast,
    x="Year",
    y="Access Forecast"
)

fig.add_scatter(
    x=forecast["Year"],
    y=forecast["Upper"],
    line=dict(width=0),
    showlegend=False
)

fig.add_scatter(
    x=forecast["Year"],
    y=forecast["Lower"],
    fill="tonexty",
    line=dict(width=0),
    name="95% CI"
)

st.plotly_chart(fig)

st.subheader("Projected Milestones")

st.write("""
• Account ownership expected to exceed 50%

• Digital payments continue rapid growth

• Infrastructure investments sustain adoption
""")
