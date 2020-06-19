import pandas as pd
import xlrd
wb = xlrd.open_workbook('25096.XLSX')
y = wb.sheet_by_index(0)
lin = y.nrows
col = y.ncols
numb = y.col_values(0)
nome = y.col_values(1)
dados = []
dados.append(numb)
dados.append(nome)
print(numb)
print(nome)