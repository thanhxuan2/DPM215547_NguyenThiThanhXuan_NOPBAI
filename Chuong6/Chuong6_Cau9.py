# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Mảng số tự nhiên cho sẵn
M = [3,6,7,8,11,17,2,90,2,5,4,5,8]

# Dòng 1: các số lẻ
odd_numbers = [x for x in M if x % 2 != 0]
print("Các số lẻ:", odd_numbers, "Tổng số lẻ =", len(odd_numbers))

# Dòng 2: các số chẵn
even_numbers = [x for x in M if x % 2 == 0]
print("Các số chẵn:", even_numbers, "Tổng số chẵn =", len(even_numbers))

# Dòng 3: các số nguyên tố
prime_numbers = [x for x in M if is_prime(x)]
print("Các số nguyên tố:", prime_numbers)

# Dòng 4: các số không phải số nguyên tố
non_prime_numbers = [x for x in M if not is_prime(x)]
print("Các số không phải số nguyên tố:", non_prime_numbers)
