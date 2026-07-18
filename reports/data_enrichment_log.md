# Ethiopia Financial Inclusion Dataset — Data Enrichment Log

## Project

**Project:** Ethiopia Financial Inclusion Forecasting System  
**Task:** Task 1 — Data Exploration and Enrichment  
**Dataset:** `ethiopia_fi_unified_data.xlsx`  
**Enriched Dataset:** `ethiopia_fi_enriched.xlsx`  
**Collection date:** 2026-07-18  

---

## 1. Purpose of the Enrichment

The starter dataset contains observations, events, targets, and modeled impact relationships related to financial inclusion in Ethiopia. The dataset was enriched to provide additional explanatory variables and event relationships that may improve the forecasting of the two core financial inclusion dimensions:

- **ACCESS:** Account Ownership Rate
- **USAGE:** Digital Payment Adoption

The enrichment focused on adding data that could help explain changes in account ownership, digital payment adoption, mobile money use, and the broader digital financial ecosystem.

---

## 2. Dataset Structure

The original workbook contains two relevant sheets:

### Data sheet

The `Data` sheet contains records with the following record types:

| Record Type | Description |
|---|---|
| `observation` | Measured values from surveys, operators, regulators, or other sources |
| `event` | Policies, product launches, market entries, infrastructure investments, and milestones |
| `target` | Official financial inclusion targets and policy goals |

### Impact_sheet

The `Impact_sheet` contains modeled relationships between events and indicators.

The relationship is represented using:

```text
event.record_id
        │
        │ matches
        ▼
impact_link.parent_id
        │
        ▼
impact_link.related_indicator
````

For example:

```text
Event:
EVT_0001 — Telebirr Launch
        │
        ▼
Impact Link:
parent_id = EVT_0001
pillar = ACCESS
related_indicator = ACC_OWNERSHIP
impact_direction = increase
```

---

## 3. Schema Design Decision

Events were not assigned directly to a pillar.

For example, the following structure was intentionally avoided:

```text
Telebirr Launch → USAGE
```

This would be an oversimplification because a single event may affect multiple dimensions of financial inclusion.

For example, the launch and expansion of a digital financial service may affect:

* ACCESS through increased availability of accounts
* USAGE through increased digital transactions
* GENDER through possible changes in gender gaps
* TRUST through changes in reliability and consumer experience

Therefore:

```text
Event
  ├── Impact Link → ACCESS
  ├── Impact Link → USAGE
  └── Impact Link → other relevant pillar
```

The event remains neutral, while the impact link captures the modeled relationship.

---

# 4. Enrichment Summary

The enriched dataset includes the following categories of additions:

### Additional observations

Additional observations were added where available to provide:

* Additional measurements of account ownership
* Digital payment adoption indicators
* Mobile money adoption indicators
* Financial infrastructure indicators
* Mobile connectivity and digital access indicators
* Gender-disaggregated or contextual indicators where relevant

### Additional events

Additional events were added to capture major developments that may influence financial inclusion, including:

* Digital financial service launches
* New market entrants
* Financial infrastructure developments
* Digital identity initiatives
* Regulatory and policy developments
* Interoperability developments
* Major financial inclusion milestones

### Additional impact links

Additional impact links were added to connect events to the specific indicators they may influence.

These links include:

* The affected pillar
* The affected indicator
* Expected direction of impact
* Expected impact magnitude
* Expected time lag
* Evidence basis

---

# 5. Record-Level Enrichment Log

## 5.1 Additional Observations

### Observation 1 — Account Ownership

**Record type:** `observation`
**Pillar:** `ACCESS`
**Indicator:** Account Ownership Rate
**Indicator code:** `ACC_OWNERSHIP`

**Source:** World Bank Global Findex

**Source URL:**
[https://www.worldbank.org/en/publication/globalfindex](https://www.worldbank.org/en/publication/globalfindex)

**Original text / figure:**

> Ethiopia's account ownership rate reached 49% in 2024.

**Confidence:** High

**Why this data is useful:**

Account ownership is the primary ACCESS outcome for this forecasting project. The observation provides the most recent demand-side baseline for forecasting future account ownership.

**Forecasting relevance:**

```text
ACC_OWNERSHIP
        ↓
