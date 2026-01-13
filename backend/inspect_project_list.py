
import pandas as pd
import os

file_path = "SRIC project list.xlsx"
try:
    df = pd.read_excel(file_path, nrows=5)
    print("Columns:", df.columns.tolist())
    print("\nFirst 2 rows:")
    print(df.head(2).to_string())
except Exception as e:
    print(f"Error reading file: {e}")
