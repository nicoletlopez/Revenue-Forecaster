import numpy as np

class HoltWinters():
    def initial_trend(self,series,slen):
        sum = 0.0
        for i in range(slen):
            sum += float(series[i + slen] - series[i]) / slen
        return sum / slen

    def initial_seasonal_components(self,series, slen):
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

    def get_constant_values(self,skip=1,place_value = 100):
        #generate list of all constant values
        constants_list = []
        for constant in range(1,101,1):
            constants_list.append(constant/100)

        #generate dictionary of all possible alpha, beta, gamma combinations
        value_dictionary = {}
        counter = 1
        for alpha in constants_list:
            for beta in constants_list:
                for gamma in constants_list:
                    value_dictionary[counter] = [alpha,beta,gamma]
                    counter +=1
        return value_dictionary

    def triple_exponential_smoothing(self,series,slen,n_preds,alpha=0.02,beta=0.7,gamma=0.8):
        result = []
        seasonals = self.initial_seasonal_components(series, slen)
        for i in range(len(series) + n_preds):
            if i == 0:  # initial values
                smooth = series[0]
                trend = self.initial_trend(series, slen)
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

    def optimize(self,series,slen=12,n_preds=1):
        value_dictionary = self.get_constant_values()

        predicted_list = []
        for constant_set_key in value_dictionary:
            predicted_list.append(
                self.triple_exponential_smoothing(series, slen,n_preds, value_dictionary[constant_set_key][0],
                                                   value_dictionary[constant_set_key][0],
                                                   value_dictionary[constant_set_key][0],))

        fitting_list_tuple = []
        for fitting_set in predicted_list:
            fitting_list_tuple.append(fitting_set[0:len(series)])

        sse_list = []
        for tuple in fitting_list_tuple:
            sse_list.append(self.sse(tuple))

        """mad_list = []
        for tuple in fitting_list_tuple:
            mad_list.append(self.mad(tuple))"""

        #FOR SSE
        min_sse = min(sse_list)
        min_sse_index = sse_list.index(min_sse)
        alpha_beta_gamma_list = value_dictionary[min_sse_index]
        print(alpha_beta_gamma_list)
        prediction_list_sse = self.triple_exponential_smoothing(series,slen,n_preds,
                                                            alpha_beta_gamma_list[0],
                                                            alpha_beta_gamma_list[1],
                                                            alpha_beta_gamma_list[2])
        prediction_list_sse = prediction_list_sse[-n_preds:]
        print(prediction_list_sse)

        #FOR MAD
        """min_mad = min(mad_list)
        min_mad_index = mad_list.index(min_mad)
        alpha_beta_gamma_list = value_dictionary[min_mad_index]
        print(alpha_beta_gamma_list)
        prediction_list_mad = self.triple_exponential_smoothing(series,slen,n_preds,
                                                                alpha_beta_gamma_list[0],
                                                                alpha_beta_gamma_list[1],
                                                                alpha_beta_gamma_list[2],)
        prediction_list_mad = prediction_list_mad[-n_preds:]
        print(prediction_list_mad)"""
        return prediction_list_sse
    def sse(self, prediction_list):
        m = np.mean(prediction_list)
        sse = 0
        for i in range(len(prediction_list)):
            dev = prediction_list[i] - m
            sse += (dev * dev)
        return sse

    def mad(self, prediction_list):
        mean = np.mean(prediction_list)
        mad = 0
        for i in range(len(prediction_list)):
            dev = prediction_list[i] - mean
            if dev < 0:
                dev *= -1
            mad += dev
        mad = mad / len(prediction_list)
        return mad

f = HoltWinters()
sample_data = \
    [
        18561,14229,15881,18939,17107,13042,6652,5654,9771,15759,20965,27088,21089,17311,19192,19429,21000,13573,16678,17343,14320,15514,19143,31602,
        23904,21119,19746,22644,19025,17196,17582,16439,16301,19200,20529,#29143
    ]
prediction_list = f.optimize(sample_data,12,12)
