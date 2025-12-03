from tkinter import *

# Hàm chuyển F -> C
def chuyenAction():
    try:
        f = float(entryF.get())
        c = (f - 32) * 5/9
        stringKetQua.set(f"{c:.2f} °C")
    except ValueError:
        stringKetQua.set("❌ Nhập số hợp lệ!")

def xoaAction():
    entryF.delete(0, END)
    stringKetQua.set("")

# Giao diện
root = Tk()
root.title("Chuyển độ F -> C")
root.geometry("300x180")
root.configure(bg="#FFD700")  # nền vàng

# Label Nhập độ F
Label(root, text="Nhập độ F:", bg="#FFD700", font=("Tahoma", 12)).pack(pady=5)
entryF = Entry(root, bg="white", fg="red", font=("Tahoma", 12))
entryF.pack(pady=5)

# Nút chuyển và xóa
frameButton = Frame(root, bg="#FFD700")
Button(frameButton, text="Chuyển", bg="lightblue", width=10, command=chuyenAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Xóa", bg="lightblue", width=10, command=xoaAction).pack(side=LEFT, padx=5)
frameButton.pack(pady=10)

# Label Kết quả
Label(root, text="Độ C:", bg="#FFD700", font=("Tahoma", 12)).pack()
stringKetQua = StringVar()
Entry(root, textvariable=stringKetQua, bg="white", fg="red", font=("Tahoma", 12), state="readonly").pack(pady=5)

root.mainloop()
