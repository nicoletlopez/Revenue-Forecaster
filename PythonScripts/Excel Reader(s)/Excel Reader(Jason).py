from __future__ import print_function
from os.path import join, dirname, abspath
import datetime, xlrd, numpy as np
from xlrd.sheet import ctype_text
import sqlite3

conn = sqlite3.connect('sample_db.sqlite3')
cur = conn.cursor()

xl_workbook = xlrd.open_workbook('2015 ROOMS SEGMENTATION.xlsx')  # location and name of the file
sheet_names = xl_workbook.sheet_names()
xl_sheet = xl_workbook.sheet_by_index(4)
print('Sheet name: %s' % xl_sheet.name)
row = xl_sheet.row(4)
ind_or_grp = xl_sheet.row(3)
for iog, cell_obj in enumerate(ind_or_grp):
    if cell_obj.value == 'GROUP':
        group_start = iog
        print('%s' % group_start)
ind_actual = np.zeros((13, 12),
                      dtype=[('subsegment', 'S40'), ('month', 'S40'), ('rns', float), ('arr', float), ('rev', float)])
grp_actual = np.zeros((5, 12), dtype=[('rns', 'f8'), ('arr', 'f8'), ('rev', 'f8')])

ind_actual_last_year = np.zeros((13, 12),
                      dtype=[('subsegment', 'S40'), ('month', 'S40'), ('rns', float), ('arr', float), ('rev', float)])
grp_actual_last_year = np.zeros((5, 12), dtype=[('rns', 'f8'), ('arr', 'f8'), ('rev', 'f8')])

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
print('(Column #) type:value')
unneeded_columns = ['', 'Barter', 'GRAND TOTAL', 'TOTAL GROUP', 'TOTAL INDIVIDUAL', 'SEGMENT NAME',
                    'Qualified Discount', 'Long Staying']

year = xl_sheet.cell(1,1).value.split()[1]
print(year)
#year_row = year_row.split()
#year = year_row[1]
#print(year)


subsegment_column = 0
m = 0
actual_row = 7
actual_row_last_year = 9
for idx, cell_obj in enumerate(row):
    # only gets the subsegment
    subsegment = cell_obj.value  # use .value to get the value (duh)

    if subsegment not in unneeded_columns:  # get the Subsegment (rack, group, etc)
        #print('(%s) %s' % (idx, subsegment))
        mon = 5
        monx = 0
        for month in month_list:  # get the month (January, February etc)
            #print(month)
            ind_actual[subsegment_column, m]['subsegment'] = subsegment
            ind_actual_last_year[subsegment_column, m]['subsegment'] = subsegment
            ind_actual[subsegment_column, m]['month'] = month
            ind_actual_last_year[subsegment_column, m]['month'] = month
            mon = mon + monx
            for x in range(0, 3):  # get the column headers (Room Nights Sold, Average Rm Rate(PHP), Revenue (PHP'000)
                ecolumn = idx + x
                if x == 0:
                    val = 'rns'
                elif x == 1:
                    val = 'arr'
                else:
                    val = 'rev'
                our = xl_sheet.cell(actual_row, ecolumn).value
                our2 = xl_sheet.cell(actual_row_last_year, ecolumn).value
                if isinstance(our,str):
                    our = 0.0
                #print(type(our))
                ind_actual[subsegment_column, m][val] = our
                ind_actual_last_year[subsegment_column, m][val] = our2
                # print(m)
                # print(erow)
            actual_row += 4
            actual_row_last_year += 4
            m += 1
        subsegment_column += 1
        actual_row = 7
        actual_row_last_year += 4
        m = 0

def getDate(month,year):
    thirty_ones = ["January","March","May","July","August","October","December"]
    #thirties = ["February","April","June","September","November"]
    monthMap = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,
                "December":12}
    if month in thirty_ones:
        day = 31
    else:
        day = 30
    month = monthMap.get(month)
    date = "%s-%s-%s" % (year,month,day)
    return date



for main in ind_actual:
    for sub in main:
        segment = sub[0].upper().decode('utf-8').strip()
        month = sub[1].decode('utf-8')
        rns = sub[2]
        arr = sub[3]
        rev = sub[4]
        date = getDate(month,year)
        try:
            seg_id_get_query = "select id from seg_list where name like  '%%%s' limit 1" % segment
            cur.execute(seg_id_get_query)
            seg_id = cur.fetchone()[0]
            print("%s %s %s %s %s %s" % (date, segment, month, rns, arr, rev))
            insert_query = "insert into actual (date,rns,arr,rev,seg_id) values('%s',%s,%s,%s,%s)" % (
            date, rns, arr, rev, seg_id)
            cur.execute(insert_query)
            conn.commit()
        except(Exception):
            print(Exception.__traceback__)
            pass
    print()
conn.close()
