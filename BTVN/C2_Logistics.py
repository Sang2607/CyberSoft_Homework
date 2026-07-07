import bootstrap
from pathlib import Path 
BASE_DIR = Path(__file__).parent.parent
from Common.ExcelHandle import ReadFile

path_File = f"{BASE_DIR}/Files/data_logistics.xlsx"

#Mức phân khối lượng
kl5,kl10 = 5,20

MucGiam = 0
LoaiVanChuyen = {"Siêu tốc":20000}
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
def CheckHeader():
    rows ,_ ,wb = ReadFile(path_File,False,1) # cần refactor -> do tốn ram nếu kích thước quá lớn => dùng context manager
    cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10 = "Mã đơn","Khách hàng","Loại hàng"	,"Nơi gửi"	,"Nơi nhận","Khối lượng (kg)",	"Loại vận chuyển",	"Cước cơ bản (đ/kg)","Phí vận chuyển (đ)","Phân loại"

    print(rows[0])

def Cach1_UpdateProfitToExcel():
    # rows ,_ ,wb = ReadFile(path_File,False,2) # cần refactor -> do tốn ram nếu kích thước quá lớn => dùng context manager

    # # Đọc dữ liệu từ dòng thứ 2
    # for index, row in enumerate(rows):
    #     #Input: lấy value từng cột tương ứng
    #     # san_pham,so_luong,don_gia, gia_nhap = row[1].value, row[3].value, row[4].value, row[5].value
    #     # row[7].value = LoiNhuan
    #     # row[6].value = LoaiLoiNhuan
    #     # print( f"{index + 1}.Sản phẩm: {san_pham}; Phân loại: {LoaiLoiNhuan}; Lợi nhuận: {LoiNhuan:,} ")
    # wb.save(path_File)
    pass

CheckHeader()