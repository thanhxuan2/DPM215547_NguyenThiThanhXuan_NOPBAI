#6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.(vd: n=35 => Ba mươi lăm, n=5 => năm)

def doc_so(n):
    dv = {0:"",1:"một",2:"hai",3:"ba",4:"bốn",5:"năm",
          6:"sáu",7:"bảy",8:"tám",9:"chín"}

    if n < 10:
        return "không" if n == 0 else dv[n]

    c, d = divmod(n, 10)

    # Đọc hàng chục
    if c == 1:
        chuoi = "mười"
    else:
        chuoi = dv[c] + " mươi"

    # Đọc hàng đơn vị
    if d == 0:
        return chuoi
    elif d == 1 and c > 1:
        return chuoi + " mốt"
    elif d == 5:
        return chuoi + " lăm"
    else:
        return chuoi + " " + dv[d]

# --- Chương trình chính ---
n = int(input("Nhập số n (0–99): "))
if 0 <= n <= 99:
    print("Cách đọc:", doc_so(n))
else:
    print("Vui lòng nhập số có tối đa 2 chữ số!")