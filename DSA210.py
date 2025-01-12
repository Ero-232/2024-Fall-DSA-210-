"""
analysis.py

Author: Your Name
Date: 2025-01-12

Description:
------------
Extended script to read a CSV of expense transactions, parse data, and create
several data visualizations & statistical tests. This version includes:
  - (1) Basic load, parse, cleaning
  - (2) Time-based aggregations & plots
  - (3) Heatmap
  - (4) Additional (6) daily transactions over 3-month window w/ regression slope
  - (5) Additional (7) transaction distribution by place
  - (6) Example T-test to compare two groups
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Optional: If you'd like an example T-test
from scipy.stats import ttest_ind

# ------------------------------------------------------------------------------
# 1. READ THE CSV DATA
# ------------------------------------------------------------------------------
# Adjust filename/path & parameters to match your CSV
df = pd.read_csv("data.csv", sep=";", encoding="ansi", header=None)

# Example column renaming:
# Check how many columns your data has with print(df.shape[1])
df.columns = ["DateTimeStr", "TransactionAmountStr", "BalanceStr", "Description", "ExtraColumn"]  
# If your file has only 4 columns, remove the "ExtraColumn" above or rename as needed.

# ------------------------------------------------------------------------------
# 2. PARSE/CLEAN THE DATA
# ------------------------------------------------------------------------------
# Parsing datetime (example: 2024-12-31-07.44.51.466893)
date_format = "%Y-%m-%d-%H.%M.%S.%f"
df["DateTime"] = pd.to_datetime(df["DateTimeStr"], format=date_format, errors="coerce")
df.drop(columns=["DateTimeStr"], inplace=True)

# Convert numeric amounts
def parse_tl_amount(x):
    # Remove 'TL' and extra spaces
    if isinstance(x, str):
        x = x.replace("TL", "").strip().replace(",", ".").replace("   ", "").replace(" ", "")
        if "." not in x:
            if len(x) > 2:
                x = x[:-2] + "." + x[-2:]
    else:
        return np.nan
    try:
        return float(x)
    except ValueError:
        return np.nan

df["TransactionAmount"] = df["TransactionAmountStr"].apply(parse_tl_amount)
df["Balance"] = df["BalanceStr"].apply(parse_tl_amount)

# Drop original columns if no longer needed
df.drop(columns=["TransactionAmountStr", "BalanceStr"], inplace=True)

# ------------------------------------------------------------------------------
# 3. EXTRACT TIME/DATE FEATURES
# ------------------------------------------------------------------------------
df["Year"] = df["DateTime"].dt.year
df["Month"] = df["DateTime"].dt.month_name()
df["DayOfWeek"] = df["DateTime"].dt.day_name()  # Monday, Tuesday...
df["Hour"] = df["DateTime"].dt.hour

# ------------------------------------------------------------------------------
# 4. VISUALIZATIONS (Existing Examples)
# ------------------------------------------------------------------------------

# (A) Transactions Count by Day of Week
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="DayOfWeek", 
              order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], 
              palette="Set2")
plt.title("Transactions Count by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Count of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# (B) Transactions Count by Hour
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="Hour", palette="Set3")
plt.title("Transactions Count by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Count of Transactions")
plt.tight_layout()
plt.show()

# (C) Histogram of Transaction Amounts
plt.figure(figsize=(8, 4))
sns.histplot(df["TransactionAmount"], kde=True, color="purple", bins=30)
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# (D) Heatmap: DayOfWeek vs Hour (count of transactions)
pivot_data = df.pivot_table(index="DayOfWeek", columns="Hour", values="TransactionAmount", aggfunc="count", fill_value=0)
day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
pivot_data = pivot_data.reindex(day_order)

plt.figure(figsize=(12, 5))
sns.heatmap(pivot_data, cmap="Reds", annot=True, fmt="d")
plt.title("Heatmap of # of Transactions by Day of Week and Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Day of Week")
plt.tight_layout()
plt.show()

# (E) KDE Plot: Hour vs Transaction Amount
plt.figure(figsize=(8, 4))
sns.kdeplot(x=df["Hour"], y=df["TransactionAmount"], fill=True, cmap="mako")
plt.title("Density Plot of Transaction Amount vs Hour")
plt.xlabel("Hour")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# 5. ADDITIONAL VISUALIZATIONS
# ------------------------------------------------------------------------------

# (6) Plot # of Transactions Per Day in a 3-Month Range + "Beta" (Slope) Interpretation
# ------------------------------------------------------------------------------
# Let's pick a 3-month window. For example, the last 3 months in the data.
# We'll find the max date, then define a "3 months prior" cutoff:
if not df["DateTime"].isna().all():
    max_date = df["DateTime"].max()
    three_months_ago = max_date - pd.DateOffset(months=3)

    # Filter data for last 3 months
    mask_3mo = (df["DateTime"] >= three_months_ago) & (df["DateTime"] <= max_date)
    df_3mo = df.loc[mask_3mo].copy()

    # Group by date (ignoring time)
    daily_counts_3mo = df_3mo.groupby(df_3mo["DateTime"].dt.date)["TransactionAmount"].count()
    daily_counts_3mo = daily_counts_3mo.reset_index()
    daily_counts_3mo.columns = ["Date", "TransactionCount"]

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(daily_counts_3mo["Date"], daily_counts_3mo["TransactionCount"], marker='o', color='blue')
    plt.title("Daily Transaction Count (Last 3 Months)")
    plt.xlabel("Date")
    plt.ylabel("Count of Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Regression to find the slope (Beta) to see if there's an upward/downward trend
    # We'll do a simple linear regression: 
    #   y = a + bX, where X is an integer day index, y = TransactionCount
    daily_counts_3mo = daily_counts_3mo.sort_values("Date")
    # Create an index from 0..N-1
    daily_counts_3mo["DayIndex"] = range(len(daily_counts_3mo))

    # Fit a simple regression using numpy polyfit
    x = daily_counts_3mo["DayIndex"].values
    y = daily_counts_3mo["TransactionCount"].values
    b, a = np.polyfit(x, y, 1)  # slope = b, intercept = a
    # b is the "Beta" slope
    print(f"\n[6] 3-Month Daily Transaction Trend:")
    print(f"    - Found slope (Beta): {b:.3f}")
    print(f"    - Interpretation: If Beta>0, transactions are generally increasing over time, else decreasing.")

else:
    print("No valid DateTime data to do 3-month analysis.")


# (7) Transaction Distribution by "Place"
# ------------------------------------------------------------------------------
# We'll assume "Description" indicates the place or merchant. Let's do a top 10 bar chart.
plt.figure(figsize=(8, 4))

# Count how many transactions per place
place_counts = df["Description"].value_counts().nlargest(10)  # top 10
sns.barplot(x=place_counts.values, y=place_counts.index, palette="Blues_r")
plt.title("Top 10 Transaction Places by Count")
plt.xlabel("Count of Transactions")
plt.ylabel("Place (from Description)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# 6. EXAMPLE STATISTICAL TEST
# ------------------------------------------------------------------------------
# We can do, for instance, a T-test comparing transaction amounts
# in the Morning (Hour < 12) vs. Evening (Hour >= 12).
morning_amounts = df.loc[df["Hour"] < 12, "TransactionAmount"].dropna()
evening_amounts = df.loc[df["Hour"] >= 12, "TransactionAmount"].dropna()

if len(morning_amounts) > 1 and len(evening_amounts) > 1:
    t_stat, p_val = ttest_ind(morning_amounts, evening_amounts, equal_var=False)
    print("\nT-Test: Morning vs. Evening Transaction Amounts")
    print(f"  T-statistic: {t_stat:.3f}")
    print(f"  p-value: {p_val:.6f}")
    if p_val < 0.05:
        print("  -> Statistically significant difference at alpha=0.05!")
    else:
        print("  -> No statistically significant difference at alpha=0.05.")
else:
    print("\nNot enough data to perform T-test for morning vs evening amounts.")

# ------------------------------------------------------------------------------
print("\nScript finished. Review the additional plots and printed results!")
