#8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theođúng phép toán đã nhập.

print("Chương trình tính toán đơn giản")

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == "+":
    print("Kết quả:", a + b)
elif op == "-":
    print("Kết quả:", a - b)
elif op == "*":
    print("Kết quả:", a * b)
elif op == "/":
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ")