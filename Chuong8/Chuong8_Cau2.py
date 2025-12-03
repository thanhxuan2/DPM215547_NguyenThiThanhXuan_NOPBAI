from tkinter import *
from math import sqrt

# ===============================
# Hàm giải phương trình bậc 2
# ===============================
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        if a == 0:  # bx + c = 0
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set(f"x = {x}")
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                stringKQ.set("Vô nghiệm")
            elif delta == 0:
                x = -b / (2 * a)
                stringKQ.set(f"Nghiệm kép x1 = x2 = {x}")
            else:
                x1 = (-b - sqrt(delta)) / (2 * a)
                x2 = (-b + sqrt(delta)) / (2 * a)
                stringKQ.set(f"x1 = {x1}; x2 = {x2}")
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ!")

# ===============================
# Hàm xóa dữ liệu
# ===============================
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

# ===============================
# Thiết lập giao diện Tkinter
# ===============================
root = Tk()
root.title("Giải phương trình bậc 2")
root.resizable(False, False)

# Căn giữa cửa sổ khi mở
window_width = 350
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

Label(root, text="Phương Trình Bậc 2", fg="red", font=("Tahoma", 16)).pack(pady=10)

frameInput = Frame(root)
frameInput.pack(pady=5)

Label(frameInput, text="Hệ số a:").grid(row=0, column=0, sticky=E, padx=5, pady=5)
Entry(frameInput, width=25, textvariable=stringHSA).grid(row=0, column=1, padx=5, pady=5)

Label(frameInput, text="Hệ số b:").grid(row=1, column=0, sticky=E, padx=5, pady=5)
Entry(frameInput, width=25, textvariable=stringHSB).grid(row=1, column=1, padx=5, pady=5)

Label(frameInput, text="Hệ số c:").grid(row=2, column=0, sticky=E, padx=5, pady=5)
Entry(frameInput, width=25, textvariable=stringHSC).grid(row=2, column=1, padx=5, pady=5)

# Frame chứa button, căn giữa toàn bộ
frameButton = Frame(root)
frameButton.pack(pady=10)
Button(frameButton, text="Giải", width=10, command=giaiAction).pack(side=LEFT, padx=10)
Button(frameButton, text="Tiếp", width=10, command=tiepAction).pack(side=LEFT, padx=10)
Button(frameButton, text="Thoát", width=10, command=root.quit).pack(side=LEFT, padx=10)

frameKQ = Frame(root)
frameKQ.pack(pady=5)
Label(frameKQ, text="Kết quả:").grid(row=0, column=0, sticky=E, padx=5)
Entry(frameKQ, width=25, textvariable=stringKQ, state='readonly').grid(row=0, column=1, padx=5)

root.mainloop()
