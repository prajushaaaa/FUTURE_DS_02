# Customer Retention & Churn Analysis Dashboard

## Project Overview

This project analyzes customer churn and retention patterns using the Telco Customer Churn dataset. The objective is to identify factors affecting customer retention, understand customer behavior, and provide business recommendations to reduce churn.

This project was completed as part of the Future Interns Data Science & Analytics Internship.

---

## Objectives

- Analyze customer churn trends.
- Calculate churn rate and retention metrics.
- Identify customer segments with higher churn.
- Understand customer tenure patterns.
- Generate business recommendations for improving retention.

---

## Tools Used

- Python
- Pandas
- Matplotlib
- Power BI
- CSV Dataset

---

## Dataset

Dataset: Telco Customer Churn Dataset

The dataset contains information about:

- Customer ID
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Internet Service
- Contract Type
- Monthly Charges
- Total Charges
- Churn Status

---

## Analysis Performed

### Data Cleaning
- Checked dataset structure.
- Verified missing values.
- Validated column formats.

### Customer Churn Analysis
- Total Customers
- Churned Customers
- Churn Rate
- Average Customer Tenure
- Contract Type Analysis
- Internet Service Analysis

### Power BI Dashboard
Created an interactive dashboard containing:

- KPI Cards
- Churn Rate Analysis
- Contract Type vs Churn
- Internet Service vs Churn
- Customer Distribution Charts
- Interactive Filters

---

## Key Insights

- Total Customers: 7043
- Churned Customers: 1869
- Churn Rate: 26.54%
- Average Customer Tenure: 32.37 Months
- Month-to-month contracts have the highest churn.
- Two-year contracts show the strongest retention.
- Fiber optic customers contribute significantly to churn.

---

## Business Recommendations

- Promote long-term contracts.
- Offer retention incentives for month-to-month customers.
- Improve support services for high-risk customers.
- Create loyalty programs for long-term subscribers.
- Investigate causes of churn among fiber optic users.

---

## Dashboard Preview

![Dashboard](images/dashboard.png)

---

## Project Structure

```
FUTURE_DS_02/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── src/
│   └── analysis.py
│
├── dashboard/
│   └── Customer_Retention_Dashboard.pbix
│
├── images/
│   └── dashboard.png
│
└── README.md
```

---

## How to Run

Install required libraries:

```bash
pip install pandas matplotlib
```

Run analysis:

```bash
python src/analysis.py
```

---

## Internship Task

Future Interns – Data Science & Analytics Internship

Task 2: Customer Retention & Churn Analysis

---

## Author

Prajusha Gangrade