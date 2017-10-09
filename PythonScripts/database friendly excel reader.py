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
                      dtype=[('subsegment', 'S40'), ('month', 'S10'), ('rns', float), ('arr', float), ('rev', float)])
grp_actual = np.zeros((5, 12), dtype=[('rns', 'f4'), ('arr', 'f4'), ('rev', 'f4')])

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
print('(Column #) type:value')
unneeded_columns = ['', 'Barter', 'GRAND TOTAL', 'TOTAL GROUP', 'TOTAL INDIVIDUAL', 'SEGMENT NAME',
                    'Qualified Discount', 'Long Staying']

ss = 0
m = 0
erow = 7
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


year = 2015
def getDate(month,year):
    thirty_ones = ["January","March","May","July","August","October","December"]
    #thirties = ["February","April","June","September","November"]
    if month in thirty_ones:
        day = 31
    else:
        day = 30
    date = "%s-%s-%s" % (year,month,day)

for main in ind_actual:
    for sub in main:
        segment = sub[0].upper().decode('utf-8')
        month = sub[1].decode('utf-8')
        rns = sub[2]
        arr = sub[3]
        rev = sub[4]
        date = getDate(month,year)
        seg_id_get_query = "select id from seg_list where name like '%s' limit 1" % segment
        seg_id =  cur.execute(seg_id_get_query).fetchall()
        print(seg_id)
        print("%s %s %s %s %s" % (segment,month,rns,arr,rev))
    print()
"""for main in ind_actual:
    for sub_main in ind_actual:
        for sub_sub_main in sub_main:
            for record in sub_sub_main:
                try:
                    print(record.decode('utf-8'))
                except:
                    print(record)
                segment_name = sub_sub_main[0]#.decode('utf-8').upper()
                month = sub_sub_main[1].decode('utf-8')
                rns = sub_sub_main[2]
                arr = sub_sub_main[3]
                rev = sub_sub_main[4]
                date = getDate(month,year)
                seg_id_query = "select id from seg_list where name like '%%s' limit 1" % segment_name
                seg_id = cur.execute(seg_id_query)
                for column in seg_id:
                    print(str(column))
                #print("%s %s" % (segment_name,seg_id))
                               #"values(%s %s %s %s %s)" % (segment_name,seg_id,month,rns,arr,rev,)
print(counter)
"""
conn.close()