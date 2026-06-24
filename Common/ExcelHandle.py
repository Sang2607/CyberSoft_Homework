from openpyxl import Workbook,load_workbook
import os
#insert
def CreateExcel(FileName,Title,NTL):
    wb = Workbook()
    ws = wb.active
    ws.title = Title
    if len(NTL) > 0:
        for i in NTL:
            ws.append(i)
    wb.save(FileName)

#Append data
def AppendRows(FileName,Title,NTL):
    wb = load_workbook(FileName)
    ws = wb[Title]
    for i in NTL:
        ws.append(i)
    wb.save(FileName)

def SaveFile(FileName,Title,NestedList):
    if os.path.exists(FileName):
        if len(NestedList) == 0:
            print("Lỗi: Vui lòng kiểm tra Data cần thêm")
        else:
            AppendRows(FileName,Title,NestedList)
    else:
        CreateExcel(FileName,Title,NestedList)