# ============================================
# CÂU 4: CÁC HÀM QUAN TRỌNG TRONG XỬ LÝ CHUỖI PYTHON
# ============================================

def demo_string_functions():
    s = "  xin ChAO cac BAN  "

    print("Chuỗi gốc:", repr(s))

    # --- 1. Các hàm thay đổi nội dung ---
    print("\n1. HÀM THAY ĐỔI NỘI DUNG")
    print("upper()     →", s.upper())
    print("lower()     →", s.lower())
    print("capitalize()→", s.capitalize())
    print("title()     →", s.title())

    # --- 2. Hàm xóa khoảng trắng ---
    print("\n2. HÀM XOÁ KHOẢNG TRẮNG")
    print("strip()  →", repr(s.strip()))
    print("lstrip() →", repr(s.lstrip()))
    print("rstrip() →", repr(s.rstrip()))

    # --- 3. Tách và nối chuỗi ---
    print("\n3. TÁCH VÀ NỐI CHUỖI")
    items = "5;7;8;9"
    print("Chuỗi:", items)
    arr = items.split(";")
    print("split(';') →", arr)
    print("join với '-' →", "-".join(arr))

    # --- 4. Tìm kiếm ---
    print("\n4. TÌM KIẾM")
    sample = "banana"
    print("Chuỗi:", sample)
    print("find('a') →", sample.find("a"))
    print("count('a') →", sample.count("a"))

    # --- 5. Kiểm tra nội dung ---
    print("\n5. KIỂM TRA NỘI DUNG")
    print("'123'.isdigit() →", "123".isdigit())
    print("'abc'.isalpha() →", "abc".isalpha())
    print("'abc123'.isalnum() →", "abc123".isalnum())
    print("'   '.isspace() →", "   ".isspace())
    print("'HELLO'.isupper() →", "HELLO".isupper())
    print("'hello'.islower() →", "hello".islower())

    # --- 6. Thay thế ---
    print("\n6. THAY THẾ")
    print("replace('ChAO', 'chào') →", s.replace("ChAO", "chào"))

    # --- 7. Lấy chuỗi con ---
    print("\n7. LẤY CHUỖI CON (slice)")
    t = "python"
    print("Chuỗi:", t)
    print("t[0:3]  →", t[0:3])   # pyt
    print("t[-3:] →", t[-3:])   # hon


# Gọi hàm để chạy demo
demo_string_functions()
