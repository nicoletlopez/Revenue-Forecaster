from __future__ import print_function
from os.path import join, dirname, abspath
import datetime, xlrd
from xlrd.sheet import ctype_text
import sqlite3

def saveInTuple(dictionary_object):
    return dictionary_object

xl_workbook = xlrd.open_workbook('2015 ROOMS SEGMENTATION.xlsx') #location and name of the file
sheet_names = xl_workbook.sheet_names()
xl_sheet = xl_workbook.sheet_by_index(4)
print ('Sheet name: %s' % xl_sheet.name)
row = xl_sheet.row(4)
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print('(Column #) type:value')
unneeded_columns = ['','GRAND TOTAL','TOTAL GROUP','TOTAL INDIVIDUAL','SEGMENT NAME']

#This block of Code gets the subsegment and values of each subsegment in correspondence to Month
results_dict = {}
results_tuple = []
for idx, cell_obj in enumerate(row):
    #only gets the subsegment
    subsegment = cell_obj.value #use .value to get the value (duh)
    if subsegment not in unneeded_columns: #get the Subsegment (rack, group, etc)
        print('(%s) %s' %(idx, subsegment))
        mon = 5
        monx = 0
        results_dict["Subsegment"] = subsegment.upper()
        for month in month_list: # get the month (January, February etc)
            print (month)
            mon = mon + monx
            results_dict["Month"] = month
            results_dict["Values"] = []
            append_counter = 0
            for x in range(0, 3): # get the column headers (Room Nights Sold, Average Rm Rate(PHP), Revenue (PHP'000)
                ecolumn = idx+x
                erow = 5
                column_header = xl_sheet.cell(erow, ecolumn).value
                print('\t''(%s) %s' % (ecolumn, column_header))
                for y in range(2, 3): #get the Growth Rate, Actual 2015, Budget, Actual 2014 and their respective values
                    intersect_value = xl_sheet.cell(mon + y, ecolumn).value #the value within the cell
                    if intersect_value is '':
                        intersect_value = 0.0
                    row_title = xl_sheet.cell(erow + y, 2).value # the row names themselves(see the comment before the last one)
                    print('\t' '\t' '(%s) %s: %s' % (erow + y, row_title, intersect_value))
                    print("Intersect value: %s" % intersect_value)
                    results_dict["Values"].append(intersect_value)
            #for key, object in results_dict.items():
            #    print("%s %s" % (key, object))
"""for row in results_tuple:
    print(row)"""
    #for key, value in row.items():
     #   print("%s %s" % (key,value))
