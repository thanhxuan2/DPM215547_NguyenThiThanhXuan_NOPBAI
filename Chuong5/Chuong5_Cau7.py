# ============================================
# CÂU 7: TỐI ƯU CHUỖI DANH TỪ
# ============================================

def ToiUuChuoiDanhTu(s):
    # Xóa khoảng trắng dư thừa ở đầu/cuối + tách từ
    words = s.strip().split()

    # Viết hoa chữ cái đầu từng từ, các chữ còn lại viết thường
    result = []
    for w in words:
        result.append(w.capitalize())

    # Ghép lại với 1 khoảng trắng giữa các từ
    return " ".join(result)


# ===============================
# TEST CHƯƠNG TRÌNH
# ===============================
s = input("Nhập chuỗi danh từ: ")
print("Chuỗi tối ưu:", ToiUuChuoiDanhTu(s))
