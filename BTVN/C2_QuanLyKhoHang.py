import bootstrap
from pathlib import Path 
BASE_DIR = Path(__file__).parent.parent
from Common.ExcelHandle import ReadFile

path_File = f"{BASE_DIR}/Files/data_nhap_xuat_kho.xlsx"
#Mức phân loại lợi nhuận
LoiNhuanCao,LoiNhuanTB = 200000,100000

def process(so_luong,don_gia, gia_nhap):

    #Process: tính lợi nhuận
    loi_nhuan = (don_gia - gia_nhap) * so_luong

    # Xác định loại lợi nhuận
    match (True):
        case _ if loi_nhuan > LoiNhuanCao:
            loai_loi_nhuan = "Lợi nhuận cao"
        case _ if loi_nhuan > LoiNhuanTB:
            loai_loi_nhuan = "Lợi nhuận trung bình"
        #sử lý ngoại lệ
        case _ if loi_nhuan == 0:
            loai_loi_nhuan = "Hòa vốn"
        case _ if loi_nhuan < 0:
            loai_loi_nhuan = "Lỗ vốn"
        #trả về trường còn lại
        case _:
            loai_loi_nhuan = "Lợi nhuận thấp"
    return loai_loi_nhuan,loi_nhuan

def Cach1_UpdateProfitToExcel():
    rows ,_ ,wb = ReadFile(path_File,False,2) # cần refactor -> do tốn ram nếu kích thước quá lớn => dùng context manager

    # Đọc dữ liệu từ dòng thứ 2
    for index, row in enumerate(rows):
        #Input: lấy value từng cột tương ứng
        san_pham,so_luong,don_gia, gia_nhap = row[1].value, row[3].value, row[4].value, row[5].value
        LoaiLoiNhuan,LoiNhuan = process(so_luong,don_gia, gia_nhap)
        row[7].value = LoiNhuan
        row[6].value = LoaiLoiNhuan
        print( f"{index + 1}.Sản phẩm: {san_pham}; Phân loại: {LoaiLoiNhuan}; Lợi nhuận: {LoiNhuan:,} ")
    wb.save(path_File)

def Cach2_UpdateProfitToExcel(): #dùng ws.cell
    rows ,ws ,wb = ReadFile(path_File,True,2)

    for index, row in enumerate(rows,start=1): #start chỉ làm ảnh hưởng tới value bắt đầu của index 
        # print(row)
        san_pham,so_luong,don_gia, gia_nhap = row[1], row[3], row[4], row[5]
        LoaiLoiNhuan,LoiNhuan = process(so_luong,don_gia, gia_nhap)
        ws.cell(row=index, column=7).value = LoaiLoiNhuan
        ws.cell(row=index, column=8).value = LoiNhuan
        print( f"{index}.Sản phẩm: {san_pham}; Phân loại: {LoaiLoiNhuan}; Lợi nhuận: {LoiNhuan:,} ")

    wb.save(path_File)

if __name__ == "__main__":
    #cách 1 sử lý iter_rows: values_only = false
    #Cach1_UpdateProfitToExcel() 

    #cách 2 sử lý iter_rows: values_only = true
    Cach2_UpdateProfitToExcel()

    print("Hoàn thành!")

    

