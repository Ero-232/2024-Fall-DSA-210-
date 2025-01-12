

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta


from scipy.stats import ttest_ind

df = pd.read_csv("data_nobalance.csv", sep=";", encoding="ansi", header=None)


df.columns = ["DateTimeStr", "TransactionAmountStr", "BalanceStr", "Description", "ExtraColumn"]  

date_format = "%Y-%m-%d-%H.%M.%S.%f"
df["DateTime"] = pd.to_datetime(df["DateTimeStr"], format=date_format, errors="coerce")
df.drop(columns=["DateTimeStr"], inplace=True)


def parse_tl_amount(x):
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


df.drop(columns=["TransactionAmountStr", "BalanceStr"], inplace=True)

df["Year"] = df["DateTime"].dt.year
df["Month"] = df["DateTime"].dt.month_name()
df["DayOfWeek"] = df["DateTime"].dt.day_name()  
df["Hour"] = df["DateTime"].dt.hour


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


plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="Hour", palette="Set3")
plt.title("Transactions Count by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Count of Transactions")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 4))
sns.histplot(df["TransactionAmount"], kde=True, color="purple", bins=30)
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


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


plt.figure(figsize=(8, 4))
sns.kdeplot(x=df["Hour"], y=df["TransactionAmount"], fill=True, cmap="mako")
plt.title("Density Plot of Transaction Amount vs Hour")
plt.xlabel("Hour")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.show()


if not df["DateTime"].isna().all():
    max_date = df["DateTime"].max()
    three_months_ago = max_date - pd.DateOffset(months=3)


    mask_3mo = (df["DateTime"] >= three_months_ago) & (df["DateTime"] <= max_date)
    df_3mo = df.loc[mask_3mo].copy()


    daily_counts_3mo = df_3mo.groupby(df_3mo["DateTime"].dt.date)["TransactionAmount"].count()
    daily_counts_3mo = daily_counts_3mo.reset_index()
    daily_counts_3mo.columns = ["Date", "TransactionCount"]


    plt.figure(figsize=(8, 4))
    plt.plot(daily_counts_3mo["Date"], daily_counts_3mo["TransactionCount"], marker='o', color='blue')
    plt.title("Daily Transaction Count (Last 3 Months)")
    plt.xlabel("Date")
    plt.ylabel("Count of Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    
    daily_counts_3mo = daily_counts_3mo.sort_values("Date")

    daily_counts_3mo["DayIndex"] = range(len(daily_counts_3mo))

   
    x = daily_counts_3mo["DayIndex"].values
    y = daily_counts_3mo["TransactionCount"].values
    b, a = np.polyfit(x, y, 1) 
    
    print(f"\n[6] 3-Month Daily Transaction Trend:")
    print(f"    - Found slope (Beta): {b:.3f}")
    print(f"    - Interpretation: If Beta>0, transactions are generally increasing over time, else decreasing.")

else:
    print("No valid DateTime data to do 3-month analysis.")



plt.figure(figsize=(8, 4))


place_counts = df["Description"].value_counts().nlargest(10)  # top 10
sns.barplot(x=place_counts.values, y=place_counts.index, palette="Blues_r")
plt.title("Top 10 Transaction Places by Count")
plt.xlabel("Count of Transactions")
plt.ylabel("Place (from Description)")
plt.tight_layout()
plt.show()


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


print("\nScript finished. Review the additional plots and printed results!")
