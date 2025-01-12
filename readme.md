# Project: Personal Expense Analysis for 2024-Fall-DSA-210

## Overview
The code and data for my DSA 210 project from the fall semester of 2024 are in this repository. The project's goal is to examine my personal expenses from October 1st to December 30th, look for trends, and assess transaction behaviors to find correlations between variables like time, quantity, and transaction category.

---

## Contents Table
1. [Inspiration](#inspiration)
2. [Source of Data](#data-source)
3. [Preprocessing Data](#preparing-data)
4. [Used Tools](#equipment-used)
5. [Visualizations and Analysis](#visualizations-and-analysis)  
    - [Analysis of Transaction Frequencies](#transaction-frequency-analysis)  
    - [Patterns Based on Time](#patterns-based-on-time)  
    - [Highest Cost Types](#top-cost-types)  
    - [3-Month Trend Analysis](#trend-analysis-for-three-months)  
    - [Tests of Statistics](#tests-of-statistics)  
6. [Results](#results)  
7. [Restrictions](#restrictions)  
8. [Work for the Future](#upcoming-projects)  

---

## Inspiration
This project's main objective is to examine my bank account activities in order to have a better understanding of my spending patterns. This involves investigating:  
- When do transactions happen most often?  
- Which categories are most prevalent?  
- Which areas account for the majority of my expenditures?  
- How my spending evolves over time.

The knowledge gained will help improve my financial practices.

---

## Source of Data
**Dataset:** The data source is a CSV file exported using the Akbank mobile application.  
**Data Masking:** To protect privacy, personal data including income transactions and current balances were eliminated using the `nobalance.py` script.

The following crucial fields are present in the cleaned dataset:  
- **DateTime:** The transaction's date and time.  
- **TransactionAmount:** The transaction's total value.  
- **Description:** The type of transaction or location.

---

## Preparing Data
To get the dataset ready for examination:  
1. Date and time strings were converted to `datetime` objects to facilitate handling.  
2. Transaction amounts were parsed and standardized, eliminating formatting errors and non-numeric characters.  
3. Removed unnecessary or superfluous columns (e.g., raw balance data).  
4. Extracted extra features such as:  
    - Day of the week  
    - Time of day  
    - Monthly patterns  

---

## Equipment Used
The following libraries and tools are necessary for the project:  
- **Python:** One essential programming language for data analysis.  
- **Pandas:** To clean, organize, and manipulate data.  
- **NumPy:** For computations and numerical operations.  
- **Matplotlib and Seaborn:** To create static visualizations.  
- **Scipy:** To perform statistical tests.  
- **Jupyter Notebook:** For interactive exploration and documentation.

---

## Visualizations and Analysis

### Transaction Frequency Analysis
- **Day of the Week:** The distribution of transaction counts by day of the week is shown in a bar chart.  
- **Hourly Activity:** The quantity of transactions for each hour of the day is depicted in another bar chart.

### Patterns Based on Time
- **Heatmap:** A heatmap highlights periods of high transaction volume by displaying the intersection of the hours of the day and the days of the week.  
- **KDE Plot:** A density plot visualizes transaction quantities by time of day, providing insights about high-value transactions.

### Top Cost Types
- **Top Locations:** The top ten transaction categories or locations are displayed in a bar chart according to frequency.

### Trend Analysis for Three Months
- **Daily Counts:** The number of transactions during the previous three months is shown in a line chart.  
- **Regression Analysis:** The trend of transaction frequency over this time period is assessed using a linear regression model.

### Tests of Statistics
- **T-Test:** A two-sample t-test analyzes transaction quantities between morning (before 12 PM) and evening (after 12 PM) hours to ascertain whether spending patterns differ significantly by time.

---

## Results

1. **Transaction Trends:**  
   - Transactions are at their highest on particular days and hours of the day.  
   - High-frequency activity coincides with regular work or playtime.  

2. **Spending Patterns:**  
   - Transaction counts are dominated by particular merchants or categories.  
   - There aren't any notable variations in transaction amounts according to the time of day.  

3. **Month Trends:**  
   - The frequency of transactions exhibits a steady or marginally rising trend.  

---

## Restrictions

### Data Restrictions
- **Privacy Concerns:** To protect individual privacy, certain data fields were eliminated.  
- **Sample Size:** Because the dataset only spans three months, it is not suitable for long-term trend analysis.

### Methodological Restrictions
- **Categorization Subjectivity:** Transaction descriptions might not be a true representation of spending categories.  
- **Lack of Contextual Data:** No details regarding the purpose of the transaction or outside variables influencing expenditure.

---

## Upcoming Projects

1. **Longitudinal Analysis:** Extend the dataset to span one or more years to see long-term patterns.  
2. **Advanced Techniques:** Use machine learning algorithms to spot irregularities or forecast future expenditure trends.  
3. **Interactive Visualizations:** Create a dashboard that can be accessed online for dynamic dataset exploration.  
4. **Detailed Categorization:** Use natural language processing (NLP) methods to more effectively group transaction descriptions into relevant groups.  

---

## Structure of the Repository

- **`analysis.py`:** The primary script for cleaning, analyzing, and visualizing data.  
- **`nobalance.py`:** A script to conceal private information.  
- **`data_nobalance.csv`:** The cleaned dataset used for the analysis.  
- **`Figure_X.png`:** The analysis script's visualizations.  
- **`README.md`:** This file, containing project documentation.
