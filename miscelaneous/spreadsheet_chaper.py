import openpyxl
wb = openpyxl.load_workbook('example.xlsx')

#print(wb.get_sheet_names())
#sheet = wb.get_sheet_by_name('Sheet3')
#print (sheet.title)
#print(type(sheet))

#anothersheet = wb.get_active_sheet()
#print(anothersheet)

sheet = wb.get_sheet_by_name('Sheet1')
