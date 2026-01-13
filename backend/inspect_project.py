
import sys
import os
sys.path.append(os.getcwd())
try:
    from app.models.generated_models import SricProjectMaster
    print("--- SricProjectMaster Columns ---")
    for col in SricProjectMaster.__table__.columns:
        print(f"{col.name}")
except ImportError:
    print("Could not import SricProjectMaster")

import re
path = os.path.join("app", "models", "generated_models.py")
with open(path, "r", encoding='utf-8') as f:
    content = f.read()
    classes = re.findall(r"class (\w+)\(Base\):", content)
    print("\n--- Project Related Tables ---")
    for c in classes:
        if "Project" in c:
            print(c)
