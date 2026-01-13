
import pandas as pd

file_path = "SRIC project list.xlsx"
xl = pd.ExcelFile(file_path)
print("Sheets:", xl.sheet_names)
target_sheet = next((s for s in xl.sheet_names if "Active" in s), xl.sheet_names[1] if len(xl.sheet_names)>1 else xl.sheet_names[0])
print(f"Inspecting columns of: {target_sheet}")

df = pd.read_excel(file_path, sheet_name=target_sheet)
cols = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]
print("Normalized Columns:", cols)
