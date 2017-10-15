actual = [18561.0, 14229.0, 15881.0, 18939.0, 17107.0, 13042.0, 6652.0, 5654.0, 9771.0, 15759.0, 20965.0, 27088.0,
          21089.0, 17311.0, 19192.0, 19429.0, 21000.0, 13573.0, 16678.0, 17343.0, 14320.0, 15514.0, 19143.0, 31602.0,
          23904.0, 21119.0, 19746.0, 22644.0, 19025.0, 17196.0, 17582.0, 16439.0, 16301.0, 19200.0, 20529.0, 29143.0]

total = 0
for x in range(0, 12):
    total = total + actual[x]
firstYearAverage = total / 12
seasonalSeed = actual[11] - firstYearAverage
baseLevelSeed = actual[11] - seasonalSeed
trendSeed = 0.0
alpha = 0.66
beta = 0.10
gamma = 0.25
baseLevelFactor = 0.0
trendFactor = 0.0
seasonalFactor = []
y = 0
z = 0

for x in range(12, 35):
    if (y < 12):
        baseLevelFactor = (alpha * (actual[x] - (actual[y] - firstYearAverage))) + (1 - alpha) * (
            baseLevelSeed + trendSeed)
        trendFactor = (beta * (baseLevelFactor - baseLevelSeed)) + ((1 - beta) * trendSeed)
        seasonalFactor1 = (gamma * (actual[x] - baseLevelFactor)) + ((1 - gamma) * (actual[y] - firstYearAverage))
        seasonalFactor.extend([seasonalFactor1])
        baseLevelSeed = baseLevelFactor
        trendSeed = trendFactor
        y += 1
    else:
        baseLevelFactor = (alpha * (actual[x] - seasonalFactor[z])) + (1 - alpha) * (
            baseLevelSeed + trendSeed)
        trendFactor = (beta * (baseLevelFactor - baseLevelSeed)) + ((1 - beta) * trendSeed)
        seasonalFactor1 = (gamma * (actual[x] - baseLevelFactor)) + ((1 - gamma) * (actual[y] - firstYearAverage))
        seasonalFactor.extend([seasonalFactor1])
        baseLevelSeed = baseLevelFactor
        trendSeed = trendFactor
        y+=1
        z+=1
    print("period #", x+1, "\nBase Level Factor: ", baseLevelFactor, "\nTrend Factor: ", trendFactor, "\nSesonal Factor: ", seasonalFactor1,"\n")
forecast = baseLevelFactor+trendFactor+seasonalFactor[z]
print(forecast)