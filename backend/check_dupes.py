
import pandas as pd

file_path = "SRIC project list.xlsx"
df = pd.read_excel(file_path, sheet_name=1 if len(pd.ExcelFile(file_path).sheet_names)>1 else 0)
df.columns = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]

print("Total rows:", len(df))
print("Duplicate project codes:", df['user_proj_code'].duplicated().sum())

# Check for Nulls in mandatory fields
print("Null Titles:", df['project_title'].isnull().sum())
print("Null PIs:", df['pi_name'].isnull().sum())
