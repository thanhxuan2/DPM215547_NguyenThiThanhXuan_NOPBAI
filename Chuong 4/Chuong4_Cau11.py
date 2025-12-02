def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


#TH1
def main():
    global val
    val = 5
    print(sum2())   # sum2 giảm val từ 5 -> 0
    print(sum1(5))  # sum1(5) = 5, không phụ thuộc val
    print(sum3())   # val = 0 sau sum2, nên sum3() = 0
main()
#KQ
5
5
5

#TH2
def main():
    global val
    val = 5
    print(sum1(5))  # sum1(5) = 5
    print(sum3())   # sum3() dùng val=5, nên kết quả = 5
    print(sum2())   # sum2() giảm val từ 5 -> 0, kết quả = 5
main()
#KQ
5
5
5
def main():
    global val
    val = 5
    print(sum1(5))  # sum1(5) = 5
    print(sum3())   # sum3() dùng val=5, nên kết quả = 5
    print(sum2())   # sum2() giảm val từ 5 -> 0, kết quả = 5
main()

#KQ
5
5
0




