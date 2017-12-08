from PythonScripts.forecasting import HoltWinters2 as hw2
from PythonScripts.forecasting import ConstantFitting as fcast

f = fcast.ConstantFitting()

sample_data = \
    [
        18561,14229,15881,18939,17107,13042,6652,5654,9771,15759,20965,27088,21089,17311,19192,19429,21000,13573,16678,17343,14320,15514,19143,31602,
        23904,21119,19746,22644,19025,17196,17582,16439,16301,19200,20529
    ]

hw = hw2.HoltWinters2(sample_data)

predicted_list = hw.get_prediction_tuples(1,101,1)
optimize = hw.optimize_by_sse(predicted_list)
#optimized = hw.optimize_by_sse(predicted_list)
#print(optimized)



"""pred =hw.triple_exponential_smoothing(0.07,1,1)
print(pred)
print(f.sse(pred[0:len(sample_data)]))"""
#prediction_tuples =  hw.get_prediction_tuples(1,101,1)


#optimized = hw.optimize_by_sse(prediction_tuples)