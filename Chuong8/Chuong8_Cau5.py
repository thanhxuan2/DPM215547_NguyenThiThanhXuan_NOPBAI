from tkinter import *
from tkinter import messagebox

# ===============================
# Hàm xử lý
# ===============================
def okAction():
    old = stringOld.get()
    new = stringNew.get()
    confirm = stringConfirm.get()

    # Kiểm tra dữ liệu
    if not old or not new or not confirm:
        messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
        return

    if new != confirm:
        messagebox.showerror("Lỗi", "Mật khẩu mới không khớp!")
        return

    # Giả sử mật khẩu cũ là "123456" để demo
    if old != "123456":
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")
        return

    messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")
    xoaAction()

def xoaAction():
    stringOld.set("")
    stringNew.set("")
    stringConfirm.set("")

def cancelAction():
    root.destroy()

# ===============================
# Giao diện
# ===============================
root = Tk()
root.title("Eneter New Password")
root.geometry("300x200")
root.resizable(False, False)

# Biến lưu dữ liệu
stringOld = StringVar()
stringNew = StringVar()
stringConfirm = StringVar()

# Tiêu đề
Label(root, text="Enter New Password", font=("Tahoma", 14), fg="blue").pack(pady=5)

# Old Password
frameOld = Frame(root)
frameOld.pack(pady=2, padx=10, fill=X)
Label(frameOld, text="Old Password:", width=22, anchor=W).pack(side=LEFT)
Entry(frameOld, textvariable=stringOld, show="*").pack(side=LEFT, fill=X, expand=True)

# New Password
frameNew = Frame(root)
frameNew.pack(pady=2, padx=10, fill=X)
Label(frameNew, text="New Password:", width=22, anchor=W).pack(side=LEFT)
Entry(frameNew, textvariable=stringNew, show="*").pack(side=LEFT, fill=X, expand=True)

# Confirm Password
frameConfirm = Frame(root)
frameConfirm.pack(pady=0, padx=8, fill=X)
Label(frameConfirm, text="Enter New Password Again:", width=22, anchor=W).pack(side=LEFT)
Entry(frameConfirm, textvariable=stringConfirm, show="*").pack(side=LEFT, fill=X, expand=True)

# Nút OK và Cancel
frameButton = Frame(root)
frameButton.pack(pady=10)
Button(frameButton, text="OK", width=10, command=okAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Cancel", width=10, command=cancelAction).pack(side=LEFT, padx=5)

root.mainloop()
