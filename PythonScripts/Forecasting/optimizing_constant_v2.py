from PythonScripts.forecasting import forecasting as f

fcast = f.Forecast()
"""sample_data = [30,21,29,31,40,48,53,47,37,39,31,29,17,9,20,24,27,35,41,38,
          27,31,27,26,21,13,21,18,33,35,40,36,22,24,21,20,17,14,17,19,
          26,29,40,31,20,24,18,26,17,9,17,21,28,32,46,33,23,28,22,27,
          18,8,17,21,31,34,44,38,31,30,26,32]"""
#from the excel file
sample_data = \
    [
        18561,14229,15881,18939,17107,13042,6652,5654,9771,15759,20965,27088,21089,17311,19192,19429,21000,13573,16678,17343,14320,15514,19143,31602,
        23904,21119,19746,22644,19025,17196,17582,16439,16301,19200,20529
    ]
actual_value = 29143 #for period number 36

prediction_count = 1
seasons = 12

#populate values list
constant_values = []
for x in range(1,101,1):
    constant_values.append(x/100)

#create a value dictionary ( 1:[alpha0,beta0,gamma0],2:...
value_dictionary ={}
counter = 1
for alpha_value in constant_values:
    for beta_value in constant_values:
        for gamma_value in constant_values:
            value_dictionary[counter] = [alpha_value,beta_value,gamma_value]
            counter+=1
#print(value_dictionary)
#print(len(value_dictionary))

predicted_list = []
for constant_set_key in value_dictionary:
    predicted_list.append(fcast.triple_exponential_smoothing(sample_data,seasons,value_dictionary[constant_set_key][0],
                                                             value_dictionary[constant_set_key][0],
                                                             value_dictionary[constant_set_key][0],prediction_count))

fitting_list_tuple = []
for fitting_set in predicted_list:
    fitting_list_tuple.append(fitting_set[0:len(predicted_list[0]) - 1])

#every element of the fitting list tuple contains a set of predicted values for each constant combination
#get the sse for each set, get the minimum SSE, get the index of that minimum SSE so that we can reference it from
# constant library
sse_list = []
for tuple in fitting_list_tuple:
    sse_list.append(fcast.sse(tuple))

min_sse = min(sse_list)
min_sse_index = sse_list.index(min_sse)
alpha_beta_gamma_list = value_dictionary[min_sse_index]
prediction_list = fcast.triple_exponential_smoothing(sample_data,
                                                     seasons,
                                                     alpha_beta_gamma_list[0],
                                                     alpha_beta_gamma_list[1],
                                                     alpha_beta_gamma_list[2],
                                                     prediction_count)
prediction_list = prediction_list[-prediction_count:]
percent_error = (1- (prediction_list[0]/actual_value)) * 100
print("Minimum SSE: \t %s" % min_sse)
print("Minimum SSE index:\t %s" % min_sse_index)
print("Constants:\t %s" % alpha_beta_gamma_list)
print("Prediction List:\t %s" % prediction_list)
print("---")
print("Actual value for next period: %s" % actual_value)
print("Difference: (+-)%s" % abs(prediction_list[0] - actual_value))
print("Percent Error: %s" % str(percent_error))
