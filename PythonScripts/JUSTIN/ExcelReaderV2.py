from __future__ import print_function
from os.path import join, dirname, abspath
import datetime, xlrd
from xlrd.sheet import ctype_text

month_list = ['January', 'February', 'March', 'April',
         'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December']

workbook = xlrd.open_workbook('2016 ROOMS SEGMENTATION.xlsx')
sheet_names = workbook.sheet_names()
counter = 0
for item in sheet_names:
    print ("%s " % counter + item)
    counter+=1

xl_sheet = workbook.sheet_by_index(4)
row = xl_sheet.row(4)

for idx, cell_obj in enumerate(row):
    if cell_obj.value != '':
        print ('(%s) %s' % (idx,cell_obj.value))