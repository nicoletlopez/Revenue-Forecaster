import sqlite3

import numpy as np
import xlrd


class ExcelReader(object):
    def __init__(self, file_path, sheet_index=4, sub_segments_index=4):
        # initializing xlrd objects
        self.workbook = xlrd.open_workbook(file_path)
        self.sheet = self.workbook.sheet_by_index(sheet_index)
        self.sub_segments = self.sheet.row(sub_segments_index)
        # initializing time data for storing in the database
        self.current_year = self.sheet.cell(1, 1).value.split()[1]
        print(self.current_year)
        self.last_year = int(self.current_year) - 1
        self.month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December']
        # list of unneeded columns to be ignored in the storing loop
        self.unneeded_columns = ['', 'Barter', 'GRAND TOTAL', 'TOTAL GROUP', 'TOTAL INDIVIDUAL', 'SEGMENT NAME',
                                 'Qualified Discount', 'Long Staying']

    def store_current_year_values_to_array(self, actual_row_index=7):  # year relative to the excel file
        # initializing numpy array for storing actual values
        actual_values = np.zeros((13, 12),
                      dtype=[('subsegment', 'S40'), ('month', 'S40'), ('rns', float), ('arr', float), ('rev', float)])
        # initialize array indices
        sub_segment_index = 0
        month_index = 0
        for column, cell_obj in enumerate(self.sub_segments):
            #print(column)
            sub_segment = cell_obj.value
            if sub_segment not in self.unneeded_columns:
                for month in self.month_list:
                    # populating numpy array with subsegment and month values
                    actual_values[sub_segment_index, month_index]['subsegment'] = sub_segment
                    #print("subsegment index: %s     month index: %s" %(sub_segment_index,month_index))
                    actual_values[sub_segment_index, month_index]['month'] = month
                    # populating numpy array with actual values
                    # get the column headers (Room Nights Sold, Average Rm Rate(PHP), Revenue (PHP'000)
                    for x in range(0, 3):
                        metric_index = column + x
                        if x == 0:
                            numpy_column = 'rns'
                        elif x == 1:
                            numpy_column = 'arr'
                        else:
                            numpy_column = 'rev'
                        actual = self.sheet.cell(actual_row_index, metric_index).value
                        # sets actual to 0 if cell has no value
                        if isinstance(actual, str):
                            actual = 0.0
                        actual_values[sub_segment_index, month_index][numpy_column] = actual
                    actual_row_index += 4
                    month_index += 1
                sub_segment_index += 1
                actual_row_index = 7
                month_index = 0
        return actual_values

    def store_last_year_values_to_array(self, actual_last_year_row_index=9):  # year relative to the excel file
        # initializing numpy array for storing actual values
        actual_values_last_year = np.zeros((13, 12),
                      dtype=[('subsegment', 'S40'), ('month', 'S40'), ('rns', float), ('arr', float), ('rev', float)])
        # initialize array indices
        sub_segment_index = 0
        month_index = 0
        for column, cell_obj in enumerate(self.sub_segments):
            sub_segment = cell_obj.value
            if sub_segment not in self.unneeded_columns:
                for month in self.month_list:
                    # populating numpy array with subsegment and month values
                    actual_values_last_year[sub_segment_index, month_index]['subsegment'] = sub_segment
                    actual_values_last_year[sub_segment_index, month_index]['month'] = month
                    # populating numpy array with actual values
                    # get the column headers (Room Nights Sold, Average Rm Rate(PHP), Revenue (PHP'000)
                    for x in range(0, 3):
                        metric_index = column + x
                        if x == 0:
                            numpy_column = 'rns'
                        elif x == 1:
                            numpy_column = 'arr'
                        else:
                            numpy_column = 'rev'
                        actual_last_year = self.sheet.cell(actual_last_year_row_index, metric_index).value
                        if isinstance(actual_last_year, str):
                            actual_last_year = 0.0
                        actual_values_last_year[sub_segment_index, month_index][numpy_column] = actual_last_year
                    actual_last_year_row_index += 4
                    month_index += 1
                sub_segment_index += 1
                actual_last_year_row_index = 9
                month_index = 0
        return actual_values_last_year

    def __get_date(self, month, year):
        thirty_ones = ["January", "March", "May", "July", "August", "October", "December"]
        # thirties = ["February","April","June","September","November"]
        month_map = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                     "September": 9, "October": 10, "November": 11,
                     "December": 12}
        if month in thirty_ones:
            day = 31
        else:
            day = 30
        month = month_map.get(month)
        date = "%s-%s-%s" % (year, month, day)
        return date

    def save_current_year_actual_to_db(self, actual_values):
        conn = sqlite3.connect('sample_db.sqlite3')
        cur = conn.cursor()
        for main in actual_values:
            for sub in main:
                segment = sub[0].upper().decode('utf-8').strip()
                month = sub[1].decode('utf-8')
                rns = sub[2]
                arr = sub[3]
                rev = sub[4]
                date = self.__get_date(month, self.current_year)
                try:
                    seg_id_get_query = "select id from seg_list where name like  '%%%s' limit 1" % segment
                    cur.execute(seg_id_get_query)
                    seg_id = cur.fetchone()[0]
                    insert_query = "insert into actual (date,rns,arr,rev,seg_id) values('%s',%s,%s,%s,%s)" % (
                        date, rns, arr, rev, seg_id)
                    cur.execute(insert_query)
                    conn.commit()
                except(Exception):
                    pass
        conn.close()

    def save_last_year_actual_to_db(self, actual_values_last_year):
        conn = sqlite3.connect('sample_db.sqlite3')
        cur = conn.cursor()
        for main in actual_values_last_year:
            for sub in main:
                segment = sub[0].upper().decode('utf-8').strip()
                month = sub[1].decode('utf-8')
                rns = sub[2]
                arr = sub[3]
                rev = sub[4]
                date = self.__get_date(month, self.last_year)
                try:
                    seg_id_get_query = "select id from seg_list where name like  '%%%s' limit 1" % segment
                    cur.execute(seg_id_get_query)
                    seg_id = cur.fetchone()[0]
                    insert_query = "insert into actual (date,rns,arr,rev,seg_id) values('%s',%s,%s,%s,%s)" % (
                        date, rns, arr, rev, seg_id)
                    cur.execute(insert_query)
                    conn.commit()
                except(Exception):
                    pass
        conn.close()