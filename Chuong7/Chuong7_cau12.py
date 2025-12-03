# -*- coding: utf-8 -*-
import csv
import os
import random

file_path = "data_random.csv"

# ===============================
# PHẦN 1: Tạo file CSV với dữ liệu ngẫu nhiên
# ===============================
def TaoCSV():
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=';')
            for _ in range(10):  # 10 dòng
                line = [random.randint(1, 100) for _ in range(10)]
                writer.writerow(line)
        print(f"✅ Đã tạo file CSV: {file_path}")
    else:
        print(f"File {file_path} đã tồn tại, không tạo lại.")

# ===============================
# PHẦN 2: Đọc file CSV và xuất tổng mỗi dòng
# ===============================
def DocVaTinhTong():
    if not os.path.exists(file_path):
        print("❌ File CSV chưa tồn tại!")
        return

    print("Tổng giá trị các phần tử trên mỗi dòng:")
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for i, row in enumerate(reader, start=1):
            # Chuyển từng phần tử thành int
            numbers = [int(x) for x in row if x.strip()]
            tong = sum(numbers)
            print(f"Dòng {i}: {tong}")

# ===============================
# PHẦN 3: Menu chính
# ===============================
def Menu():
    while True:
        print("===== QUẢN LÝ CSV NGẪU NHIÊN =====")
        print("1. Tạo file CSV ngẫu nhiên 10x10")
        print("2. Đọc file CSV và tính tổng mỗi dòng")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            TaoCSV()
        elif choice == "2":
            DocVaTinhTong()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
        print()

# ===============================
# Chạy chương trình
# ===============================
if __name__ == "__main__":
    Menu()
