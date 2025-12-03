# Khởi tạo list
lst = [20, 1, -34, 40, -8, 60, 1, 3]

# (a) In toàn bộ list
print("lst =", lst)  # Kết quả: [20, 1, -34, 40, -8, 60, 1, 3]

# (b) In các phần tử từ index 0 đến 2
print("lst[0:3] =", lst[0:3])  # [20, 1, -34]

# (c) In các phần tử từ index 4 đến 7
print("lst[4:8] =", lst[4:8])  # [-8, 60, 1, 3]

# (d) In các phần tử từ index 4 đến 33
# Nếu chỉ số vượt quá list, Python lấy đến cuối
print("lst[4:33] =", lst[4:33])  # [-8, 60, 1, 3]

# (e) In các phần tử từ index -5 đến -3 (tính từ cuối list)
print("lst[-5:-3] =", lst[-5:-3])  # [40, -8]

# (f) In các phần tử từ index -22 đến 3
# start âm vượt quá list → Python bắt đầu từ đầu, end = 3
print("lst[-22:3] =", lst[-22:3])  # [20, 1, -34]

# (g) In các phần tử từ index 4 đến cuối
print("lst[4:] =", lst[4:])  # [-8, 60, 1, 3]

# (h) In toàn bộ list bằng slicing
print("lst[:] =", lst[:])  # [20, 1, -34, 40, -8, 60, 1, 3]

# (i) In các phần tử từ đầu đến index 3
print("lst[:4] =", lst[:4])  # [20, 1, -34, 40]

# (j) In các phần tử từ index 1 đến 4
print("lst[1:5] =", lst[1:5])  # [1, -34, 40, -8]

# (k) Kiểm tra xem -34 có trong list không
print("-34 in lst =", -34 in lst)  # True

# (l) Kiểm tra xem -34 không có trong list
print("-34 not in lst =", -34 not in lst)  # False

# (m) Đếm số phần tử trong list
print("len(lst) =", len(lst))  # 8
