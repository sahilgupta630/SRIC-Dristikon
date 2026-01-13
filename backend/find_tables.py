
import re
import os
import sys

# Force utf-8
sys.stdout.reconfigure(encoding='utf-8')

path = os.path.join("app", "models", "generated_models.py")
with open(path, "r", encoding='utf-8') as f:
    content = f.read()
    classes = re.findall(r"class (\w+)\(Base\):", content)
    
    print(f"Total classes: {len(classes)}")
    
    keywords = ["Dept", "Department", "Staff", "Emp", "User", "Faculty", "Coord", "Investigator", "Member"]
    
    print("--- Potentially Relevant Tables ---")
    for c in classes:
        if any(k.lower() in c.lower() for k in keywords):
            print(c)
