import pandas as pd
import matplotlib.pyplot as plt

bikes = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# bikes['Berri 1'].plot()
# plt.show()

berri_bikes = bikes[['Berri 1']]
# print(berri_bikes.index)
# print(berri_bikes.index.day)
# print(berri_bikes.index.weekday)

# 这个是赋值操作，berri_bikes 的 weekday等于berri_bikes.index.weekday
berri_bikes['weekday'] = berri_bikes.index.weekday
print(berri_bikes[:5])





