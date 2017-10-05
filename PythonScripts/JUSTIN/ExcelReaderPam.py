from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
from xlrd.sheet import ctype_text

#fname = join(dirname(dirname(abspath(__file__))), 'test_data', '2016 ROOMS SEGMENTATION.xlsx')
fname = "2016 ROOMS SEGMENTATION.xlsx"

#open the workbook
xl_workbook = xlrd.open_workbook(fname)

#list sheet names, and pull a sheet by name
sheet_names = xl_workbook.sheet_names()
print('Sheet Names',sheet_names)

xl_sheet = xl_workbook.sheet_by_name(sheet_names[2])
print("Sheet name : %s" % xl_sheet.name)

#pull the first row by index
row = xl_sheet.row(0)

#print first row value and types
print('(Column #) type:value')
for idx,cell_obj in enumerate(row):
    cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
    print('(%s) %s %s' % (idx,cell_type_str,cell_obj.value))
print()

"""
#print all values, iterating through rows and columns
num_cols = xl_sheet.ncols # number of columns
for row_idx in range(0,xl_sheet.nrows): #iterate through rows
    print("-"*40)
    print('Row: %s' % row_idx) #print row number
    for col_idx in range(0,num_cols): #iterate through columns
        cell_obj = xl_sheet.cell(row_idx,col_idx) #get cell object by (r,c)
        print('Column: [%s] cell_obj: [%s]' % (col_idx,cell_obj))"""
