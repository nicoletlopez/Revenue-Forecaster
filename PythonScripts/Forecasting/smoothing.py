import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', 1000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

conn = sqlite3.connect('sample_db.sqlite3')
c = conn.cursor()

def exp_smoothing(series, alpha):
    return sum([alpha * (1 - alpha) ** i * x for i, x in enumerate(reversed(series))])

revenue_list = []
revenues = c.execute("select rev from actual where seg_id=1 order by date LIMIT 12")
for revenue in revenues:
    revenue_list.append(revenue[0])
print(revenue_list)

month_list =["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept",
             "Oct","Nov","Dec"]

df = pd.DataFrame({'month':month_list,'revenue':revenue_list})
print(df)

predicted = exp_smoothing(df['revenue'],0.8)

actual = 9032984.78

print(predicted)
###################

alpha_values = []
predicted_values = []
percent_error = []

print("Actual Value: %s" %actual)

for x in range(1,101):
    alpha_values.append(x/100)
for revenue in alpha_values:
    predicted_values.append((exp_smoothing(revenue_list, revenue)))
for prediction in predicted_values:
    percent_error.append( 1 - ((prediction/actual)))

demo_frame = pd.DataFrame({'Alpha':alpha_values,'Prediction':predicted_values,'Percent Error':percent_error})
print(demo_frame)




