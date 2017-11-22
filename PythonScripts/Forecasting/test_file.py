import sqlite3
from PythonScripts.forecasting import forecasting as f

fcast = f.Forecast()

a = [2,3,2,4]

n_preds = 1
print(fcast.triple_exponential_smoothing(a,2,0.2,0.3,0.5,n_preds))

print(a[0:n_preds-1])