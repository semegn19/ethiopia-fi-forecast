# Ethiopia Financial Inclusion Forecasting System

A data science project that analyzes, models, and forecasts Ethiopia's financial inclusion indicators using historical observations, policy events, infrastructure developments, and digital finance ecosystem data.

## Project Overview

This project was completed as part of a financial inclusion forecasting assignment for **Selam Analytics**, a financial technology consulting firm supporting a consortium of development finance institutions, mobile money operators, and the National Bank of Ethiopia.

The objective is to build a forecasting system capable of predicting Ethiopia's progress on the two core dimensions of financial inclusion defined by the **World Bank Global Findex**:

- **Access** – Account Ownership Rate
- **Usage** – Digital Payment Adoption Rate

The project combines historical financial inclusion data with policy events, infrastructure developments, and market milestones to understand the drivers of financial inclusion and forecast future outcomes for **2025–2027**.

---

## Business Problem

Despite rapid digital transformation—including:

- Telebirr growing to over **54 million users**
- M-Pesa entering Ethiopia in **2023**
- Interoperable digital P2P transfers surpassing ATM withdrawals

only **49% of Ethiopian adults** owned a financial account in the 2024 Global Findex survey.

This project seeks to answer:

- What drives financial inclusion in Ethiopia?
- How do policies and market events affect financial inclusion?
- What will Ethiopia's financial inclusion look like in 2025–2027?

---

## Project Objectives

- Explore and understand the unified financial inclusion dataset
- Enrich the dataset using credible external sources
- Analyze historical financial inclusion trends
- Model relationships between national events and financial inclusion indicators
- Forecast Access and Usage for 2025–2027
- Build an interactive dashboard for visualization

---

## Project Structure

```
financial-inclusion-forecasting/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── data_enrichment.ipynb
│   ├── eda.ipynb
│   ├── Task3_Event_Impact_Modeling.ipynb
│   ├── Task4_Forecasting.ipynb
│   └── Task5_Dashboard.ipynb
│
├── reports/
│   ├── data_enrichment_log.md
│
├── dashboard/
│
├── src/
│
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses a **unified financial inclusion dataset** consisting of four record types:

| Record Type | Description |
|-------------|-------------|
| Observation | Historical measurements from surveys and operators |
| Event | Product launches, policies, infrastructure, milestones |
| Impact Link | Relationships between events and indicators |
| Target | Official government targets |

The dataset follows a unified schema where events remain neutral and their effects are modeled separately through **impact links**.

---

## Data Sources

The project integrates information from multiple authoritative sources including:

- World Bank Global Findex
- National Bank of Ethiopia (NBE)
- IMF Financial Access Survey (FAS)
- GSMA
- ITU
- Ethio Telecom
- Safaricom Ethiopia
- Official government publications

---

## Methodology

### Task 1 — Data Exploration & Enrichment

- Schema validation
- Data quality assessment
- Missing value analysis
- Dataset enrichment
- Documentation of newly collected records

---

### Task 2 — Exploratory Data Analysis

- Financial inclusion trends
- Account ownership analysis
- Digital payment adoption analysis
- Infrastructure analysis
- Event timeline visualization
- Event-indicator relationship exploration

---

### Task 3 — Event Impact Modeling

- Event-indicator association matrix
- Lag effect analysis
- Historical validation
- Event impact scoring

---

### Task 4 — Forecasting

Forecasts are generated for:

- Access (Account Ownership)
- Usage (Digital Payments)

Forecast horizon:

- 2025
- 2026
- 2027

Including:

- Confidence intervals
- Scenario analysis
- Trend projections

---

### Task 5 — Dashboard

Interactive dashboard displaying:

- Historical trends
- Forecasts
- Event timeline
- Infrastructure indicators
- Policy impacts

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Jupyter Notebook

---

## Repository Contents

- Exploratory analysis notebooks
- Forecasting models
- Data enrichment scripts
- Visualization notebooks
- Final datasets
- Reports
- Dashboard source code

---

## Key Outputs

- Cleaned and enriched financial inclusion dataset
- Event-impact relationship matrix
- Exploratory visualizations
- Forecasts for 2025–2027
- Interactive dashboard
- Interim project report