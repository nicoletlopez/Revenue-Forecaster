#you're gong to need to have anaconda installed for you to run this script
import statsmodels.api as sm
from sklearn import datasets
import numpy as np
import pandas as pd
from pandas import tseries

data = datasets.load_boston()
#print (data.DESCR)

# define the data/predictors as the pre-set feature names
df = pd.DataFrame(data.data,columns = data.feature_names)

# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target,columns = ['MEDV'])

"""
#Without a constant
X = df["RM"]
y = target["MEDV"]
#Note the difference in argument order
model = sm.OLS(y,X).fit()
predictions = model.predict(X) #make the predictions by the models
#print out the statistics
model.summary()
"""

#With a constant
X = df["RM"] #X usually means our input variables (independent)
y = target["MEDV"] #y usually means our output/dependent variable
X = sm.add_constant(X) #add an intercept (beta_0) to the model
#note the difference in argument order
model = sm.OLS(y,X).fit() #sm.OLS(output,input)
predictions = model.predict(X)
model.summary()