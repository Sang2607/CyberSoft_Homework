import bootstrap
from pathlib import Path 
BASE_DIR = Path(__file__).parent.parent
from Common.ExcelHandle import ReadFile

path_File = f"{BASE_DIR}/Files/data_logistics.xlsx"

#Mức phân khối lượng
kl5,kl20 = 5,20

LoaiKhuVuc = {
    "Hà Nội": "Bac",
    "Hải Phòng": "Bac",
    "Đà Nẵng": "Trung",
    "Huế": "Trung",
    "Nha Trang": "Trung",
    "TP.HCM": "Nam",
    "Cần Thơ": "Nam",
    "Vũng Tàu": "Nam",
}
rows ,ws ,wb = ReadFile(path_File,True,2,isMaxRow=True) # cần refactor -> do tốn ram nếu kích thước quá lớn => dùng context manager

def CheckHeader():
    cells = {
    "cell1": "Mã đơn",
    "cell2": "Khách hàng",
    "cell3": "Loại hàng",
    "cell4": "Nơi gửi",
    "cell5": "Nơi nhận",
    "cell6": "Khối lượng (kg)",
    "cell7": "Loại vận chuyển",
    "cell8": "Cước cơ bản (đ/kg)",
    "cell9": "Phí vận chuyển (đ)",
    "cell10": "Phân loại",
    }
    for i in range(1,len(cells) + 1):
        if ws.cell(row=1, column=i).value != cells[f"cell{i}"]:
            ws.cell(row=1, column=i).value = cells[f"cell{i}"]
            print(f"Đã thêm tiêu đề: {ws.cell(row=1, column=i).value}")

def PhanLoaiCuocPhi(tongtien):
    if tongtien > 5000000:
        return "Cao"
    elif tongtien > 200000:
        return "Trung bình"
    else:
        return "Thấp"

def TinhGiaGiam(KhoiLuong,from_location,to_location):
    giamgia = 0
    if KhoiLuong > kl20:
        giamgia = 0.1
    elif  KhoiLuong > kl5:
        giamgia = 0.05
    giamgia += checkLocation(from_location,to_location)
    return giamgia

def TinhCuocPhi():
    for i, row in enumerate(rows, start=2):
        ma_don = row[0]
        #tạo biến local
        khoi_luong = row[5] 
        cuoc_coban = row[7]
        loai_vanchuyen = row[6] 
        from_location = row[3]
        to_location = row[4]
        phi_ban_dau = float(khoi_luong) *  float(cuoc_coban)

        #tính giá giảm
        giamgia = TinhGiaGiam(khoi_luong,from_location,to_location)
        
        #tính tổng tiền
        tongtien = phi_ban_dau * (1-giamgia) # phibandau - phibandau*giamgia 
        if loai_vanchuyen == "Siêu tóc":
            tongtien += 20000

        #save cell
        ws.cell(row=i, column=9).value = tongtien
        ws.cell(row=i, column=10).value = PhanLoaiCuocPhi(tongtien)

        print(f"Mã đơn: {ma_don} có tổng cước phí: {tongtien:,} loại cước phí là:{ws.cell(row=i, column=10).value}")
    wb.save(path_File)
    print("Lưu thành công")

def checkLocation(formLoca,toLoca):
    return 0.05 if(LoaiKhuVuc[formLoca] == LoaiKhuVuc[toLoca]) else 0

if __name__ == "__main__":
    CheckHeader()
    TinhCuocPhi()