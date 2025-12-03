# -*- coding: utf-8 -*-
import os

# ===============================
# PHẦN 1: Đọc / Lưu dữ liệu Text File
# ===============================
# ===============================
# PHẦN 1: Đọc / Lưu dữ liệu Text File
# ===============================
file_path = "sanpham.txt"

# Tạo file mẫu nếu chưa tồn tại
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("DM1;Nước ngọt;SP1;Coca;15000\n")
        f.write("DM1;Nước ngọt;SP2;Pepsi;18000\n")


# Dữ liệu dạng: ma_dm;ten_dm;ma_sp;ten_sp;don_gia
def DocFile():
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                arr = line.strip().split(";")
                if len(arr) == 5:
                    ma_dm, ten_dm, ma_sp, ten_sp, don_gia = arr
                    data.append({
                        "ma_dm": ma_dm,
                        "ten_dm": ten_dm,
                        "ma_sp": ma_sp,
                        "ten_sp": ten_sp,
                        "don_gia": float(don_gia)
                    })
    return data

def LuuFile(data):
    with open(file_path, "w", encoding="utf-8") as f:
        for item in data:
            line = f"{item['ma_dm']};{item['ten_dm']};{item['ma_sp']};{item['ten_sp']};{item['don_gia']}"
            f.write(line + "\n")

# ===============================
# PHẦN 2: Chức năng chính
# ===============================
def ThemSanPham(data):
    ma_dm = input("Nhập mã danh mục: ").strip()
    ten_dm = input("Nhập tên danh mục: ").strip()
    ma_sp = input("Nhập mã sản phẩm: ").strip()
    ten_sp = input("Nhập tên sản phẩm: ").strip()
    don_gia = float(input("Nhập đơn giá: "))
    data.append({
        "ma_dm": ma_dm,
        "ten_dm": ten_dm,
        "ma_sp": ma_sp,
        "ten_sp": ten_sp,
        "don_gia": don_gia
    })
    LuuFile(data)  # tự động lưu vào file
    print(f"✅ Thêm sản phẩm {ma_sp} - {ten_sp} thành công!")


def XuatSanPham(data):
    print("\nDanh sách sản phẩm:")
    print("Ma_DM\tTen_DM\tMa_SP\tTen_SP\tDonGia")
    for sp in data:
        print(f"{sp['ma_dm']}\t{sp['ten_dm']}\t{sp['ma_sp']}\t{sp['ten_sp']}\t{sp['don_gia']}")
    print()

def SuaSanPham(data):
    ma_sp = input("Nhập mã sản phẩm muốn sửa: ").strip()
    for sp in data:
        if sp['ma_sp'] == ma_sp:
            sp['ten_sp'] = input(f"Nhập tên sản phẩm mới ({sp['ten_sp']}): ").strip() or sp['ten_sp']
            gia = input(f"Nhập đơn giá mới ({sp['don_gia']}): ").strip()
            if gia:
                sp['don_gia'] = float(gia)
            print("✅ Sửa sản phẩm thành công!")
            return
    print("❌ Không tìm thấy sản phẩm.")

def XoaSanPham(data):
    ma_sp = input("Nhập mã sản phẩm muốn xóa: ").strip()
    for sp in data:
        if sp['ma_sp'] == ma_sp:
            data.remove(sp)
            print("✅ Xóa sản phẩm thành công!")
            return
    print("❌ Không tìm thấy sản phẩm.")

def TimKiemSanPham(data):
    tu_khoa = input("Nhập mã hoặc tên sản phẩm muốn tìm: ").strip().lower()
    ketqua = [sp for sp in data if tu_khoa in sp['ma_sp'].lower() or tu_khoa in sp['ten_sp'].lower()]
    if ketqua:
        XuatSanPham(ketqua)
    else:
        print("❌ Không tìm thấy sản phẩm phù hợp.")

def SapXepSanPham(data):
    print("1. Theo giá tăng dần\n2. Theo giá giảm dần")
    choice = input("Chọn: ").strip()
    if choice == "1":
        data.sort(key=lambda x: x['don_gia'])
    elif choice == "2":
        data.sort(key=lambda x: x['don_gia'], reverse=True)
    else:
        print("Lựa chọn không hợp lệ.")
        return
    print("✅ Sắp xếp xong!")
    XuatSanPham(data)

# ===============================
# PHẦN 3: Menu
# ===============================
def Menu():
    data = DocFile()
    while True:
        print("===== QUẢN LÝ SẢN PHẨM =====")
        print("1. Thêm sản phẩm mới")
        print("2. Sửa sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Sắp xếp sản phẩm theo giá")
        print("6. Xem danh sách sản phẩm")
        print("0. Lưu và thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            ThemSanPham(data)
        elif choice == "2":
            SuaSanPham(data)
        elif choice == "3":
            XoaSanPham(data)
        elif choice == "4":
            TimKiemSanPham(data)
        elif choice == "5":
            SapXepSanPham(data)
        elif choice == "6":
            XuatSanPham(data)
        elif choice == "0":
            LuuFile(data)
            print("✅ Dữ liệu đã lưu vào Text File. Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
        print()

# ===============================
# Chạy chương trình
# ===============================
if __name__ == "__main__":
    Menu()

   

