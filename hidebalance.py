import pandas as pd


input_file = "data.csv" #the one left was the original data file
output_file = "data_nobalance.csv" #the one here is the csv file i have upladed to repo, clean from confidential info

df = pd.read_csv(input_file, sep=";", encoding="ansi", header=None)

df.columns = ["DateTimeStr", "TransactionAmountStr", "BalanceStr", "Description", "Extra"]

df["BalanceStr"] = ""  # Empty the balance

df.to_csv(output_file, sep=";", index=False, header=False, na_rep="")

print(f"Modified CSV saved as: {output_file}")
