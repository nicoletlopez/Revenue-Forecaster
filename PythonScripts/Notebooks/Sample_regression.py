from numpy import *

x = array([0,1,2,3,4,5])
y = array([0,0.8,0.9,0.1,-0.8,-1])

print(x)
print(y)

from scipy.interpolate import *

p1 = polyfit(x,y,1) #gets the slope and the intercept

print(p1)

from matplotlib.pyplot import *

plot(x,y,'o')

#%matplotlib inline