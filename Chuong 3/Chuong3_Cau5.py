#5: Hãy cho biết kết quả xuất ra màn hình

print("Kết quả Câu 5:")

cases = [
    ("a", 3, 5, 7),
    ("b", 3, 7, 5),
    ("c", 5, 3, 7),
    ("d", 5, 7, 3),
    ("e", 7, 3, 5),
    ("f", 7, 5, 3),
]

for name, i, j, k in cases:
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            pass
    print(f"{name}) i = {i}, j = {j}, k = {k}")