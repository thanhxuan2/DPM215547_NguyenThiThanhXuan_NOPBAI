from random import randrange

# ------------------------------
# 1. Tạo ma trận ngẫu nhiên MxN
# ------------------------------
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(0, 100))  # giá trị 0-99
        D.append(row)
    return D

# ------------------------------
# 2. Xuất ma trận
# ------------------------------
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

# ------------------------------
# 3. Lấy dòng và xuất
# ------------------------------
def LayDong(D, r):
    return D[r]

def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

# ------------------------------
# 4. Lấy cột
# ------------------------------
def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

# ------------------------------
# 5. Tìm MAX trong ma trận
# ------------------------------
def MAX(D):
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_val < D[i][j]:
                max_val = D[i][j]
    return max_val

# ------------------------------
# MAIN
# ------------------------------
print("=== CHƯƠNG TRÌNH XỬ LÝ MA TRẬN ===")
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

D = TaoMaTran(m, n)
print("\nMa trận ngẫu nhiên:")
XuatMaTran(D)

r = int(input("\nNhập dòng muốn xuất (0-indexed): "))
print(f"Dòng {r}:")
XuatList1Chieu(LayDong(D, r))

c = int(input("\nNhập cột muốn xuất (0-indexed): "))
print(f"Cột {c}:")
XuatList1Chieu(LayCot(D, c))

print("\nSố lớn nhất trong ma trận =", MAX(D))
