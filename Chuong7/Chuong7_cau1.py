# -*- coding: utf-8 -*-
# File: Chuong7/chuong7_cau1.py

# ===============================
# PHẦN 1: Hàm xử lý file
# ===============================
def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data + "\n")

def DocFile(path):
    arrProduct = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            arr = data.split(';')
            arr[2] = float(arr[2])  # chuyển đơn giá sang float
            arrProduct.append(arr)
    return arrProduct

# ===============================
# PHẦN 2: Nhập sản phẩm
# ===============================
def NhapSanPham():
    masp = input("Nhập mã SP: ")
    tensp = input("Nhập tên SP: ")
    dongia = float(input("Nhập giá: "))
    line = f"{masp};{tensp};{dongia}"
    LuuFile("database.txt", line)
    print("✅ Đã lưu sản phẩm vào file!")

# ===============================
# PHẦN 3: Xuất và sắp xếp sản phẩm
# ===============================
def XuatSanPham(dssp):
    print("Mã SP\tTên SP\tĐơn giá")
    for row in dssp:
        for element in row:
            print(element, end='\t')
        print()
    print()

def SortSp(dssp):
    return sorted(dssp, key=lambda x: x[2], reverse=True)

# ===============================
# PHẦN 4: Chạy chương trình
# ===============================
if __name__ == "__main__":
    while True:
        print("1. Nhập sản phẩm mới")
        print("2. Xem danh sách sản phẩm")
        print("3. Xem danh sách sản phẩm sắp xếp theo giá giảm dần")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == "1":
            NhapSanPham()
        elif choice == "2":
            dssp = DocFile("database.txt")
            print("Danh sách sản phẩm từ file:")
            XuatSanPham(dssp)
        elif choice == "3":
            dssp = DocFile("database.txt")
            dssp_sorted = SortSp(dssp)
            print("Sản phẩm sau khi sắp xếp giá giảm dần:")
            XuatSanPham(dssp_sorted)
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Chọn sai, vui lòng chọn lại.")
