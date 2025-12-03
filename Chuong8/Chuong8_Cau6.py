from tkinter import *

root = Tk()
root.title("frame2")
root.geometry("700x400")

Label(root, text="Các kiểu Button trong Tkinter", font=("Tahoma", 14, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

# 1. Nút bình thường
Button(frame, text="Normal Button").grid(row=0, column=0, padx=5, pady=5)

# 2. Nút màu nền và chữ
Button(frame, text="Colored", bg="blue", fg="white").grid(row=0, column=1, padx=5, pady=5)

# 3. Nút in đậm chữ và font khác
Button(frame, text="Font Bold", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=5, pady=5)

# 4. Nút viền lõm/nhô (relief)
Button(frame, text="Sunken", relief=SUNKEN).grid(row=1, column=1, padx=5, pady=5)
Button(frame, text="Raised", relief=RAISED).grid(row=2, column=0, padx=5, pady=5)
Button(frame, text="Groove", relief=GROOVE).grid(row=2, column=1, padx=5, pady=5)
Button(frame, text="Ridge", relief=RIDGE).grid(row=3, column=0, padx=5, pady=5)

# 5. Nút với border width
Button(frame, text="Border 5", bd=5).grid(row=3, column=1, padx=5, pady=5)

# 6. Nút với hình ảnh (demo bằng hình built-in)
photo = PhotoImage(width=20, height=20)  # hình trống demo
Button(frame, text="Image Btn", image=photo, compound=LEFT).grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
