from random import randint

N = int(input("Nhập số phần tử N: "))

lst = []
while len(lst) < N:
    num = randint(1, 100)  # Sinh số ngẫu nhiên từ 1 đến 100
    if num not in lst:     # Kiểm tra xem số có trùng chưa
        lst.append(num)    # Nếu chưa, thêm vào list

print("List N số ngẫu nhiên không trùng nhau:", lst)
