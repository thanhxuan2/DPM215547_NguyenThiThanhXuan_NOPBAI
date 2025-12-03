from random import randrange

print("=== CHƯƠNG TRÌNH XỬ LÝ LIST NGẪU NHIÊN ===")

# ------------------------------
# 1. Khởi tạo list ngẫu nhiên
# ------------------------------
lst = []
n = int(input("Nhập số phần tử: "))

for i in range(n):
    lst.append(randrange(0, 100))

print("List sau khi tạo ngẫu nhiên:")
print(lst)

# ------------------------------
# 2. Thêm phần tử mới
# ------------------------------
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# ------------------------------
# 3. Xóa tất cả phần tử có giá trị k
# ------------------------------
k = int(input("Nhập số k cần xóa khỏi list: "))

while k in lst:
    lst.remove(k)

print("List sau khi xóa tất cả giá trị", k, ":")
print(lst)

# ------------------------------
# 4. Kiểm tra list có đối xứng hay không
# ------------------------------
def CheckDoiXung(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

if CheckDoiXung(lst):
    print("✔ List đối xứng")
else:
    print("✘ List không đối xứng")
