# -*- coding: utf-8 -*-
import json
import os

# ===============================
# PHẦN 1: File JSON
# ===============================
file_path = "sinhvien.json"

# Tạo file JSON mẫu nếu chưa tồn tại
if not os.path.exists(file_path):
    data_mau = [
        {
            "ma_lop": "L01",
            "ten_lop": "CNTT1",
            "sinhvien": [
                {"ma_sv": "SV1", "ten_sv": "Nguyễn Văn A", "nam_sinh": 2000},
                {"ma_sv": "SV2", "ten_sv": "Trần Thị B", "nam_sinh": 2001}
            ]
        },
        {
            "ma_lop": "L02",
            "ten_lop": "CNTT2",
            "sinhvien": [
                {"ma_sv": "SV3", "ten_sv": "Lê Văn C", "nam_sinh": 2000}
            ]
        }
    ]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_mau, f, indent=4, ensure_ascii=False)

# ===============================
# PHẦN 2: Đọc / Lưu JSON
# ===============================
def DocFile():
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def LuuFile(data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ===============================
# PHẦN 3: Chức năng chính
# ===============================
def XuatDS(data):
    print("\nDanh sách lớp và sinh viên:")
    for lop in data:
        print(f"Lớp: {lop['ma_lop']} - {lop['ten_lop']}")
        for sv in lop['sinhvien']:
            print(f"  {sv['ma_sv']}\t{sv['ten_sv']}\t{sv['nam_sinh']}")
    print()

def ThemSinhVien(data):
    ma_lop = input("Nhập mã lớp: ").strip()
    lop = next((l for l in data if l['ma_lop'] == ma_lop), None)
    if not lop:
        ten_lop = input("Nhập tên lớp mới: ").strip()
        lop = {"ma_lop": ma_lop, "ten_lop": ten_lop, "sinhvien": []}
        data.append(lop)
    ma_sv = input("Nhập mã sinh viên: ").strip()
    ten_sv = input("Nhập tên sinh viên: ").strip()
    nam_sinh = int(input("Nhập năm sinh: "))
    lop['sinhvien'].append({"ma_sv": ma_sv, "ten_sv": ten_sv, "nam_sinh": nam_sinh})
    LuuFile(data)
    print(f"✅ Thêm sinh viên {ma_sv} - {ten_sv} thành công!")

def SuaSinhVien(data):
    ma_sv = input("Nhập mã sinh viên muốn sửa: ").strip()
    for lop in data:
        for sv in lop['sinhvien']:
            if sv['ma_sv'] == ma_sv:
                sv['ten_sv'] = input(f"Nhập tên mới ({sv['ten_sv']}): ").strip() or sv['ten_sv']
                ns = input(f"Nhập năm sinh mới ({sv['nam_sinh']}): ").strip()
                if ns:
                    sv['nam_sinh'] = int(ns)
                LuuFile(data)
                print("✅ Sửa sinh viên thành công!")
                return
    print("❌ Không tìm thấy sinh viên.")

def XoaSinhVien(data):
    ma_sv = input("Nhập mã sinh viên muốn xóa: ").strip()
    for lop in data:
        for sv in lop['sinhvien']:
            if sv['ma_sv'] == ma_sv:
                lop['sinhvien'].remove(sv)
                LuuFile(data)
                print("✅ Xóa sinh viên thành công!")
                return
    print("❌ Không tìm thấy sinh viên.")

def TimKiemSinhVien(data):
    tu_khoa = input("Nhập mã hoặc tên sinh viên muốn tìm: ").strip().lower()
    ketqua = []
    for lop in data:
        for sv in lop['sinhvien']:
            if tu_khoa in sv['ma_sv'].lower() or tu_khoa in sv['ten_sv'].lower():
                ketqua.append((lop['ma_lop'], lop['ten_lop'], sv))
    if ketqua:
        print("Kết quả tìm kiếm:")
        for l_ma, l_ten, sv in ketqua:
            print(f"Lớp {l_ma}-{l_ten}: {sv['ma_sv']}\t{sv['ten_sv']}\t{sv['nam_sinh']}")
    else:
        print("❌ Không tìm thấy sinh viên phù hợp.")

def SapXepSinhVien(data):
    print("1. Theo tên tăng dần\n2. Theo năm sinh tăng dần")
    choice = input("Chọn: ").strip()
    for lop in data:
        if choice == "1":
            lop['sinhvien'].sort(key=lambda x: x['ten_sv'])
        elif choice == "2":
            lop['sinhvien'].sort(key=lambda x: x['nam_sinh'])
    print("✅ Sắp xếp xong!")
    XuatDS(data)

# ===============================
# PHẦN 4: Menu
# ===============================
def Menu():
    data = DocFile()
    while True:
        print("===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Sửa sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Sắp xếp sinh viên")
        print("6. Xem danh sách")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            ThemSinhVien(data)
        elif choice == "2":
            SuaSinhVien(data)
        elif choice == "3":
            XoaSinhVien(data)
        elif choice == "4":
            TimKiemSinhVien(data)
        elif choice == "5":
            SapXepSinhVien(data)
        elif choice == "6":
            XuatDS(data)
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
