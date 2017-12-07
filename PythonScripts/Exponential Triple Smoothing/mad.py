import numpy as np


def mean_average_deviation(self, prediction_list):
    mean = np.mean(prediction_list)
    mad = 0
    for i in range(len(prediction_list)):
        dev = prediction_list[i] - mean
        if dev < 0:
            dev *= -1
        mad += dev
    mad = mad / len(prediction_list)
    return mad
