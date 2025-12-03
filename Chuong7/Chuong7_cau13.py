# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
import os

# ===============================
# PHẦN 1: Kiểm tra và tạo file XML mẫu
# ===============================
def TaoFileXML():
    if not os.path.exists("nhomthietbi.xml"):
        with open("nhomthietbi.xml", "w", encoding="utf-8") as f:
            f.write("""<?xml version="1.0" encoding="UTF-8" ?>
<nhoms>
 <nhom>
 <ma>n1</ma>
 <ten>Nhóm 1</ten>
 </nhom>
 <nhom>
 <ma>n2</ma>
 <ten>Nhóm 2</ten>
 </nhom>
 <nhom>
 <ma>n3</ma>
 <ten>Nhóm 3</ten>
 </nhom>
</nhoms>""")
    if not os.path.exists("ThietBi.xml"):
        with open("ThietBi.xml", "w", encoding="utf-8") as f:
            f.write("""<?xml version="1.0" encoding="UTF-8" ?>
<thietbis>
 <thietbi manhom="n1">
 <ma>tb1</ma>
 <ten>Thiết bị 1</ten>
 </thietbi>
 <thietbi manhom="n1">
 <ma>tb2</ma>
 <ten>Thiết bị 2</ten>
 </thietbi>
 <thietbi manhom="n2">
 <ma>tb3</ma>
 <ten>Thiết bị 3</ten>
 </thietbi>
 <thietbi manhom="n3">
 <ma>tb4</ma>
 <ten>Thiết bị 4</ten>
 </thietbi>
 <thietbi manhom="n3">
 <ma>tb5</ma>
 <ten>Thiết bị 5</ten>
 </thietbi>
</thietbis>""")
    print("✅ File XML mẫu đã sẵn sàng.")

# ===============================
# PHẦN 2: Hàm đọc XML
# ===============================
def DocNhom():
    DOMTree = parse("nhomthietbi.xml")
    collection = DOMTree.documentElement
    nhoms = collection.getElementsByTagName("nhom")
    danh_sach = []
    for nhom in nhoms:
        ma = nhom.getElementsByTagName("ma")[0].childNodes[0].data
        ten = nhom.getElementsByTagName("ten")[0].childNodes[0].data
        danh_sach.append({"ma": ma, "ten": ten})
    return danh_sach

def DocThietBi():
    DOMTree = parse("ThietBi.xml")
    collection = DOMTree.documentElement
    thietbis = collection.getElementsByTagName("thietbi")
    danh_sach = []
    for tb in thietbis:
        ma = tb.getElementsByTagName("ma")[0].childNodes[0].data
        ten = tb.getElementsByTagName("ten")[0].childNodes[0].data
        manhom = tb.getAttribute("manhom")
        danh_sach.append({"ma": ma, "ten": ten, "manhom": manhom})
    return danh_sach

# ===============================
# PHẦN 3: Chức năng quản lý
# ===============================
def HienThiNhom():
    nhoms = DocNhom()
    print("\nDanh sách Nhóm Thiết bị:")
    print("Mã\tTên")
    for nhom in nhoms:
        print(f"{nhom['ma']}\t{nhom['ten']}")
    print()

def HienThiThietBi():
    thietbis = DocThietBi()
    print("\nDanh sách Thiết bị:")
    print("Mã\tTên\tMã Nhóm")
    for tb in thietbis:
        print(f"{tb['ma']}\t{tb['ten']}\t{tb['manhom']}")
    print()

def LocTheoNhom():
    nhoms = DocNhom()
    thietbis = DocThietBi()
    print("\nCác nhóm có sẵn:")
    for nhom in nhoms:
        print(f"{nhom['ma']}: {nhom['ten']}")
    ma_nhom = input("Nhập mã nhóm cần lọc: ").strip()
    ds = [tb for tb in thietbis if tb['manhom'] == ma_nhom]
    if ds:
        print(f"\nThiết bị thuộc nhóm {ma_nhom}:")
        print("Mã\tTên")
        for tb in ds:
            print(f"{tb['ma']}\t{tb['ten']}")
    else:
        print("❌ Không tìm thấy thiết bị nào thuộc nhóm này.")
    print()

def NhomNhieuThietBiNhat():
    thietbis = DocThietBi()
    dem = {}
    for tb in thietbis:
        dem[tb['manhom']] = dem.get(tb['manhom'], 0) + 1
    max_nhom = max(dem, key=dem.get)
    print(f"\nNhóm thiết bị có số lượng nhiều nhất: {max_nhom} ({dem[max_nhom]} thiết bị)\n")

# ===============================
# PHẦN 4: Menu chính
# ===============================
def Menu():
    while True:
        print("===== QUẢN LÝ THIẾT BỊ =====")
        print("1. Hiển thị danh sách Nhóm thiết bị")
        print("2. Hiển thị toàn bộ Thiết bị")
        print("3. Lọc thiết bị theo Nhóm")
        print("4. Nhóm thiết bị có số lượng nhiều nhất")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            HienThiNhom()
        elif choice == "2":
            HienThiThietBi()
        elif choice == "3":
            LocTheoNhom()
        elif choice == "4":
            NhomNhieuThietBiNhat()
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
    TaoFileXML()
    Menu()
