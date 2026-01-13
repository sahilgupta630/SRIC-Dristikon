
import pandas as pd
import os
import sys

file_path = "SRIC_DB_PROD_without-cross-db.xlsx"

try:
    print(f"Reading {file_path}...")
    # Load all sheets
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print(f"Found sheets: {sheet_names}")

    schema = {}
    for sheet_name in sheet_names:
        print(f"Processing sheet: {sheet_name}...")
        df = pd.read_excel(xls, sheet_name=sheet_name, header=1)
        
        # Iterate over rows
        for index, row in df.iterrows():
            table_name = row['Table Name']
            if pd.isna(table_name):
                continue
            
            if table_name not in schema:
                schema[table_name] = []
            
            # Clean up column names usually represented as "Unnamed: X" if keys are wrong
            # But here we rely on 'Column', 'Data Type', etc. from header=1
            
            col_name = row['Column']
            dtype = row['Data Type']
            nullable = row['IS NULLABLE']
            
            if pd.isna(col_name):
                continue

            schema[table_name].append({
                'column': col_name,
                'type': dtype,
                'nullable': nullable
            })
    
    print(f"Extracted {len(schema)} tables.")

    # SQLAlchemy Type Mapping
    type_mapping = {
        'integer': 'Integer',
        'character varying': 'String',
        'character': 'String',
        'text': 'Text',
        'timestamp without time zone': 'DateTime',
        'date': 'Date',
        'double precision': 'Float',
        'numeric': 'Numeric',
        'bytea': 'LargeBinary',
        'boolean': 'Boolean',
        'bigint': 'BigInteger'
    }

    model_code = [
        "from sqlalchemy import Column, Integer, String, DateTime, Date, Float, Numeric, LargeBinary, Boolean, BigInteger, Text",
        "from sqlalchemy.ext.declarative import declarative_base",
        "",
        "Base = declarative_base()",
        ""
    ]

    for table_name, columns in schema.items():
        # Sanitize class name
        clean_table_name = str(table_name).replace(" ", "_").replace("-", "_")
        class_name = "".join(x.capitalize() or '_' for x in clean_table_name.split('_'))
        
        model_code.append(f"class {class_name}(Base):")
        model_code.append(f"    __tablename__ = '{table_name}'")
        model_code.append("")
        
        primary_key_set = False
        
        # Determine Primary Key
        pk_column = None
        # Priority list
        priority_pks = ['sl_no', 'id', 'serial_no', 'project_code', 'receipt_no', 'bill_no', 'rollno', 'user_code', 'vendor_code', 'fin_year']
        
        # Check if any column matches priority
        for col in columns:
            if str(col['column']).strip().lower() in priority_pks:
                pk_column = str(col['column']).strip()
                break
        
        # Fallback to first column if no priority match
        if not pk_column and columns:
             pk_column = str(columns[0]['column']).strip()

        for col in columns:
            col_name = str(col['column']).strip()
            dtype = str(col['type']).strip().lower()
            nullable = str(col['nullable']).strip().upper() == 'YES'
            
            sa_type = type_mapping.get(dtype, 'String') 
            
            is_pk = False
            if col_name == pk_column:
                    is_pk = True
            
            # Sanitize column name for Python
            py_col_name = col_name.replace(" ", "_").replace("-", "_").replace(".", "_")
            if py_col_name[0].isdigit():
                py_col_name = f"_{py_col_name}"
            
            # Avoid ensuring unique attributes if duplicates exist in schema (legacy DBs are messy)
            # But let's assume unique for now or add counter
            
            line = f"    {py_col_name} = Column({sa_type}"
            if col_name != py_col_name:
                line = f"    {py_col_name} = Column('{col_name}', {sa_type}"
            
            if is_pk:
                line += ", primary_key=True"
            if not nullable and not is_pk:
                line += ", nullable=False"
            line += ")"
            
            model_code.append(line)
        model_code.append("")
        model_code.append("")
    
    # Ensure directory exists (absolute path safety)
    output_dir = os.path.join(os.getcwd(), "app", "models")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, "generated_models.py")
    
    with open(output_path, "w") as f:
        f.write("\n".join(model_code))
        
    print(f"Successfully generated models in {output_path}")

except ImportError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error analyzing file: {e}")
    import traceback
    traceback.print_exc()
