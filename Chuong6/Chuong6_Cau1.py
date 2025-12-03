from random import randrange

print("Chương trình xử lý List")

# --- Khởi tạo LIST ---
n = int(input("Nhập số phần tử: "))
lst = [0] * n

for i in range(n):
    lst[i] = randrange(-100, 100)

print("List ngẫu nhiên là:")
print(lst)

# --- Thêm phần tử vào list ---
value = int(input("Mời bạn thêm số mới: "))
lst.append(value)
print("List sau khi thêm:")
print(lst)

# --- Kiểm tra số k xuất hiện bao nhiêu lần ---
k = int(input("Bạn muốn đếm số nào: "))
dem = lst.count(k)
print(f"{k} xuất hiện {dem} lần trong list")

# --- Hàm kiểm tra số nguyên tố ---
def CheckPrime(n):
    if n < 2:
        return False
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2

# --- Tính tổng số nguyên tố ---
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng số nguyên tố =", tongnt)

# --- Sắp xếp list ---
lst.sort()
print("List sau khi sort:")
print(lst)

# --- Xóa list ---
del lst
print("List sau khi xóa:")
try:
    print(lst)
except:
    print("List đã bị xóa hoàn toàn!")
