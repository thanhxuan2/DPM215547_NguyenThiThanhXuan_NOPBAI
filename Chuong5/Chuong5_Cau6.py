# ============================================
# CÂU 6: TRÍCH LỌC SỐ NGUYÊN ÂM TRONG CHUỖI
# ============================================

def NegativeNumberInStrings(s):
    kq = []        # danh sách số âm tìm được
    i = 0

    while i < len(s):
        # Nếu gặp dấu '-' và ký tự sau nó là số
        if s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit():
            num = "-"  # bắt đầu số âm
            i += 1
            # đọc tiếp các chữ số phía sau
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            kq.append(int(num))
        else:
            i += 1
    return kq


# ===============================
# TEST chương trình
# ===============================
s = input("Nhập chuỗi cần trích lọc số âm: ")
ds_am = NegativeNumberInStrings(s)

print("\nCác số nguyên âm trong chuỗi:")
for x in ds_am:
    print(x)
