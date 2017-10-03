from __future__ import print_function
from os.path import join, dirname, abspath
import datetime, xlrd
from xlrd.sheet import ctype_text

'''
#database 
import MySQLdb
connection=MySQLdb.connect(host="localhost", user="root", passwd="", db="python")
cur=connection.cursor() #establishes connection
cur.execute("create table lfy(ID int NOT NULL AUTO_INCREMENT, LastName varchar(255) NOT NULL,FirstName varchar(255),Age int, PRIMARY KEY (ID))") #create Table
cur.execute("insert into lfy (FirstName,LastName) values('Lars','Monsen')") #Insert to Table
cur.execute("select * from lfy") #Select from the table
multiplerow=cur.fetchall() #fetch all of the results of a query and return in a nested list form
cur.execute("select * from lfy") #must query again since it was the result was already fetched
row=cur.fetchone() #fetch one row at a time
connection.commit() #pushes the values to database
cur.close()
connection.close()
'''

def excel_reader(file):
    # Open the workbook
    xl_workbook = xlrd.open_workbook(file) #location and name of the file

    # List sheet names, and pull a sheet by name
    sheet_names = xl_workbook.sheet_names()
    print('Sheet Names', sheet_names)
    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

    # Or grab the first sheet by index
    xl_sheet = xl_workbook.sheet_by_index(4)
    print ('Sheet name: %s' % xl_sheet.name)

    # Pull the first row by index(rows/columns are also zero-indexed)
    row = xl_sheet.row(4)

    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print('(Column #) type:value')

    #This block of Code gets the subsegment and values of each subsegment in correspondence to Month
    for idx, cell_obj in enumerate(row):
        #only gets the subsegment
        if cell_obj.value != '':
            print('(%s) %s' %(idx, cell_obj.value)) #Prints Subsegment
            mon = 5
            monx = 0
            cur.execute("create table if NOT EXISTS cell_obj.value(ID int NOT NULL AUTO_INCREMENT, name varchar(255), author varchar(40))")
            for xmonth in month:
                print (xmonth) #prints the Month
                mon = mon + monx
                #gets the corresponding subsubsegments to the subsegment
                for x in range(0, 3):
                    ecolumn = idx+x
                    erow = 5
                    cell_obj2 = xl_sheet.cell(erow, ecolumn)
                    print('\t''(%s) %s' %(ecolumn, cell_obj2.value))
                #prints the corresponding values per subsubsegment
                    for y in range(1, 5): #gets the Growth Rate, Actual 2015, Budget, Actual 2014
                        cell_obj3 = xl_sheet.cell(mon+y, ecolumn)
                        cell_obj4 = xl_sheet.cell(erow+y, 2)
                        print('\t' '\t' '(%s) %s: %s' % (erow+y, cell_obj4.value, cell_obj3.value))
                monx = 4
        context={'sheet_names':sheet_names,
                 'xl_sheet.name':xl_sheet.name,
                 'str0':'(%s) %s' %(idx, cell_obj.value),
                }
        return "successful",context