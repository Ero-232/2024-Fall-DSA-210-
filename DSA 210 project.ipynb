
# analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

def load_data(file_path):
    """
    Loads the CSV file with the specified encoding and
    returns a cleaned DataFrame.
    """
    # Because your data has lines with bank info that aren’t real rows,
    # you can try skipping them by specifying skiprows or skipfooter.
    # Adjust skiprows or skipfooter as necessary.
    try:
        df = pd.read_csv(file_path, 
                         encoding='latin-1',   # or 'cp1254' or 'ISO-8859-9', etc.
                         sep=';',             # your file seems to use ';'
                         skiprows=5           # if the first 5 lines are garbage
                        )
    except Exception as e:
        print("Error reading CSV:", e)
        return None
    
    # Print top rows to verify
    print("Raw Data (first 5 rows):")
    print(df.head(5))
    return df

if __name__ == "__main__":
    # Example usage:
    file_path = "data.csv"  # CSV file name
    df = load_data(file_path)
    

##############


def clean_data(df):
    """
    Clean and convert columns in the DataFrame to usable formats.
    """
    # Rename columns as you see them, for example:
    df.columns = ["Tarih", "Tutar", "Bakiye", "Aciklama"]
    
    # Remove trailing spaces or strange characters (like ' TL')
    # Example:  "500   00 TL" -> "500,00" or "500.00"
    df["Tutar"] = df["Tutar"].apply(lambda x: str(x).replace(" TL", "").replace("\t","").replace(",", "."))
    df["Bakiye"] = df["Bakiye"].apply(lambda x: str(x).replace(" TL", "").replace("\t","").replace(",", "."))

    # Convert Tutar and Bakiye to float
    # This step might need to handle negative signs or
    # a decimal sign that uses commas, etc.
    try:
        df["Tutar"] = df["Tutar"].astype(float)
        df["Bakiye"] = df["Bakiye"].astype(float)
    except ValueError:
        print("Could not convert Tutar or Bakiye to float. Please check the data format.")
    
    # Parse "Tarih" column as datetime
    # You might have a format like: 2024-12-31-07.44.51.466893
    # We'll try a flexible approach:
    try:
        df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y-%m-%d-%H.%M.%S.%f", errors="coerce")
    except ValueError:
        print("Date parsing issue. The format might need to be adjusted.")
    
    # Drop rows that could not be parsed (if needed)
    df.dropna(subset=["Tarih"], inplace=True)
    
    # Sort by date
    df.sort_values(by="Tarih", inplace=True)
    
    print("\nCleaned Data (first 5 rows):")
    print(df.head(5))
    
    return df

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)



####3

def enrich_data(df):
    """
    Add new columns such as 'DayOfWeek' and 'TimeOfDay' to analyze patterns.
    """
    df["DayOfWeek"] = df["Tarih"].dt.day_name()  # e.g. Monday, Tuesday, ...
    df["Hour"] = df["Tarih"].dt.hour           # 0-23
    
    # Define day segments (morning, noon, evening, night)
    conditions = [
        (df["Hour"] >= 5) & (df["Hour"] < 12),
        (df["Hour"] >= 12) & (df["Hour"] < 17),
        (df["Hour"] >= 17) & (df["Hour"] < 22),
        (df["Hour"] >= 22) | (df["Hour"] < 5)
    ]
    day_parts = ["Morning", "Noon", "Evening", "Night"]
    df["TimeOfDay"] = np.select(conditions, day_parts)
    
    print("\nEnriched Data (first 5 rows):")
    print(df[["Tarih", "DayOfWeek", "Hour", "TimeOfDay"]].head(5))
    
    return df

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        df = enrich_data(df)



####4


def analyze_transactions(df):
    """
    Prints some statistics about transactions by day of week, time of day, etc.
    """
    print("\nTransaction count by Day of Week:")
    print(df["DayOfWeek"].value_counts())
    
    print("\nTransaction count by Time of Day:")
    print(df["TimeOfDay"].value_counts())

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        df = enrich_data(df)
        analyze_transactions(df)




#### 5 1 

def plot_day_of_week(df):
    """
    Creates a bar plot of transaction counts by day of the week.
    """
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="DayOfWeek", order=[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ], palette="rocket")
    plt.title("Number of Transactions by Day of the Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        df = enrich_data(df)
        plot_day_of_week(df)








#### 5 2



def plot_time_of_day_distribution(df):
    """
    Creates a pie chart showing the distribution of transactions across times of day.
    """
    time_counts = df["TimeOfDay"].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(time_counts, labels=time_counts.index, autopct="%1.1f%%", startangle=140)
    plt.title("Distribution of Transactions by Time of Day")
    plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        df = enrich_data(df)
        plot_time_of_day_distribution(df)



##### 5 3


def plot_tarih_vs_tutar_heatmap(df):
    """
    Creates a heatmap / 2D histogram of date vs. amount.
    Because 'Tarih' is a date, we might transform to numeric or just group by day.
    """
    # Example: group by date only (no time) and sum the Tutar
    df["DateOnly"] = df["Tarih"].dt.date
    pivot_df = df.groupby("DateOnly")["Tutar"].sum().reset_index()

    # For a heatmap, we typically need a matrix. Another approach:
    # We'll do a lineplot or barplot instead. If you really want a
    # "heatmap", you can group by day of week vs. hour, for example:
    pivot_day_hour = df.groupby(["DayOfWeek", "Hour"])["Tutar"].sum().unstack(fill_value=0)
    
    plt.figure(figsize=(10,6))
    sns.heatmap(pivot_day_hour, cmap="Blues", annot=True, fmt=".2f")
    plt.title("Heatmap of Sum of Transactions by Day of Week & Hour")
    plt.ylabel("Day of Week")
    plt.xlabel("Hour of Day")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        df = enrich_data(df)
        plot_tarih_vs_tutar_heatmap(df)
