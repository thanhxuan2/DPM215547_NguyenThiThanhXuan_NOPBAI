# Hàm nhập ma trận kích thước m x n
def nhap_matrix(m, n, ten="A"):
    print(f"Nhập ma trận {ten} ({m}x{n}):")
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            val = int(input(f"{ten}[{i}][{j}] = "))
            row.append(val)
        M.append(row)
    return M

# Hàm xuất ma trận
def xuat_matrix(M):
    for row in M:
        print("\t".join(map(str, row)))

# Hàm cộng 2 ma trận
def cong_matrix(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# Hàm tính ma trận hoán vị (transpose)
def transpose(M):
    m = len(M)
    n = len(M[0])
    T = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        T.append(row)
    return T

# ------------------- Chương trình chính -------------------
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = nhap_matrix(m, n, "A")
B = nhap_matrix(m, n, "B")

print("\nMa trận A:")
xuat_matrix(A)

print("\nMa trận B:")
xuat_matrix(B)

# Cộng ma trận
C = cong_matrix(A, B)
print("\nMa trận C = A + B:")
xuat_matrix(C)

# Ma trận hoán vị
A_T = transpose(A)
B_T = transpose(B)
print("\nMa trận A hoán vị (transpose):")
xuat_matrix(A_T)

print("\nMa trận B hoán vị (transpose):")
xuat_matrix(B_T)
