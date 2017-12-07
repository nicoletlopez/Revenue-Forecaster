import numpy

series = [18561, 14229, 15881, 18939, 17107, 13042, 6652, 5654, 9771, 15759, 20965, 27088, 21089, 17311, 19192, 19429,
          21000, 13573, 16678, 17343, 14320, 15514, 19143, 31602, 23904, 21119, 19746, 22644, 19025, 17196, 17582,
          16439, 16301, 19200, 20529]


def initial_trend(series, slen):
    sum = 0.0
    for i in range(slen):
        sum += float(series[i + slen] - series[i]) / slen
    return sum / slen


def initial_seasonal_components(series, slen):
    seasonals = {}
    season_averages = []
    n_seasons = int(len(series) / slen)
    # compute season averages
    for j in range(n_seasons):
        season_averages.append(sum(series[slen * j:slen * j + slen]) / float(slen))
    # compute initial values
    for i in range(slen):
        sum_of_vals_over_avg = 0.0
        for j in range(n_seasons):
            sum_of_vals_over_avg += series[slen * j + i] - season_averages[j]
        seasonals[i] = sum_of_vals_over_avg / n_seasons
    return seasonals


def triple_exponential_smoothing(series, slen, alpha, beta, gamma, n_preds):
    result = []
    seasonals = initial_seasonal_components(series, slen)
    for i in range(len(series) + n_preds):
        if i == 0:  # initial values
            smooth = series[0]
            trend = initial_trend(series, slen)
            result.append(series[0])
            continue
        if i >= len(series):  # we are forecasting
            m = i - len(series) + 1
            result.append((smooth + m * trend) + seasonals[i % slen])
        else:
            val = series[i]
            last_smooth, smooth = smooth, alpha * (val - seasonals[i % slen]) + (1 - alpha) * (smooth + trend)
            trend = beta * (smooth - last_smooth) + (1 - beta) * trend
            seasonals[i % slen] = gamma * (val - smooth) + (1 - gamma) * seasonals[i % slen]
            result.append(smooth + trend + seasonals[i % slen])
    return result[len(result) - 1]


def sum_squared_error(series):
    m = numpy.mean(series)
    sse = 0
    for i in range(len(series)):
        dev = series[i] - m
        sse += (dev * dev)
    return sse


print(triple_exponential_smoothing(series, 12, 0.2, 0.1, 0.25, 1))
