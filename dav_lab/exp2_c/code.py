# Experiment 2C: Reading Data from Text Files, Excel, and the Web

import pandas as pd

# ─── Read data from CSV (text file) ───────────────────────────────────────────
text_df = pd.read_csv('Google_data.csv')

# ─── Read data from Excel file ────────────────────────────────────────────────
excel_df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# ─── Read data from web-based source (CSV from URL) ──────────────────────────
web_df = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')

# ─── Display first few rows of each dataset ───────────────────────────────────
print("--- CSV Data (first 5 rows) ---")
print(text_df.head())

print("\n--- Excel Data (first 5 rows) ---")
print(excel_df.head())

print("\n--- Web Data (first 5 rows) ---")
print(web_df.head())

# ─── Handle missing values ────────────────────────────────────────────────────
text_df.ffill(inplace=True)       # forward fill for CSV data
excel_df.bfill(inplace=True)      # backward fill for Excel data
web_df.dropna(inplace=True)       # drop rows with nulls for web data

# ─── Save processed data ──────────────────────────────────────────────────────
text_df.to_csv('processed_text.csv', index=False)
excel_df.to_excel('processed_excel.xlsx', index=False)

print("\nData processing complete. Files saved.")
