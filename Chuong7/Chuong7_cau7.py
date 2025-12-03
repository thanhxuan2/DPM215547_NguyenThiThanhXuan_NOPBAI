# -*- coding: utf-8 -*-
import xlsxwriter
import os

# ===============================
# PHẦN 1: Tạo file Excel với dữ liệu mẫu
# ===============================
def TaoExcel(path):
    # Tạo workbook và worksheet
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet("SanPham")

    # ===============================
    # Thiết lập cột
    # ===============================
    worksheet.set_column('A:A', 5)   # STT
    worksheet.set_column('B:B', 15)  # Mã SP
    worksheet.set_column('C:C', 20)  # Tên SP
    worksheet.set_column('D:D', 15)  # Số lượng
    worksheet.set_column('E:E', 15)  # Đơn giá

    # Định dạng in đậm cho tiêu đề
    bold = workbook.add_format({'bold': True})

    # ===============================
    # Thêm tiêu đề
    # ===============================
    worksheet.write('A1', 'STT', bold)
    worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
    worksheet.write('C1', 'TÊN SẢN PHẨM', bold)
    worksheet.write('D1', 'SỐ LƯỢNG', bold)
    worksheet.write('E1', 'ĐƠN GIÁ', bold)

    # ===============================
    # Thêm dữ liệu mẫu
    # ===============================
    data = [
        [1, 'SP1', 'Coca', 15, 15000],
        [2, 'SP2', 'Pepsi', 20, 18000],
    ]

    row_start = 1  # vì hàng đầu tiên là tiêu đề
    for i, row_data in enumerate(data):
        for col, value in enumerate(row_data):
            worksheet.write(row_start + i, col, value)

    # ===============================
    # Chèn logo (nếu file tồn tại)
    # ===============================
    logo_path = "logo_UEL.png"
    if os.path.exists(logo_path):
        worksheet.insert_image('B5', logo_path)
        print(f"✅ Logo {logo_path} đã được chèn.")
    else:
        print(f"⚠️ Logo {logo_path} không tìm thấy, bỏ qua chèn logo.")

    # Đóng workbook
    workbook.close()
    print(f"✅ File Excel '{path}' đã được tạo thành công!")

# ===============================
# Chạy chương trình
# ===============================
if __name__ == "__main__":
    TaoExcel("demo.xlsx")
