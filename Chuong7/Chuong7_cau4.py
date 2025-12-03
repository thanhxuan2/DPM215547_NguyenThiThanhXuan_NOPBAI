# -*- coding: utf-8 -*-
import json

# String JSON mẫu
jsonString = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

# Chuyển đổi JSON string sang Python Object (dict)
dataObject = json.loads(jsonString)

# Xuất toàn bộ object
print("Dữ liệu Python Object:")
print(dataObject)
print()

# Xuất từng trường đúng
print("Mã =", dataObject["ma"])
print("Tuổi =", dataObject["age"])
print("Tên =", dataObject["ten"])
