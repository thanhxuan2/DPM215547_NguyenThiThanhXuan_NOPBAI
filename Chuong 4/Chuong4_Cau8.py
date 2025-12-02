# Hàm tính tổng các ước số (không tính chính nó)
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

# a) Kiểm tra số hoàn thiện
def la_so_hoan_thien(n):
    return tong_uoc_so(n) == n

# b) Kiểm tra số thịnh vượng
def la_so_thinh_vuong(n):
    return tong_uoc_so(n) > n


# ==========================
# Chạy thử
# ==========================
n = int(input("Nhập số nguyên dương n: "))

tong = tong_uoc_so(n)
print(f"Tổng các ước số (không kể {n}) = {tong}")

if la_so_hoan_thien(n):
    print(n, "là số hoàn thiện.")
elif la_so_thinh_vuong(n):
    print(n, "là số thịnh vượng.")
else:
    print(n, "không phải số hoàn thiện hay thịnh vượng.")
