from PythonScripts.forecasting import forecasting as f
import sqlite3
import pandas as pd
import scipy.optimize._minimize as sp
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 1000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

conn = sqlite3.connect('sample_db.sqlite3')
cur = conn.cursor()
"""
#store tuples in temporary directory
temp = cur.execute("select rev from actual where seg_id = 1 limit 12")

revenue_list = []
for item in temp:
    #var item contains tuples (the entire data structure is a 2d array)
    revenue_list.append(item[0])
"""
sample_data = [30,21,29,31,40,48,53,47,37,39,31,29,17,9,20,24,27,35,41,38,
          27,31,27,26,21,13,21,18,33,35,40,36,22,24,21,20,17,14,17,19,
          26,29,40,31,20,24,18,26,17,9,17,21,28,32,46,33,23,28,22,27,
          18,8,17,21,31,34,44,38,31,30,26,32]

revenue_list = [6806425.71, 3592011.4028, 2682894.0, 6404799.0,
                5367100.0, 3335506.0, 2746567.1, 4396821.0, 2883258.0, 3318648.0, 6252736.0, 9023272.0]

#instantiate new forecast object
fcast = f.Forecast()

#get mean of sample data
mean = sum(sample_data)/len(sample_data)

result = fcast.triple_exponential_smoothing(sample_data,12,0.66,0.10,0.25,12)

#add placeholder data
for x in range (len(result) - len(sample_data)):
    sample_data.append(0)

deviation = []
deviation2 = []
for predicted_value in result:
    deviation.append(predicted_value - mean)
for single_sse in deviation:
    deviation2.append(single_sse ** 2)

print("Mean %s:" % mean)
result_frame = pd.DataFrame({"Values":sample_data,"Predicted":result,"Deviation(predicted-mean)":deviation,"Deviation^2":deviation2})
"""fig, ax1 = plt.subplots()

x = result_frame["Values"]
y1 = result_frame["Predicted"]

ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-')"""

print(result_frame)

#####################################
sample_data = [30,21,29,31,40,48,53,47,37,39,31,29,17,9,20,24,27,35,41,38,
          27,31,27,26,21,13,21,18,33,35,40,36,22,24,21,20,17,14,17,19,
          26,29,40,31,20,24,18,26,17,9,17,21,28,32,46,33,23,28,22,27,
          18,8,17,21,31,34,44,38,31,30,26,32]
def error_fn(input_params, y, m, h=1):
    alpha, beta, gamma = input_params
    # Call your impl of holt_winters with alpha, beta, gamma
    y_hat = fcast.triple_exponential_smoothing(sample_data,12,alpha=alpha,beta=beta,gamma=gamma,n_preds=12)

    # Compute different error metrics.
    sse = 0
    for i in range(h, len(y)):
        sse += (y_hat[i] - y[i]) ** 2
    return sse
### Main
alpha0 = 0.8
beta0 = 0.1
gamma0 = 0.1

p0 = [alpha0,beta0,gamma0]
bounds = ((0,1),(0,1),(0,1))
#plsq = sp(error_fn(),p0,bounds=bounds,args=(y,m,h))
