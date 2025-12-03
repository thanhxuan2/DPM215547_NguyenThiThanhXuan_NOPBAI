from tkinter import *
from tkinter import messagebox

# Hàm tính BMI
def tinhBMI():
    try:
        height = float(entryChieuCao.get()) / 100  # cm -> m
        weight = float(entryCanNang.get())
        bmi = weight / (height ** 2)
        stringBMI.set(f"{bmi:.2f}")

        # Xác định tình trạng cân nặng
        if bmi < 18.5:
            stringTinhTrang.set("Gầy")
        elif 18.5 <= bmi <= 24.9:
            stringTinhTrang.set("Bình thường")
        elif 25 <= bmi <= 29.9:
            stringTinhTrang.set("Thừa cân")
        else:
            stringTinhTrang.set("Béo phì")
    except ValueError:
        stringBMI.set("❌ Nhập số hợp lệ!")
        stringTinhTrang.set("")

# Hàm cảnh báo nguy cơ bệnh
def nguyCoBenh():
    try:
        bmi = float(stringBMI.get())
        if bmi < 18.5:
            messagebox.showinfo("Nguy cơ sức khỏe", "Nguy cơ phát triển bệnh: Thấp")
        elif 18.5 <= bmi <= 24.9:
            messagebox.showinfo("Nguy cơ sức khỏe", "Nguy cơ phát triển bệnh: Trung bình")
        elif 25 <= bmi <= 29.9:
            messagebox.showinfo("Nguy cơ sức khỏe", "Nguy cơ phát triển bệnh: Cao")
        else:
            messagebox.showinfo("Nguy cơ sức khỏe", "Nguy cơ phát triển bệnh: Rất cao")
    except ValueError:
        messagebox.showwarning("Lỗi", "Vui lòng tính BMI trước!")

def thoat():
    root.destroy()

# Giao diện
root = Tk()
root.title("Tính BMI")
root.geometry("350x300")
root.configure(bg="#FFFACD")  # nền vàng nhạt

# Label và Entry Chiều cao
Label(root, text="Nhập chiều cao (cm):", bg="#FFFACD", font=("Tahoma", 12)).pack(pady=5)
entryChieuCao = Entry(root, bg="white", fg="red", font=("Tahoma", 12))
entryChieuCao.pack(pady=5)

# Label và Entry Cân nặng
Label(root, text="Nhập cân nặng (kg):", bg="#FFFACD", font=("Tahoma", 12)).pack(pady=5)
entryCanNang = Entry(root, bg="white", fg="red", font=("Tahoma", 12))
entryCanNang.pack(pady=5)

# Button Tính BMI, Nguy cơ, Thoát
frameButton = Frame(root, bg="#FFFACD")
Button(frameButton, text="Tính BMI", bg="#0066CC", fg="white", width=12, command=tinhBMI).pack(side=LEFT, padx=5, pady=10)
Button(frameButton, text="Nguy cơ phát triển bệnh", bg="#0066CC", fg="white", width=20, command=nguyCoBenh).pack(side=LEFT, padx=5, pady=10)
Button(frameButton, text="Thoát", bg="#0066CC", fg="white", width=12, command=thoat).pack(side=LEFT, padx=5, pady=10)
frameButton.pack()

# Hiển thị kết quả BMI
Label(root, text="BMI:", bg="#FFFACD", font=("Tahoma", 12)).pack()
stringBMI = StringVar()
Entry(root, textvariable=stringBMI, bg="white", fg="red", font=("Tahoma", 12), state="readonly").pack(pady=5)

# Hiển thị tình trạng cân nặng
Label(root, text="Tình trạng cân nặng:", bg="#FFFACD", font=("Tahoma", 12)).pack()
stringTinhTrang = StringVar()
Entry(root, textvariable=stringTinhTrang, bg="white", fg="red", font=("Tahoma", 12), state="readonly").pack(pady=5)

root.mainloop()
