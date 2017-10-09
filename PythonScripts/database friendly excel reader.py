from __future__ import print_function
from os.path import join, dirname, abspath
import datetime, xlrd, numpy as np
from xlrd.sheet import ctype_text
import sqlite3

# Open the workbook
xl_workbook = xlrd.open_workbook('2015 ROOMS SEGMENTATION.xlsx')  # location and name of the file

# List sheet names, and pull a sheet by name
sheet_names = xl_workbook.sheet_names()
# print('Sheet Names', sheet_names)
# xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

# Get a sheet by sheet index (starts with 0)
# Relevant sheet is the fifth one (index 5) Andrey says the other sheets
# were probably links
xl_sheet = xl_workbook.sheet_by_index(4)
print('Sheet name: %s' % xl_sheet.name)

# Get a row by index
row = xl_sheet.row(4)

# Gets the row to determine whether individual or group
ind_or_grp = xl_sheet.row(3)

for iog, cell_obj in enumerate(ind_or_grp):
    if cell_obj.value == 'GROUP':
        group_start = iog
        print('%s' % group_start)

ind_actual = np.zeros((13, 12),
                      dtype=[('subsegment', 'S20'), ('month', 'S10'), ('rns', float), ('arr', float), ('rev', float)])
grp_actual = np.zeros((5, 12), dtype=[('rns', 'f4'), ('arr', 'f4'), ('rev', 'f4')])
# ind_actual[0,0]['rns'] = 1231
# print(ind_actual)

# Since the months can't be read, we just put them in an array instead :P
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
print('(Column #) type:value')

# You can comment this out if you think that we need these columns
unneeded_columns = ['', 'Barter', 'GRAND TOTAL', 'TOTAL GROUP', 'TOTAL INDIVIDUAL', 'SEGMENT NAME',
                    'Qualified Discount', 'Long Staying']

ss = 0
m = 0
erow = 7

# This block of Code gets the subsegment and values of each subsegment in correspondence to Month
for idx, cell_obj in enumerate(row):
    # only gets the subsegment
    subsegment = cell_obj.value  # use .value to get the value (duh)
    if subsegment not in unneeded_columns:  # get the Subsegment (rack, group, etc)
        #print('(%s) %s' % (idx, subsegment))
        mon = 5
        monx = 0
        for month in month_list:  # get the month (January, February etc)
            #print(month)
            ind_actual[ss, m]['subsegment'] = subsegment
            ind_actual[ss, m]['month'] = month
            mon = mon + monx
            for x in range(0, 3):  # get the column headers (Room Nights Sold, Average Rm Rate(PHP), Revenue (PHP'000)
                ecolumn = idx + x
                if x == 0:
                    val = 'rns'
                elif x == 1:
                    val = 'arr'
                else:
                    val = 'rev'
                our = xl_sheet.cell(erow, ecolumn).value
                if isinstance(our,str):
                    our = 0.0
                #print(type(our))
                ind_actual[ss, m][val] = our
                # print(m)
                # print(erow)
            erow += 4
            m += 1
        ss += 1
        erow = 7
        m = 0

print(ind_actual)
