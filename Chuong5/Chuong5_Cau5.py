# ============================================
# CÂU 5: XỬ LÝ CHUỖI VỚI CÁC HÀM CƠ BẢN
# ============================================

def main():
    s = input("Nhập vào 1 chuỗi: ")

    so_in_hoa = 0
    so_in_thuong = 0
    so_chu_so = 0
    so_ky_tu_dac_biet = 0
    so_khoang_trang = 0
    so_nguyen_am = 0
    so_phu_am = 0

    # Tập nguyên âm tiếng Việt chỉ xét a, e, i, o, u (không dấu)
    nguyen_am = "aeiouAEIOU"

    for ch in s:
        if ch.isupper():
            so_in_hoa += 1
        if ch.islower():
            so_in_thuong += 1
        if ch.isdigit():
            so_chu_so += 1
        if ch.isspace():
            so_khoang_trang += 1

        # Nguyên âm và phụ âm
        if ch.isalpha():  # nếu là chữ cái
            if ch in nguyen_am:
                so_nguyen_am += 1
            else:
                so_phu_am += 1
        else:
            # không phải chữ cái, không phải số, không phải khoảng trắng
            if not ch.isdigit() and not ch.isspace():
                so_ky_tu_dac_biet += 1

    # ======== Xuất kết quả ========
    print("\n===== KẾT QUẢ =====")
    print("Số chữ IN HOA:", so_in_hoa)
    print("Số chữ in thường:", so_in_thuong)
    print("Số chữ số:", so_chu_so)
    print("Số ký tự đặc biệt:", so_ky_tu_dac_biet)
    print("Số khoảng trắng:", so_khoang_trang)
    print("Số nguyên âm:", so_nguyen_am)
    print("Số phụ âm:", so_phu_am)


# Gọi hàm main
main()
