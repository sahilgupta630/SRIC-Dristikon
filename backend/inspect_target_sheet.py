
import pandas as pd

file_path = "SRIC project list.xlsx"
xl = pd.ExcelFile(file_path)
print("Sheet names:", xl.sheet_names)

target_sheet = None
for sheet in xl.sheet_names:
    if "Active" in sheet or "List" in sheet:
        target_sheet = sheet
        break

if target_sheet:
    print(f"\ninspecting sheet: {target_sheet}")
    df = pd.read_excel(file_path, sheet_name=target_sheet, nrows=5)
    print("Columns:", list(df.columns))
    print("\nFirst row sample:")
    print(df.iloc[0].to_dict())
else:
    print("\nCould not find a likely data sheet. Dumping Summary sheet:")
    df = pd.read_excel(file_path, sheet_name=0, nrows=5)
    print(df)
