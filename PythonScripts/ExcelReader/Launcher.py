from PythonScripts.ExcelReader import  ExcelReader as er

path = '2015 Rooms Segmentation.xlsx'

reader = er.ExcelReader(path)
actual_2015 = reader.store_current_year_values_to_array()
actual_2014 = reader.store_last_year_values_to_array()

print(actual_2014)
