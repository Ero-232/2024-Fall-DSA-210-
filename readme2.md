# Project: Personal Expense Analysis for 2024-Fall-DSA-210

## Overview
The code and data for my DSA 210 project from the fall semester of 2024 are in this repository. In order to find correlations between variables like time, quantity, and transaction category, the project's goal is to examine my personal expenses from October 1st to December 30th, look for trends, and assess transaction behaviors.

---

## Contents Table
1. [Inspiration](#inspiration)
2. [Source of Data](#data-source)
3. [Preprocessing Data](#preprocessing-data)
4. [Used Tools](#tools-used)
5. [Visualizations and Analysis](#visualizations-and-analysis)
    [Analysis of Transaction Frequencies](#transaction-frequency-analysis)
    [Patterns Based on Time](#patterns-based-on-time)
    [Highest Cost Types](#highest-cost-categories)
    [3-Month Trend Analysis](#3-month-trend-analysis)
    [Tests of Statistics](#tests-statistical)
6. [Results](#findings)
7. [Restrictions](#restrictions)
8. [Work for the Future](#future-work)

---

## Inspiration
This project's main objective is to examine my bank account activities in order to have a better understanding of my spending patterns. This involves investigating:

When do transactions happen most often?
Which categories are most prevalent?
When do transactions happen most often?
Which areas account for the majority of my expenditures?
How my spending evolves over time.
- Knowledge that will help me improve my financial practices.

---

**Dataset:** is the data source. The dataset was exported in CSV format using the Akbank mobile application.
**Data Masking:** To protect privacy, personal data including income transactions and current balances were eliminated using the `nobalance.py` script.

The following crucial fields are present in the cleaned dataset:
- **DateTime:** The transaction's date and time.
- **TransactionAmount:** The transaction's total value.
**Description:** The type of transaction or location.

---

## Preparing Data
To get the dataset ready for examination:
1. To facilitate handling, date and time strings were converted to `datetime` objects.
2. Transaction amounts were parsed and standardized, eliminating formatting errors and non-numeric characters.
3. Removed unnecessary or superfluous columns (raw balance data, for example).
4. Extra features like the day of the week were extracted.
    The time of day.
    Monthly patterns.

---

## Equipment Used
The following libraries and tools are necessary for the project:

One essential programming language for data analysis is Python.
**Pandas:** To clean, organize, and manipulate data.
- **NumPy:** For computations and numerical operations.
To create static visualizations, use Seaborn with Matplotlib.
To do statistical tests, use Scipy.
**Jupyter Notebook:** For interactive exploration and documentation.

---

## Visualizations and Analysis

### Transaction Frequency Analysis **Day of the Week:** The distribution of transaction counts by day of the week is shown in a bar chart.
**Hourly Activity:** The quantity of transactions for each hour is shown in another bar chart.

This is an hourly activity. The quantity of transactions for every hour of the day is depicted in another bar chart.

### Patterns Based on Time
**Heatmap:** A heatmap highlights periods of high transaction volume by displaying the intersection of the hours of the day and the days of the week.
**KDE Plot:** A density plot provides information about high-value transactions by visualizing transaction quantities by time of day.

### Top Cost Types- **Top Locations:** The top ten transaction categories or locations are displayed in a bar chart according to frequency.

### Trend Analysis for Three Months: **Daily Counts:** The number of transactions during the previous three months is shown in a line chart.
Regression analysis: The trend of transaction frequency over this time period is assessed using a linear regression model.

### Tests of Statistics: **T-Test:** To ascertain whether spending patterns differ significantly by time, a two-sample t-test analyzes transaction quantities between morning (before 12 PM) and evening (after 12 PM) hours.

---

## Results 1. **Transaction Trends:** - Transactions are at their highest on particular days and hours of the day.
   High-frequency activity coincides with regular work or playtime.

2. **Spending Patterns:** - Transaction counts are dominated by particular merchants or categories.
   There aren't any notable variations in transaction amounts according to the time of day.

3. **3-Month Trends:** - The frequency of transactions exhibits a steady or marginally rising trend.

---

## Restrictions ### Data Restrictions - **Privacy Concerns:** To protect individual privacy, certain data fields were eliminated.
The sample size is as follows: Because the dataset only spans three months, it is not suitable for long-term trend analysis.

### Methodological Restrictions: **Categorization Subjectivity:** Transaction descriptions might not be a true representation of spending categories.
- **Lack of Contextual Data:** No details regarding the purpose of the transaction or outside variables influencing expenditure.

---

## Upcoming Projects
1. **Longitudinal Analysis:** To see long-term patterns, extend the dataset to span one or more years.
2. **Advanced Techniques:** Use machine learning algorithms to spot irregularities or forecast future expenditure trends.
3. **Interactive Visualizations:** Create a dashboard that can be accessed online for dynamic dataset exploration.
4. **Detailed Categorization:** Use natural language processing (NLP) methods to more effectively group transaction descriptions into relevant groups.

---

## Structure of the Repository
The primary script for cleaning, analyzing, and visualizing data is **`analysis.py`:**.
- **`nobalance.py`:** A script to conceal private information.
The cleaned dataset that was used for the analysis is **`data_nobalance.csv`:**.
- **`Figure_X.png`:** The analysis script's visualizations.
This file, **`README.md`:**, is the project documentation.
