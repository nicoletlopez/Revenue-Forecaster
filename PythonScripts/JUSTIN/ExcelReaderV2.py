from __future__ import print_function
from os.path import join, dirname, abspath
import datetime, xlrd
from xlrd.sheet import ctype_text

month = ['January', 'February', 'March', 'April',
         'May', 'June', 'July', 'August',
         'September', 'October', 'November', 'December']

xl_workbook = xlrd.open_workbook('2016 ROOMS SEGMENTATION.xlsx')

sheet_names = xl_workbook.sheet_names()
print('Sheet Names ' , sheet_names)

xl_sheet = xl_workbook.sheet_by_index(4)
print('Sheet name: %s' % xl_sheet.name)

row = xl_sheet.row(4)

num_cols = xl_sheet.ncols

for cell_obj in enumerate(row):
    print(cell_obj.value)