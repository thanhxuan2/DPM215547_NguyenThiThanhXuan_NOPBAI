# -*- coding: utf-8 -*-
from xml.dom.minidom import parse, Document
import os

# ===============================
# PHẦN 1: Tạo file XML mẫu nếu chưa có
# ===============================
def TaoFileXML(path):
    if not os.path.exists(path):
        # Tạo DOM document
        doc = Document()

        # Tạo root <employees>
        root = doc.createElement("employees")
        doc.appendChild(root)

        # Dữ liệu mẫu
        data_employees = [
            {"id": "1", "name": "Trần Duy Thanh"},
            {"id": "2", "name": "Lê Hoành Sử"},
            {"id": "3", "name": "Hồ Trung Thành"}
        ]

        # Tạo các thẻ <employee>
        for emp in data_employees:
            employee = doc.createElement("employee")

            # <id>
            id_tag = doc.createElement("id")
            id_text = doc.createTextNode(emp["id"])
            id_tag.appendChild(id_text)
            employee.appendChild(id_tag)

            # <name>
            name_tag = doc.createElement("name")
            name_text = doc.createTextNode(emp["name"])
            name_tag.appendChild(name_text)
            employee.appendChild(name_tag)

            # Thêm <employee> vào root
            root.appendChild(employee)

        # Ghi ra file
        with open(path, 'w', encoding='utf-8') as f:
            doc.writexml(f, indent="  ", addindent="  ", newl="\n", encoding="UTF-8")

        print(f"✅ Đã tạo file XML mẫu: {path}")
    else:
        print(f"File {path} đã tồn tại, không tạo lại.")

# ===============================
# PHẦN 2: Đọc dữ liệu XML bằng DOM
# ===============================
def DocXML(path):
    # Parse file
    DOMTree = parse(path)
    collection = DOMTree.documentElement

    # Lấy tất cả tag <employee>
    employees = collection.getElementsByTagName("employee")
    print("\nDanh sách nhân viên:")
    for employee in employees:
        tag_id = employee.getElementsByTagName("id")[0]
        emp_id = tag_id.childNodes[0].data

        tag_name = employee.getElementsByTagName("name")[0]
        emp_name = tag_name.childNodes[0].data

        print(emp_id, "\t", emp_name)

# ===============================
# PHẦN 3: Chương trình chính
# ===============================
if __name__ == "__main__":
    path = "employees.xml"
    TaoFileXML(path)  # tạo file nếu chưa có
    DocXML(path)      # đọc và xuất dữ liệu
