import pandas as pd

# Step 1: Load the original CSV
input_file = "data.csv"  # Original file
output_file = "data_no_balance.csv"  # New file with the modified format

# Read the CSV file (ensure correct encoding and delimiter)
df = pd.read_csv(input_file, sep=";", encoding="ansi", header=None)

# Step 2: Assign column names for clarity (modify if your file structure differs)
df.columns = ["DateTimeStr", "TransactionAmountStr", "BalanceStr", "Description", "Extra"]

# Step 3: Remove the balance column by replacing it with an empty string
df["BalanceStr"] = ""  # Empty the BalanceStr column

# Step 4: Save the modified DataFrame to a new CSV file
# Include a double semicolon between TransactionAmountStr and BalanceStr
df.to_csv(output_file, sep=";", index=False, header=False, na_rep="")

print(f"Modified CSV saved as: {output_file}")
