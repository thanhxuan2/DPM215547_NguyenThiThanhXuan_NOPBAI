def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, int(abs(x)**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Chuỗi ví dụ (có thể nhập input)
s = input("Nhập chuỗi số (cách nhau bằng dấu ';'): ")

arr = s.split(';')

sochan = 0
soam = 0
sont = 0
tong = 0

for x in arr:
    print(x)            # Xuất từng số ra dòng riêng
    number = int(x)

    if number % 2 == 0:
        sochan += 1

    if number < 0:
        soam += 1

    if CheckPrime(number):
        sont += 1

    tong += number

print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", tong / len(arr))
