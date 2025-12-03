from tkinter import *

# ===============================
# Các hàm xử lý phép toán
# ===============================
def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ!")

def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ!")

def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ!")

def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không chia cho 0")
        else:
            stringKQ.set(a / b)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ!")

# ===============================
# Thiết lập giao diện
# ===============================
root = Tk()
root.title("Cộng – Trừ – Nhân – Chia")
root.resizable(False, False)

# Căn giữa màn hình khi mở
window_width = 350
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

Label(root, text="Cộng – Trừ – Nhân – Chia", fg="blue", font=("Tahoma", 16)).pack(pady=10)

frameButton = Frame(root)
frameButton.pack(side=LEFT, padx=10, pady=10)

# Button căn đều, chiếm hết chiều rộng frame
Button(frameButton, text="Cộng", width=10, command=congAction).pack(pady=2)
Button(frameButton, text="Trừ", width=10, command=truAction).pack(pady=2)
Button(frameButton, text="Nhân", width=10, command=nhanAction).pack(pady=2)
Button(frameButton, text="Chia", width=10, command=chiaAction).pack(pady=2)

# Frame nhập liệu và kết quả
frameInput = Frame(root)
frameInput.pack(side=RIGHT, padx=10, pady=10)

Label(frameInput, text="Số a:").grid(row=0, column=0, sticky=E, pady=2)
Entry(frameInput, width=15, textvariable=stringA).grid(row=0, column=1, pady=2)

Label(frameInput, text="Số b:").grid(row=1, column=0, sticky=E, pady=2)
Entry(frameInput, width=15, textvariable=stringB).grid(row=1, column=1, pady=2)

Label(frameInput, text="Kết quả:").grid(row=2, column=0, sticky=E, pady=2)
Entry(frameInput, width=15, textvariable=stringKQ, state='readonly').grid(row=2, column=1, pady=2)

Button(frameInput, text="Thoát", width=10, command=root.quit).grid(row=3, column=1, pady=5)

root.mainloop()