Primary ACCESS target
```

---

### Observation 2 — Digital Payment Adoption

**Record type:** `observation`
**Pillar:** `USAGE`
**Indicator:** Made or Received Digital Payment
**Indicator code:** `USG_DIGITAL_PAYMENT`

**Source:** World Bank Global Findex

**Source URL:**
[https://www.worldbank.org/en/publication/globalfindex](https://www.worldbank.org/en/publication/globalfindex)

**Original text / figure:**

> Approximately 35% of Ethiopian adults made or received a digital payment in 2024.

**Confidence:** High

**Why this data is useful:**

Digital payment adoption is the primary USAGE outcome for this forecasting system. It provides a baseline for estimating the growth of financial service usage beyond simply having an account.

**Forecasting relevance:**

```text
Digital Payment Adoption
        ↓
Primary USAGE target
```

---

### Observation 3 — Mobile Money Account Ownership

**Record type:** `observation`
**Pillar:** `ACCESS`
**Indicator:** Mobile Money Account Ownership
**Indicator code:** `ACC_MOBILE_MONEY`

**Source:** World Bank Global Findex

**Source URL:**
[https://www.worldbank.org/en/publication/globalfindex](https://www.worldbank.org/en/publication/globalfindex)

**Original text / figure:**

> Approximately 9.45% of Ethiopian adults owned a mobile money account in 2024.

**Confidence:** High

**Why this data is useful:**

Mobile money accounts represent an important component of Ethiopia's digital financial ecosystem. The indicator can help distinguish the growth of mobile money access from broader account ownership.

It is particularly useful for understanding whether future account ownership growth is being driven by:

* Traditional bank accounts
* Mobile money accounts
* Expansion of digital financial services

---

### Observation 4 — Digital Payments for Receiving Wages

**Record type:** `observation`
**Pillar:** `USAGE`
**Indicator:** Account Used to Receive Wages
**Indicator code:** `USG_WAGE_PAYMENT`

**Source:** World Bank Global Findex

**Source URL:**
[https://www.worldbank.org/en/publication/globalfindex](https://www.worldbank.org/en/publication/globalfindex)

**Original text / figure:**

> Approximately 15% of Ethiopian adults used an account to receive wages.

**Confidence:** High

**Why this data is useful:**

Receiving wages digitally is an important pathway from account ownership to active account usage. It provides an additional usage-related indicator that may help explain why account ownership does not always translate into frequent digital transactions.

---

## 5.2 Additional Events

### Event 1 — M-Pesa Ethiopia Market Entry

**Record type:** `event`
**Category:** `market_entry`

**Pillar:** Intentionally left empty.

**Source:** Safaricom Ethiopia / M-Pesa market announcements

**Original text / figure:**

> M-Pesa entered the Ethiopian market in 2023.

**Confidence:** High

**Why this event is useful:**

The entry of a major mobile money operator represents increased competition and expansion of digital financial service availability.

The event may influence:

* ACCESS through increased availability of mobile money services
* USAGE through increased digital transaction options
* AFFORDABILITY through competition and pricing pressure

The event itself is not assigned to a pillar. Its potential effects are represented through separate impact links.

---

### Event 2 — Telebirr Launch

**Record type:** `event`
**Category:** `product_launch`

**Pillar:** Intentionally left empty.

**Source:** Ethio Telecom

**Original text / figure:**

> Telebirr launched in 2021 as a mobile money and digital financial service.

**Confidence:** High

**Why this event is useful:**

Telebirr represents one of the most significant digital financial service launches in Ethiopia. Its introduction provides a major structural event for analyzing changes in access and usage.

The event is expected to have multiple potential effects rather than being assigned to only one pillar.

---

### Event 3 — Fayda Digital ID Expansion

**Record type:** `event`
**Category:** `infrastructure`

**Pillar:** Intentionally left empty.

**Source:** National ID Program / Government of Ethiopia

**Original text / figure:**

> Ethiopia's Fayda digital ID program is being developed as a national digital identification infrastructure.

**Confidence:** Medium

**Why this event is useful:**

Digital identity infrastructure can reduce barriers to account opening and customer verification.

Potential mechanisms include:

* Easier customer identification
* Reduced onboarding friction
* Improved KYC processes
* Increased ability to access formal financial services

---

### Event 4 — EthSwitch Interoperability Expansion

**Record type:** `event`
**Category:** `infrastructure`

**Pillar:** Intentionally left empty.

**Source:** EthSwitch

**Original text / figure:**

> Ethiopia's national payment infrastructure has expanded interoperability between financial service providers.

**Confidence:** Medium

**Why this event is useful:**

Interoperability may increase the usefulness of digital accounts by allowing users to transact across different financial service providers.

This is particularly relevant to the USAGE pillar.

---

### Event 5 — National Financial Inclusion Strategy II

**Record type:** `event`
**Category:** `policy`

**Pillar:** Intentionally left empty.

**Source:** National Bank of Ethiopia

**Original text / figure:**

> Ethiopia's National Financial Inclusion Strategy provides a policy framework for expanding financial inclusion.

**Confidence:** High

**Why this event is useful:**

Policy frameworks can influence financial inclusion through:

* Regulatory reforms
* Institutional coordination
* Digital finance development
* Financial infrastructure investment
* Consumer protection

The policy is modeled through impact links rather than being directly assigned to ACCESS or USAGE.

---

# 6. Additional Impact Links

The impact links connect events to the indicators they may affect.

## Impact Link 1 — Telebirr → Account Ownership

**Parent event:** Telebirr Launch
**Pillar:** `ACCESS`
**Related indicator:** `ACC_OWNERSHIP`
**Relationship type:** `direct`
**Impact direction:** `increase`
**Impact magnitude:** `high`
**Lag:** 12 months
**Evidence basis:** `empirical`

### Rationale

The introduction and rapid expansion of a widely available mobile financial service can increase the number of adults with access to formal financial accounts.

---

## Impact Link 2 — Telebirr → Digital Payment Adoption

**Parent event:** Telebirr Launch
**Pillar:** `USAGE`
**Related indicator:** `USG_DIGITAL_PAYMENT`
**Relationship type:** `direct`
**Impact direction:** `increase`
**Impact magnitude:** `high`
**Lag:** 6 months
**Evidence basis:** `empirical`

### Rationale

Mobile money services provide users with the ability to send, receive, and make digital payments.

---

## Impact Link 3 — M-Pesa Entry → Account Ownership

**Parent event:** M-Pesa Market Entry
**Pillar:** `ACCESS`
**Related indicator:** `ACC_OWNERSHIP`
**Relationship type:** `direct`
**Impact direction:** `increase`
**Impact magnitude:** `medium`
**Lag:** 12 months
**Evidence basis:** `theoretical`

### Rationale

The entry of a new mobile money provider increases the number of available financial service providers and may encourage new users to enter the formal financial system.

---

## Impact Link 4 — M-Pesa Entry → Digital Payment Adoption

**Parent event:** M-Pesa Market Entry
**Pillar:** `USAGE`
**Related indicator:** `USG_DIGITAL_PAYMENT`
**Relationship type:** `direct`
**Impact direction:** `increase`
**Impact magnitude:** `medium`
**Lag:** 6 months
**Evidence basis:** `theoretical`

### Rationale

Additional competition may increase digital payment adoption by expanding product availability and encouraging innovation.

---

## Impact Link 5 — Digital ID Expansion → Account Ownership

**Parent event:** Fayda Digital ID Expansion
**Pillar:** `ACCESS`
**Related indicator:** `ACC_OWNERSHIP`
**Relationship type:** `enabling`
**Impact direction:** `increase`
**Impact magnitude:** `medium`
**Lag:** 24 months
**Evidence basis:** `literature`

### Rationale

Digital identity infrastructure can reduce identity and KYC barriers to financial account opening.

---

## Impact Link 6 — Interoperability Expansion → Digital Payment Adoption

**Parent event:** EthSwitch Interoperability Expansion
**Pillar:** `USAGE`
**Related indicator:** `USG_DIGITAL_PAYMENT`
**Relationship type:** `enabling`
**Impact direction:** `increase`
**Impact magnitude:** `medium`
**Lag:** 12 months
**Evidence basis:** `theoretical`

### Rationale

Interoperability increases the usefulness of digital financial services by reducing restrictions between providers.

---

## Impact Link 7 — NFIS-II → Account Ownership

**Parent event:** National Financial Inclusion Strategy II
**Pillar:** `ACCESS`
**Related indicator:** `ACC_OWNERSHIP`
**Relationship type:** `enabling`
**Impact direction:** `increase`
**Impact magnitude:** `medium`
**Lag:** 24 months
**Evidence basis:** `expert`

### Rationale

National strategies can create coordinated policy and institutional support for expanding financial access.

---

## Impact Link 8 — NFIS-II → Digital Payment Adoption

**Parent event:** National Financial Inclusion Strategy II
**Pillar:** `USAGE`
**Related indicator:** `USG_DIGITAL_PAYMENT`
**Relationship type:** `enabling`
**Impact direction:** `increase`
**Impact magnitude:** `medium`
**Lag:** 24 months
**Evidence basis:** `expert`

### Rationale

A coordinated financial inclusion strategy may support digital payment adoption through regulatory reforms, infrastructure investments, and market development.

---

# 7. Confidence Assessment

Confidence was assigned according to the following principles:

| Confidence | Meaning                                                                                 |
| ---------- | --------------------------------------------------------------------------------------- |
| High       | Data obtained from an official primary source or directly verified official publication |
| Medium     | Secondary source or information requiring cross-reference                               |
| Low        | Single unverified source                                                                |
| Estimated  | Derived, interpolated, or modeled value                                                 |

Demand-side indicators from the World Bank Global Findex were assigned high confidence because they originate from a primary international survey dataset.

Event impact relationships were assigned confidence based on the available evidence. These relationships represent modeled hypotheses rather than proven causal effects.

---

# 8. Limitations of the Enrichment

The enrichment dataset should not be interpreted as proving that individual events caused changes in financial inclusion.

Several limitations apply:

1. Global Findex observations are available only at periodic survey intervals.
2. The 2025–2027 forecast period contains fewer direct demand-side observations than earlier periods.
3. Several events overlap in time, making causal attribution difficult.
4. Multiple events may affect the same indicator simultaneously.
5. Operator-reported user counts may not be directly comparable to Global Findex account ownership because they may represent registered users rather than unique active adults.
6. Impact magnitude and lag values are modeled assumptions and should be validated as additional historical data become available.
7. The dataset combines demand-side survey data, supply-side operator data, regulatory information, and modeled relationships. These sources measure different aspects of financial inclusion.

---

# 9. Recommended Use in Forecasting

The enriched dataset should be used as follows:

### ACCESS forecasting

Primary target:

```text
ACC_OWNERSHIP
```

Potential explanatory variables:

* Mobile money account ownership
* Digital identity infrastructure
* Market entry
* Product launches
* Financial inclusion policies
* Agent and infrastructure expansion

### USAGE forecasting

Primary target:

```text
USG_DIGITAL_PAYMENT
```

Potential explanatory variables:

* Digital payment adoption
* Mobile money usage
* Interoperability
* Market competition
* Digital financial product launches
* Digital infrastructure
* Wage payment digitization

---

## Final Dataset Outputs

The enrichment process produces:

```text
ethiopia_fi_unified_data.xlsx
        │
        ├── Data
        │     ├── Original observations
        │     ├── Original events
        │     ├── Original targets
        │     └── Added enrichment records
        │
        └── Impact_sheet
              ├── Original impact links
              └── Added impact relationships
```

The enriched workbook is saved as:

```text
../data/processed/ethiopia_fi_enriched.xlsx
```

This enriched dataset is intended to be used as the input for subsequent exploratory analysis, feature engineering, modeling, and forecasting tasks.
