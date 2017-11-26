import sqlite3
from PythonScripts.forecasting import forecasting as f

fcast = f.Forecast()

sample_data = \
    [
        18561,14229,15881,18939,17107,13042,6652,5654,9771,15759,20965,27088,21089,17311,19192,19429,21000,13573,16678,17343,14320,15514,19143,31602,
        23904,21119,19746,22644,19025,17196,17582,16439,16301,19200,20529
    ]

prediction_list = fcast.triple_exponential_smoothing(sample_data,
                                                     12,
                                                     0.07,
                                                     1.0,
                                                     1.0,
                                                     1)
print(prediction_list[-1:])