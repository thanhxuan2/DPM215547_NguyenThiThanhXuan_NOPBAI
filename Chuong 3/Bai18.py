n = 4  # chiều cao (có thể đổi số khác)

print("\nHình 1:")
for i in range(n):
    if i == 0 or i == n-1:
        print("* " * n)
    else:
        print("*" + " "*(2*n-3) + "*")

print("\nHình 2:")
for i in range(1, n+1):
    # khoảng trắng bên trái: mỗi "*" chiếm 2 ký tự, nên phải nhân đôi
    spaces = " " * (2 * (n - i))
    stars = "* " * i
    print(spaces + stars)

print("\nHình 3:")
 # in đúng hình bạn yêu cầu (mặc định n = 4)
n = 4

stars = 2 * n - 1            # số sao ở hàng giữa
middle_width = 2 * stars - 1 # bề rộng ký tự của hàng giữa

# ---- nửa trên (tam giác trái rỗng) ----
for i in range(1, n):
    if i == 1:
        print("*")
    else:
        # giữa hai dấu * có (2*i - 3) khoảng trắng
        print("*" + " " * (2 * i - 3) + "*")

# ---- hàng giữa: đầy sao, cách nhau 1 space ----
print(" ".join(["*"] * stars))

# ---- nửa dưới (tam giác ngược rỗng, canh phải theo hàng giữa) ----
for i in range(n - 1, 0, -1):
    if i == 1:
        low = "*"
    else:
        low = "*" + " " * (2 * i - 3) + "*"
    leading = middle_width - len(low)   # căn phải để khớp bề rộng hàng giữa
    print(" " * leading + low)
