import numpy as np

from PythonScripts.ExcelReader import ExcelReader as er

path = '2016 ROOMS SEGMENTATION.xlsx'

reader = er.ExcelReader(path)
reader.store_room_nights_available_to_array()

# actual_2015 = reader.store_current_year_values_to_array()
# actual_2014 = reader.store_last_year_values_to_array()


# def numpy_to_native_convert(data_object):
#     if type(data_object) == 'numpy.float64':
#         return np.float(data_object)
#     elif type(data_object) == 'numpy.bytes_':
#         return np.str_(data_object)
#
#
# for tuples in actual_2015:
#     for single_array in tuples:
#         segment = (single_array[0].decode("utf-8")).upper()
#         date = single_array[1].decode("utf-8")
#         rns = float(single_array[2])
#         arr = float(single_array[3])
#         rev = float(single_array[4])
#         print("%s - %s, %s - %s, %s - %s, %s - %s, %s - %s" % (segment,type(segment),date,type(date),rns,type(rns),arr,type(arr),rev,type(rev)))
# """for item in actual_2015:
#     for sub in item:
#         for actual in sub:
#             try:
#                 print(str(actual.decode("utf-8")))
#             except:
#                 print(float(actual))"""
