import openpyxl
path="C:\Book.xlsx"

workbook = openpyxl.load_workbook(path)
#sheet = workbook.active
sheet=workbook.get_sheet_by_name("EMPTY SHEET")


for r in range(1,5):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value="welcome writing data"

workbook.save(path)


