# -*- coding: utf-8 -*-
import json

# ===============================
# PHẦN 1: Python Object mẫu
# ===============================
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# ===============================
# PHẦN 2: Chuyển Python Object sang String JSON
# ===============================
jsonString = json.dumps(pythonObject, ensure_ascii=False)  # ensure_ascii=False để giữ tiếng Việt

# ===============================
# PHẦN 3: Xuất kết quả
# ===============================
print("Python Object:")
print(pythonObject)
print()

print("Chuyển sang String JSON:")
print(jsonString)

with open("data.json", "w", encoding="utf-8") as f:
    f.write(jsonString)

