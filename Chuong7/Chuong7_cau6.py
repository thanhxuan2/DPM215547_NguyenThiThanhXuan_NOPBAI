# -*- coding: utf-8 -*-
import csv
import os

# ===============================
# PHẦN 1: Tạo dữ liệu CSV mẫu
# ===============================
def TaoCSV(path):
    if not os.path.exists(path):
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE)
            # Ghi header
            writer.writerow(["ma", "ten"])
            # Ghi dữ liệu mẫu (chỉ 2 cột)
            writer.writerow(["nv1", "Obama"])
            writer.writerow(["nv2", "Kim Jong Un"])
            writer.writerow(["nv3", "Putin"])
        print(f"✅ Đã tạo file CSV mẫu: {path}")
    else:
        print(f"File {path} đã tồn tại, không tạo lại.")

# ===============================
# PHẦN 2: Đọc file CSV và xuất mã, tên
# ===============================
def XuatMaTenCSV(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        next(reader)  # bỏ header
        print("Danh sách mã và tên:")
        for row in reader:
            # kiểm tra tránh lỗi nếu dòng thiếu cột
            if len(row) >= 2:
                print(row[0], "\t", row[1])
            else:
                print("Dữ liệu không đủ cột:", row)

# ===============================
# PHẦN 3: Chương trình chính
# ===============================
if __name__ == "__main__":
    path = "datacsv.csv"
    TaoCSV(path)      # tạo dữ liệu mẫu nếu chưa có
    print()
    XuatMaTenCSV(path)  # xuất mã, tên

