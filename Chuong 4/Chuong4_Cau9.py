import math

def nested_sqrt(n):
    result = 0
    for i in range(n):
        result = math.sqrt(2 + result)
    return result

# Nhập số n
n = int(input("Nhập n: "))
print(f"S({n}) =", nested_sqrt(n))
