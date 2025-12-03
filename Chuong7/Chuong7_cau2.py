# -*- coding: utf-8 -*-
import os

# ===============================
# PHẦN 1: Hàm xử lý file
# ===============================
def LuuFile(path, data):
    """Ghi nối đuôi 1 dòng dữ liệu vào file"""
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data + "\n")

def DocFile(path):
    """Đọc dữ liệu từ file, mỗi dòng thành 1 list"""
    arrSo = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            arr = data.split(',')  # tách theo dấu ','
            arrSo.append(arr)
    return arrSo

# ===============================
# PHẦN 2: Tạo dữ liệu mẫu
# ===============================
def TaoDuLieuMau(path):
    """Tạo file csdl_so.txt với dữ liệu mẫu"""
    if not os.path.exists(path):
        LuuFile(path, "-5,4,7,9,3,20")
        LuuFile(path, "5,-4,37,-19,24,-21")
        LuuFile(path, "15,9,0,-38,-3,15")
        LuuFile(path, "5,-4,77,-9,3,-7")
        LuuFile(path, "55,44,27")
        LuuFile(path, "-50,26")
        print(f"✅ Đã tạo dữ liệu mẫu trong file {path}")
    else:
        print(f"File {path} đã tồn tại, không tạo lại.")

# ===============================
# PHẦN 3: Xuất số âm trên mỗi dòng
# ===============================
def XuatSoAmTrenMoiDong(arrSo):
    print("Các số âm trên mỗi dòng:")
    for row in arrSo:
        for element in row:
            number = int(element)
            if number < 0:
                print(number, end='\t')
        print()  # xuống dòng sau mỗi dòng trong file

# ===============================
# PHẦN 4: Chương trình chính
# ===============================
if __name__ == "__main__":
    path = "csdl_so.txt"
    TaoDuLieuMau(path)  # tạo file nếu chưa có

    # Đọc dữ liệu từ file
    arrSo = DocFile(path)

    # Xuất dữ liệu gốc
    print("\nDữ liệu đọc từ file:")
    for row in arrSo:
        print(row)
    print()

    # Xuất số âm trên mỗi dòng
    XuatSoAmTrenMoiDong(arrSo)
