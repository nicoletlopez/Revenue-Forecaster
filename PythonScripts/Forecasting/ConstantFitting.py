import numpy as np

class ConstantFitting(object):

    def sse(self,prediction_list):
        m = np.mean(prediction_list)
        sse = 0
        for i in range(len(prediction_list)):
            dev = prediction_list[i] - m
            sse += (dev * dev)
        return sse

    def mad(self,prediction_list):
        mean = np.mean(prediction_list)
        mad = 0
        for i in range(len(prediction_list)):
            dev = prediction_list[i] - mean
            if dev < 0:
                dev *= -1
            mad += dev
        mad = mad / len(prediction_list)
        return mad

    def mse(self, actual, seasonal_factor):
        sum_y = np.mean(seasonal_factor)
        sum_x = np.mean(actual)
        sum_xy = 0
        sum_x_squared = 0
        n = len(actual)

        for ctr in range(n):
            sum_xy += seasonal_factor[ctr] * actual[ctr]
            sum_x_squared += actual[ctr] * actual[ctr]

        a = ((sum_y * sum_x_squared) - (sum_x * sum_xy)) / ((n * sum_x_squared) - (sum_x * sum_x))
        b = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_squared) - (sum_x * sum_x))

        squared_errors = []

        for ctr in range(n):
            y_hat = a + (b * actual[ctr])
            error = seasonal_factor[ctr] - y_hat
            squared_error = error * error
            squared_errors.append(squared_error)

        mean_squared_errors = np.mean(squared_errors)
        return mean_squared_errors

    def mse2(self,prediction_list):
        m = np.mean(prediction_list)
        squared_errors = []
        mse2 = 0;
        for i in range(len(prediction_list)):
            error = prediction_list[i] - m
            squared_error = error * error
            squared_errors.append(squared_error)
            mse2 = np.mean(squared_errors)

        return mse2
