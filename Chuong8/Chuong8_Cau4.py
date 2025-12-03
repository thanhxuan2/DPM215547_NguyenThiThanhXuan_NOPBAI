from tkinter import *

# ===============================
# Hàm xử lý
# ===============================
def nhapSo(so):
    current = stringKQ.get()
    stringKQ.set(current + str(so))

def phepToan(op):
    global phep, so1
    try:
        so1 = float(stringKQ.get())
        phep = op
        stringKQ.set("")
    except ValueError:
        stringKQ.set("Nhập số hợp lệ!")

def bangAction():
    global phep, so1
    try:
        so2 = float(stringKQ.get())
        if phep == '+':
            stringKQ.set(so1 + so2)
        elif phep == '-':
            stringKQ.set(so1 - so2)
        elif phep == '*':
            stringKQ.set(so1 * so2)
        elif phep == '/':
            if so2 == 0:
                stringKQ.set("Không chia 0")
            else:
                stringKQ.set(so1 / so2)
    except ValueError:
        stringKQ.set("Nhập số hợp lệ!")

def xoaAction():
    stringKQ.set("")

# ===============================
# Giao diện
# ===============================
root = Tk()
root.title("Máy tính bỏ túi")
root.resizable(False, False)
root.geometry("250x350")

stringKQ = StringVar()

# Hiển thị kết quả
Entry(root, textvariable=stringKQ, font=("Tahoma", 16), bd=5, relief=RIDGE, justify=RIGHT).pack(fill=X, padx=5, pady=5)

# Khung chứa các nút
frame = Frame(root)
frame.pack(padx=5, pady=5)

# Danh sách nút
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['C']
]

# Tạo các nút
for r, row in enumerate(buttons):
    for c, btn in enumerate(row):
        if btn.isdigit() or btn == '.':
            Button(frame, text=btn, width=5, height=2, command=lambda b=btn: nhapSo(b)).grid(row=r, column=c, padx=2, pady=2)
        elif btn in '+-*/':
            Button(frame, text=btn, width=5, height=2, command=lambda b=btn: phepToan(b)).grid(row=r, column=c, padx=2, pady=2)
        elif btn == '=':
            Button(frame, text=btn, width=5, height=2, command=bangAction).grid(row=r, column=c, padx=2, pady=2)
        elif btn == 'C':
            Button(frame, text=btn, width=23, height=2, command=xoaAction).grid(row=r, column=0, columnspan=4, padx=2, pady=2)

root.mainloop()
