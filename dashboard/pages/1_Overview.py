import streamlit as st
import pandas as pd

data = pd.read_excel(
    "../data/processed/ethiopia_fi_enriched.xlsx",
    sheet_name="Data"
)

st.title("Overview")

access = 49

usage = 35

telebirr = 54

mpesa = 10

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Account Ownership",
    "49%",
    "+3pp"
)

c2.metric(
    "Digital Payments",
    "35%",
    "+7%"
)

c3.metric(
    "Telebirr Users",
    "54M"
)

c4.metric(
    "M-Pesa Users",
    "10M"
)

st.subheader("Digital Payments")

st.metric(
    "P2P / ATM Crossover",
    "P2P > ATM",
    "Historic Milestone"
)

growth = pd.DataFrame(
    {
        "Period":[
            "2011-2014",
            "2014-2017",
            "2017-2021",
            "2021-2024"
        ],
        "Growth":[8,13,11,3]
    }
)

st.bar_chart(
    growth,
    x="Period",
    y="Growth"
)