from openpyxl import Workbook

wb=Workbook()
ws=wb.active

ws.append([1,1,0,0])
ws.append([0,1,1,0])
ws.append([1,1,0,1])

for row in ws.iter_rows():
    for cell in row:
        valor = cell.value
        indice = cell.coordinate
        print(valor,indice)