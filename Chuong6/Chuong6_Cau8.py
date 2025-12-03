n = int(input("Nhập số lượng phần tử: "))

M = []
for i in range(n):
    num = float(input(f"Nhập số thực thứ {i+1}: "))
    M.append(num)

M.sort(reverse=True)  # Sắp xếp giảm dần

print("Dãy số sau khi sắp xếp giảm dần:", M)
