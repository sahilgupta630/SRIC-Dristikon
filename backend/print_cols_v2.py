
import pandas as pd

file_path = "SRIC project list.xlsx"
xl = pd.ExcelFile(file_path)
target_sheet = next((s for s in xl.sheet_names if "Active" in s), xl.sheet_names[1] if len(xl.sheet_names)>1 else xl.sheet_names[0])

df = pd.read_excel(file_path, sheet_name=target_sheet)
cols = [str(c).lower().strip().replace(' ', '_').replace('.', '') for c in df.columns]

with open("cols_utf8.txt", "w", encoding="utf-8") as f:
    f.write(str(cols))
