import numpy as np

series = [18561, 14229, 15881, 18939, 17107, 13042, 6652, 5654, 9771, 15759, 20965, 27088, 21089, 17311, 19192, 19429,
          21000, 13573, 16678, 17343, 14320, 15514, 19143, 31602, 23904, 21119, 19746, 22644, 19025, 17196, 17582,
          16439, 16301, 19200, 20529]

factors = [18561, 16450.469166666666, 17850.10845, 19780.04770766667, 18861.94815964667, 13497.089558037736,
           9820.250885589836, 8563.184929919718, 9845.248466785231, 14315.554326941936, 19317.13792852846,
           27620.102051227113, 19411.45130836149, 15466.019521235095, 17785.43801110928, 19463.234047919774,
           19944.623957547108, 14105.67521681582, 13905.708734062267, 14942.856829822622, 15350.252271327325,
           18252.775114446304, 21950.292338366602, 31620.544166513082, 23413.137718812854, 19793.383848461905,
           20676.507329811793, 22726.47046404154, 21298.710548718467, 16719.487946275156, 16264.509667967248,
           16117.56939290324, 16497.770417337975, 19878.681883557907, 23021.112994416468]


def mse(actual, seasonal_factor):
    sum_y = np.mean(seasonal_factor)
    sum_x = np.mean(actual)
    sum_xy = 0
    sum_x_squared = 0
    n = len(actual)

    for ctr in range(len(seasonal_factor)):
        sum_xy += seasonal_factor[ctr] * actual[ctr]
        sum_x_squared += actual[ctr] * actual[ctr]

    a = ((sum_y * sum_x_squared) - (sum_x * sum_xy)) / ((n * sum_x_squared) - (sum_x * sum_x))
    b = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_squared) - (sum_x * sum_x))

    squared_errors = []

    for ctr in range(len(seasonal_factor)):
        y_hat = a + (b * actual[ctr])
        error = seasonal_factor[ctr] - y_hat
        squared_error = error*error
        squared_errors.append(squared_error)

    mean_squared_errors = np.mean(squared_errors)
    return mean_squared_errors


print(mse(series, factors))

