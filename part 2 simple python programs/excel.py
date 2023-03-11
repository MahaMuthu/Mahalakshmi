import openpyxl
workbook=openpyxl.Workbook()
sheet=workbook.active
sheet["A1"]="Name"
sheet["B1"]="Age"
sheet["A2"]="John"
sheet["B2"]=30
workbook.save("example.xlsx")