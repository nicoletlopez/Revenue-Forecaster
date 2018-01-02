import numpy as np
from ..fitting import ConstantFitting as cfitting
from tqdm import tqdm

class HoltWinters(object):
    def __init__(self,series,n_preds=1,slen=12):
        """

        :rtype:
        """
        self.series= series
        self.slen = slen
        self.n_preds = n_preds


    def __initial_trend(self):
        sum = 0.0
        for i in range(self.slen):
            sum += float(self.series[i + self.slen] - self.series[i]) / self.slen
        return sum / self.slen

    def __initial_seasonal_components(self):
        seasonals = {}
        season_averages = []
        n_seasons = int(len(self.series) / self.slen)
        # compute season averages
        for j in range(n_seasons):
            season_averages.append(sum(self.series[self.slen * j:self.slen * j + self.slen]) / float(self.slen))
        # compute initial values
        for i in range(self.slen):
            sum_of_vals_over_avg = 0.0
            for j in range(n_seasons):
                sum_of_vals_over_avg += self.series[self.slen * j + i] - season_averages[j]
            seasonals[i] = sum_of_vals_over_avg / n_seasons
        return seasonals

    def get_prediction_tuples(self,start=1,end=101,step=1):
        #generate list of all constant values
        constants_list = []
        for constant in range(start,end,step):
            constants_list.append(constant/100)

        #generate dictionary of all possible alpha, beta, gamma combinations
        self.value_dictionary = {}
        counter = 0
        for alpha in constants_list:
            for beta in constants_list:
                for gamma in constants_list:
                    self.value_dictionary[counter] = [alpha,beta,gamma]
                    counter +=1

        prediction_list = []
        for key in self.value_dictionary:
            prediction_tuple = self.triple_exponential_smoothing(self.value_dictionary[key][0],self.value_dictionary[key][1],self.value_dictionary[key][2])
            prediction_list.append(prediction_tuple)
            """print("%s %s %s" % (self.value_dictionary[key][0],
                  self.value_dictionary[key][1],
                  self.value_dictionary[key][2]))"""
        #print(len(prediction_list))


        print(len(prediction_list))
        return prediction_list

    def triple_exponential_smoothing(self,alpha=0.07,beta=1.0,gamma=1.0):
        result = []
        seasonals = self.__initial_seasonal_components()
        for i in range(len(self.series) + self.n_preds):
            if i == 0:  # initial values
                smooth = self.series[0]
                trend = self.__initial_trend()
                result.append(self.series[0])
                continue
            if i >= len(self.series):  # we are forecasting
                m = i - len(self.series) + 1
                result.append((smooth + m * trend) + seasonals[i % self.slen])
            else:
                val = self.series[i]
                last_smooth, smooth = smooth, alpha * (val - seasonals[i % self.slen]) + (1 - alpha) * (smooth + trend)
                trend = beta * (smooth - last_smooth) + (1 - beta) * trend
                seasonals[i % self.slen] = gamma * (val - smooth) + (1 - gamma) * seasonals[i % self.slen]
                result.append(smooth + trend + seasonals[i % self.slen])
        return result

    #to get SSE, MAD, and MSE of a LIST, use the ConstantFitting class

    #create a list of SSE's find the minumum, and return the prediction list
    def optimize_by_sse(self,prediction_list):
        #instantiate ConstantFitting object
        fitting = cfitting.ConstantFitting()
        #collect all sse values in an array
        sse_list = []
        counter = 0
        for item in prediction_list:
            #include actual data only (the ETS method returns actual + predicted)
            item = item[0:len(self.series)]
            sse = fitting.sse(item)
            sse_list.append(sse)
            #print("%s - %s" % (self.value_dictionary[counter],sse))
            counter += 1

        # for the purpose of having referenceable values, I turned the following into instance variable
        self.min_sse = min(sse_list)
        self.min_sse_index = sse_list.index(self.min_sse)
        self.constants = self.value_dictionary[self.min_sse_index]
        predicted_values = self.triple_exponential_smoothing(self.constants[0],
                                                            self.constants[1],
                                                            self.constants[2])[-self.n_preds:]




        print("Min SSE: %s" % self.min_sse)
        print("Min SSE index: %s" % self.min_sse_index)
        print("Constants: %s" % self.constants)
        print(predicted_values)

        return predicted_values


    def optimize_by_mad(self,prediction_list):
        #instantiate ConstantFittting class
        fitting = cfitting.ConstantFitting()
        #collect all MAD values in an array
        mad_list = []
        counter = 0
        for item in prediction_list:
            #include actual data only (prediction list = actual + forecast values)
            item = item[0:len(self.series)]
            mad = fitting.mad(item)
            mad_list.append(mad)
            #print("%s - %s" % (self.value_dictionary[counter],mad))
            counter +=1
        self.min_mad = min(mad_list)
        self.min_mad_index = mad_list.index(self.min_mad)
        self.constants =  self.value_dictionary[self.min_mad_index]
        predicted_values = self.triple_exponential_smoothing(self.constants[0],
                                                             self.constants[1],
                                                             self.constants[2])[-self.n_preds]
        print("Min MAD: %s " % self.min_mad)
        print("Min MAD index: %s" % self.min_mad_index)
        print("Constants: %s" % self.constants)
        print(predicted_values)

        return predicted_values

    def optimize_by_mse(self, prediction_list):
        # instantiate ConstantFittting class
        fitting = cfitting.ConstantFitting()
        # collect all MSE values in an array
        mse_list = []
        counter = 0
        for item in tqdm(prediction_list):
            # include actual data only (prediction list = actual + forecast values)
            item = item[0:len(self.series)]
            mse = fitting.mse(self.series, item)
            mse_list.append(mse)
            # print("%s - %s" % (self.value_dictionary[counter],mad))
            counter += 1
        self.min_mse = min(mse_list)
        self.min_mse_index = mse_list.index(self.min_mse)
        self.constants = self.value_dictionary[self.min_mse_index]
        predicted_values = self.triple_exponential_smoothing(self.constants[0],
                                                             self.constants[1],
                                                             self.constants[2])[-self.n_preds:]
        print("Min MSE: %s " % self.min_mse)
        print("Min MSE index: %s" % self.min_mse_index)
        print("Constants: %s" % self.constants)
        print(predicted_values)

        return predicted_values


# sample_data = \
#     [
#         18561,14229,15881,18939,17107,13042,6652,5654,9771,15759,20965,27088,21089,17311,19192,19429,21000,13573,16678,17343,14320,15514,19143,31602,
#         23904,21119,19746,22644,19025,17196,17582,16439,16301,19200,20529,#29143
#     ]
# f = HoltWinters(sample_data,12,1)
# g =  f.triple_exponential_smoothing(0.4,0.6,0.3)
# print(g)
"""prediction_tuples = f.get_prediction_tuples()
prediction_list = f.optimize_by_sse(prediction_tuples)
print(f.triple_exponential_smoothing())"""