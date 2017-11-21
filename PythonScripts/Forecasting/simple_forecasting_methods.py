series = [3,10,12,13,12,10,12]

weights = [.1,.2,.3,.4]

def average(series):
    return float(sum(series))/len(series)

def moving_average(series,n):
    return average(series[-n:])

def weighted_average(series,weights):
    result = 0
    weights.reverse()
    for n in range(len(weights)):
        result += series[-n-1] * weights[n]
    return result

def exponential_smoothing(series,alpha):
    result = [series[0]]
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1-alpha) * result[n-1])
    return result

def double_exponential_smoothing(series,alpha,beta):
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
######################################################################
print(series)

print("Average: %s" % average(series))

n = 3
print("Moving Average where n is %s: %s " % (n,moving_average(series,n)))

print("weighted Moving Average is: %s" % weighted_average(series,weights))

alpha = 0.1
print("Exponential smoothing value where alpha is %s: %s" % (alpha,exponential_smoothing(series,alpha)))

alpha = 0.9
beta = 0.9
result = double_exponential_smoothing(series,alpha,beta)
print("Double exponential Smoothing \n"
      "Alpha = %s \n"
      "Beta = %s \n"
      "Result: %s" % (alpha,beta,result))



