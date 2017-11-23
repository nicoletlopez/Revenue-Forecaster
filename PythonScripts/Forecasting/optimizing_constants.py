from PythonScripts.Forecasting import forecasting as f

fcast = f.Forecast()

"""sample_data = [30,21,29,31,40,48,53,47,37,39,31,29,17,9,20,24,27,35,41,38,
          27,31,27,26,21,13,21,18,33,35,40,36,22,24,21,20,17,14,17,19,
          26,29,40,31,20,24,18,26,17,9,17,21,28,32,46,33,23,28,22,27,
          18,8,17,21,31,34,44,38,31,30,26,32]"""
#from the excel file
sample_data = \
    [18561,14229,15881,18939,17107,13042,6652,5654,9771,15759,20965,27088,21089,17311,19192,19429,21000,13573,16678,17343,14320,15514,19143,31602,
               23904,21119,19746,22644,19025,17196,17582,16439,16301,19200,20529
    ]
actual_value = 29143 #for period number 36

periods_predicted = 1

#determine all the possible combinations of the constants (100^3 values)
constant_values = []
#populate the list
for x in range(1,101,5):
    constant_values.append(x/100)

#create a value dictionary ( key:[alpha,beta,gamma] )
counter = 0
value_dictionary = {}
for alpha in constant_values:
    for beta in constant_values:
        for gamma in constant_values:
            value_dictionary[counter] = [alpha,beta,gamma]
            #print("%s %s %s" % (value_dictionary[counter][0],value_dictionary[counter][1],value_dictionary[counter][2]))
            counter +=1

# number of period predicted (12 means that we predict the next 12 periods)


#use all possible values as arguments in the holt-winters method
prediction_list = []
for value_set in value_dictionary:
    #print(value_dictionary[value_set][0],value_dictionary[value_set][1],value_dictionary[value_set][2])
    prediction_list.append(fcast.triple_exponential_smoothing(sample_data,12,value_dictionary[value_set][0],value_dictionary[value_set][2],value_dictionary[value_set][2],periods_predicted))

sse_list = []
for single_prediction_item in prediction_list:
    #delete the last n values cause they are the ones predicted
    del single_prediction_item[-periods_predicted:]
    sse_list.append(fcast.sse(single_prediction_item))

#at this point sse_list now contains all the SSE values for each prediction set
#now get the lowest sse
lowest_sse_value = min(sse_list)
#get the lowest sse's index
lowest_sse_value_index = sse_list.index(lowest_sse_value)
#retrieve the alpha beta gamma values used for this minimum SSE from the value_dictionary
alpha_beta_gamma_set = value_dictionary[lowest_sse_value_index]
print("Lowest SSE value: %s \n "
      "Index: %s \n"
      #"Prediction: %s"#
      "Constants used: \n"
      "\t Alpha: %s \n"
      "\t Beta: %s \n"
      "\t Gamma: %s" % (lowest_sse_value,lowest_sse_value_index,alpha_beta_gamma_set[0],alpha_beta_gamma_set[1],alpha_beta_gamma_set[2]))
print("Periods Predicted: ")
for predicted_period in prediction_list[lowest_sse_value_index][-periods_predicted:]:
    print(predicted_period)
print("Actual Value: %s" % actual_value)

#UNCOMMENT ONLY IF N_PRED == 1
try:
    percentage_error = (1 - (prediction_list[lowest_sse_value_index][-periods_predicted:][0])/actual_value) * 100
    print("Percentage Error: %s " %percentage_error)
except Exception:
    print("SORRY, this feature is still under development")
    print("To view the percentage error, please set period_predicted variable to 1")





