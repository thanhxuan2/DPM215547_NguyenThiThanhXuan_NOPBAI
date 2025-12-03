# ============================================
# CÂU 8: TÁCH LẤY TÊN BÀI HÁT
# ============================================

# Hàm lấy ra tên file + đuôi mở rộng
def LayFileVaDuoi(path):
    # Tách theo dấu '\'
    parts = path.split("\\")
    return parts[-1]

# Hàm lấy ra tên file KHÔNG có đuôi
def LayTenFile(path):
    full = LayFileVaDuoi(path)
    # Tách theo dấu .
    name = full.split(".")[0]
    return name


# ================================
# TEST CHƯƠNG TRÌNH
# ================================
duongdan = input("Nhập đường dẫn file nhạc: ")

print("Tên file + đuôi:", LayFileVaDuoi(duongdan))
print("Tên file:", LayTenFile(duongdan))
