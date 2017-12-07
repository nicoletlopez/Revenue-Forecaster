import numpy as np

class Forecast(object):
    def average(self,series):
        return float(sum(series))/len(series)

    def moving_average(self,series,n):
        return self.average(series[-n:])

    def weighted_average(self,series,weights):
        result = 0
        weights.reverse()
        for n in range(len(weights)):
            result += series[-n-1] * weights[n]
        return result

    def exponential_smoothing(self,series,alpha):
        result = [series[0]]
        for n in range(1, len(series)):
            result.append(alpha * series[n] + (1-alpha) * result[n-1])
        return result

    def double_exponential_smoothing(self,series,alpha,beta):
        result = [series[0]]
        for n in range(1,len(series)+1):
            if n==1:
                level,trend = series[0], series[1] - series[0]
            if n >= len(series):
                value = result[-1]
            else:
                value = series[n]
            last_level, level = level, alpha * value + (1-alpha) * (level + trend)
            trend = beta * (level-last_level) + (1-beta) * trend
        return result
    def triple_exponential_smoothing(self,series,slen,alpha,beta,gamma,n_preds):
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
        return result
    def sse(self,prediction_list):
        m = np.mean(prediction_list)
        sse = 0
        for i in range(len(prediction_list)):
            dev = prediction_list[i] - m
            sse += (dev * dev)
        return sse
"""
n = Forecast()
h = [900,800,700,12]
print(n.sse(h))
"""