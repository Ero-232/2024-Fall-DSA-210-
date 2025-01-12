# 2024-Fall-DSA-210 Project: Personal Expense Analysis

## Description
This repository contains the code and data for my 2024 Fall Semester's DSA 210 project. The aim of this project is to analyze my personal expenses from October 1st to December 30th, identify patterns, and evaluate transaction behaviors to uncover correlations among parameters such as time, amount, and transaction category.

---

## Table of Contents
1. [Motivation](#motivation)
2. [Data Source](#data-source)
3. [Data Preprocessing](#data-preprocessing)
4. [Tools Used](#tools-used)
5. [Analysis and Visualizations](#analysis-and-visualizations)
    - [Transaction Frequency Analysis](#transaction-frequency-analysis)
    - [Time-Based Patterns](#time-based-patterns)
    - [Top Expense Categories](#top-expense-categories)
    - [3-Month Trend Analysis](#3-month-trend-analysis)
    - [Statistical Tests](#statistical-tests)
6. [Findings](#findings)
7. [Limitations](#limitations)
8. [Future Work](#future-work)

---

## Motivation
The primary goal of this project is to better understand my spending habits by analyzing my bank account transactions. This includes exploring:

- When transactions occur most frequently.
- Which categories dominate my spending.
- How my expenses change over time.
- Insights that can help optimize my financial habits.

---

## Data Source
- **Dataset:** The dataset was exported from Akbank's mobile application in CSV format.
- **Data Masking:** Personal information such as current balances and income transactions were removed using the `nobalance.py` script to ensure privacy.

The cleaned dataset includes the following key fields:
- **DateTime:** Date and time of the transaction.
- **TransactionAmount:** The amount of the transaction.
- **Description:** The transaction category or place.

---

## Data Preprocessing
To prepare the dataset for analysis:
1. Converted date and time strings to `datetime` objects for easier manipulation.
2. Parsed and standardized transaction amounts, removing non-numeric characters and formatting inconsistencies.
3. Dropped unused or irrelevant columns (e.g., raw balance information).
4. Extracted additional features such as:
    - Day of the week.
    - Hour of the day.
    - Monthly trends.

---

## Tools Used
The project relies on the following tools and libraries:

- **Python:** Core programming language for data analysis.
- **Pandas:** For data cleaning, structuring, and manipulation.
- **NumPy:** For numerical operations and calculations.
- **Matplotlib & Seaborn:** For creating static visualizations.
- **Scipy:** For conducting statistical tests.
- **Jupyter Notebook:** For documentation and interactive exploration.

---

## Analysis and Visualizations

### Transaction Frequency Analysis
- **Day of the Week:** A bar chart visualizes the distribution of transaction counts across the days of the week.
- **Hourly Activity:** Another bar chart illustrates the number of transactions for each hour of the day.

### Time-Based Patterns
- **Heatmap:** A heatmap shows the intersection of days of the week and hours of the day, highlighting peak transaction times.
- **KDE Plot:** A density plot visualizes transaction amounts by the time of day, offering insights into high-value transactions.

### Top Expense Categories
- **Top Places:** A bar chart highlights the top 10 transaction categories or locations based on frequency.

### 3-Month Trend Analysis
- **Daily Counts:** A line chart displays transaction counts over the last three months.
- **Regression Analysis:** A linear regression model evaluates whether transaction frequency is trending up or down over this period.

### Statistical Tests
- **T-Test:** A two-sample t-test compares transaction amounts between morning (before 12 PM) and evening (after 12 PM) hours to determine if spending behavior varies significantly by time.

---

## Findings
1. **Transaction Patterns:**
   - Transactions peak during specific hours of the day and days of the week.
   - High-frequency activity aligns with typical work or leisure hours.

2. **Spending Habits:**
   - Certain categories or merchants dominate transaction counts.
   - No significant differences in transaction amounts based on the time of day.

3. **3-Month Trends:**
   - Transaction frequency shows a stable or slightly increasing trend.

---

## Limitations
### Data Limitations
- **Privacy Concerns:** Some data fields were excluded to maintain personal privacy.
- **Sample Size:** The dataset covers only a 3-month period, limiting the scope for long-term trend analysis.

### Methodological Limitations
- **Subjectivity in Categorization:** Transaction descriptions may not accurately reflect spending categories.
- **Lack of Contextual Data:** No information about transaction intent or external factors affecting spending.

---

## Future Work
1. **Longitudinal Analysis:** Expand the dataset to cover a full year or multiple years to observe long-term trends.
2. **Advanced Techniques:** Incorporate machine learning models to predict future spending patterns or identify anomalies.
3. **Interactive Visualizations:** Build a web-based dashboard for dynamic exploration of the dataset.
4. **Detailed Categorization:** Implement NLP techniques to better classify transaction descriptions into meaningful categories.

---

## Repository Structure
- **`analysis.py`:** Main script for data cleaning, analysis, and visualization.
- **`nobalance.py`:** Script for masking sensitive data.
- **`data_nobalance.csv`:** Cleaned dataset used in the analysis.
- **`Figure_X.png`:** Visualizations generated by the analysis script.
- **`README.md`:** Project documentation (this file).

---

Script execution and visualization outputs are included in this repository for reference.

