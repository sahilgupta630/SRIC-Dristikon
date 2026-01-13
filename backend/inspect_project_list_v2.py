
import pandas as pd

file_path = "SRIC project list.xlsx"
try:
    xl = pd.ExcelFile(file_path)
    print("Sheet names:", xl.sheet_names)
    
    # Try reading the first sheet again, but looking for the header
    df = pd.read_excel(file_path, sheet_name=0)
    print("\nFirst 5 rows (raw):")
    print(df.head(5).to_string())
    
    # If the second sheet looks better, read that too
    if len(xl.sheet_names) > 1:
        print(f"\nSecond sheet ({xl.sheet_names[1]}):")
        df2 = pd.read_excel(file_path, sheet_name=1, nrows=5)
        print(df2.head(5).to_string())
except Exception as e:
    print(f"Error: {e}")
