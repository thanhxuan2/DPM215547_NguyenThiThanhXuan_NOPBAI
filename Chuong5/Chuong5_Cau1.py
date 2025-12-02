def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            flag = False
            break
    return flag

def main():
    while True:  # vòng lặp vĩnh cửu
        s = input("Nhập 1 chuỗi: ")
        if CheckDoiXung(s):
            print("Chuỗi bạn nhập đối xứng")
        else:
            print("Chuỗi bạn nhập không đối xứng")
        
        tiep = input("Tiếp không Thím? (c/k): ").lower()
        if tiep == "k":
            print("CÁM ƠN THÍM")
            break

# Chạy chương trình
main()
