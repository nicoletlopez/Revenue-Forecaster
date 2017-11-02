import pandas
from openpyxl import load_workbook

book = load_workbook('2015 Rooms Segmentation.xlsx')
writer = pandas.ExcelWriter('2016 Rooms Segmentation with Budget Forecast.xlsx', engine='openpyxl')

writer.write_cells('9D', 200)

writer.save()