#9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.

month = int(input("Nhập vào 1 tháng (1-12): "))

if 1 <= month <= 3:
    print("Tháng", month, "thuộc Quý 1")
elif 4 <= month <= 6:
    print("Tháng", month, "thuộc Quý 2")
elif 7 <= month <= 9:
    print("Tháng", month, "thuộc Quý 3")
elif 10 <= month <= 12:
    print("Tháng", month, "thuộc Quý 4")
else:
    print("Tháng không hợp lệ")