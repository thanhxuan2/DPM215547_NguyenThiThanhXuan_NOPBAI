#7 Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngàyvừa nhập (ngày/tháng/năm).

def la_nam_nhuan(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def so_ngay_trong_thang(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if la_nam_nhuan(year) else 28
    else:
        return 0  # tháng không hợp lệ

def ngay_ke_tiep(day, month, year):
    day += 1
    if day > so_ngay_trong_thang(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year

# --- Chương trình chính ---
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if 1 <= m <= 12 and 1 <= d <= so_ngay_trong_thang(m, y):
    nd, nm, ny = ngay_ke_tiep(d, m, y)
    print("Ngày kế tiếp là: {}/{}/{}".format(nd, nm, ny))
else:
    print("Ngày tháng năm không hợp lệ!")