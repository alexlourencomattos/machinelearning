import pandas as pd
import xlrd
wb = xlrd.open_workbook('25096.XLSX')
y = wb.sheet_by_index(0)
lin = y.nrows
col = y.ncols
numb = y.col_values(0)
name = y.col_values(1)
area = y.col_values(2)
zona = y.col_values(3)
ty = y.col_values(4)
fnvolt = y.col_values(5)
fangle = y.col_values(6)
pbase = y.col_values(7)
mwload = y.col_values(8)
mvarload = y.col_values(9)
mwgenerator = y.col_values(10)
mvargenerator = y.col_values(11)
gpu = y.col_values(12)
bpu = y.col_values(13)
#Line
numk = y.col_values(14)
numl = y.col_values(15)
arealin = y.col_values(16)
zonalin = y.col_values(17)

dados = []
dados.append(numb)
print(numb)
dados.append(name)
print(name)
dados.append(area)
print(area)
dados.append(zona)
print(zona)
dados.append(ty)
print(ty)
dados.append(fnvolt)
print(fnvolt)
