from tkinter import *

# ===============================
# Hàm xử lý nút "Tiếp"
# ===============================
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

# ===============================
# Hàm giải phương trình
# ===============================
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        if a == 0 and b == 0:
            stringKQ.set("Vô số nghiệm")
        elif a == 0 and b != 0:
            stringKQ.set("Vô nghiệm")
        else:
            x = -b / a
            stringKQ.set(f"x = {x}")
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ!")

# ===============================
# Giao diện Tkinter
# ===============================
root = Tk()
root.title("Giải phương trình bậc 1 - facebook.com/duythanhcse")
root.minsize(height=150, width=300)
root.resizable(height=True, width=True)

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

Label(root, text="Phương Trình Bậc 1", fg="red", font=("Tahoma", 16), justify=CENTER).grid(row=0, columnspan=2, pady=5)

Label(root, text="Hệ số a:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Hệ số b:").grid(row=2, column=0, padx=5, pady=5, sticky=E)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1, padx=5, pady=5)

frameButton = Frame(root)
Button(frameButton, text="Giải", width=10, command=giaiAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Tiếp", width=10, command=tiepAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", width=10, command=root.quit).pack(side=LEFT, padx=5)
frameButton.grid(row=3, columnspan=2, pady=10)

Label(root, text="Kết quả:").grid(row=4, column=0, padx=5, pady=5, sticky=E)
Entry(root, width=30, textvariable=stringKQ, state='readonly').grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
