from tkinter import *

# Hàm chuyển năm Dương lịch sang Âm lịch (Can Chi)
def chuyenAction():
    try:
        nam_duong = int(entryNam.get())
        can = (nam_duong + 6) % 10   # Chu kỳ 10 năm
        chi = (nam_duong + 8) % 12   # Chu kỳ 12 năm
        can_list = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
        chi_list = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]
        stringKetQua.set(f"Năm Âm lịch: {can_list[can]} {chi_list[chi]}")
    except ValueError:
        stringKetQua.set("❌ Vui lòng nhập số hợp lệ!")

def xoaAction():
    entryNam.delete(0, END)
    stringKetQua.set("")

# Giao diện Tkinter
root = Tk()
root.title("Chuyển năm Dương -> Âm")
root.geometry("300x150")

Label(root, text="Nhập năm Dương lịch:", font=("Tahoma", 12)).pack(pady=5)
entryNam = Entry(root)
entryNam.pack(pady=5)

Button(root, text="Chuyển", command=chuyenAction, width=10).pack(pady=5)
Button(root, text="Xóa", command=xoaAction, width=10).pack()

stringKetQua = StringVar()
Label(root, textvariable=stringKetQua, font=("Tahoma", 12, "bold"), fg="green").pack(pady=5)

root.mainloop()
