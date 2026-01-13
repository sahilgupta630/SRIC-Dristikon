
import re
import os

path = os.path.join("app", "models", "generated_models.py")
with open(path, "r", encoding='utf-8') as f:
    content = f.read()
    classes = re.findall(r"class (\w+)\(Base\):", content)
    with open("all_tables.txt", "w") as out:
        for c in classes:
            out.write(c + "\n")
