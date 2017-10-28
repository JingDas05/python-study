import pandas as pd
import matplotlib.pyplot as plt

bikes = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# bikes['Berri 1'].plot()
# plt.show()

# 获取数据
berri_bikes = bikes[['Berri 1']]
# print(berri_bikes.index)
# print(berri_bikes.index.day)
# print(berri_bikes.index.weekday)

# 这个是赋值操作，berri_bikes 的 weekday等于berri_bikes.index.weekday
berri_bikes['weekday'] = berri_bikes.index.weekday
# print(berri_bikes[:5])

# 聚合，根据一周的日期聚合出各自的总数
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print(weekday_counts)

# 将索引列的 0 1 2 3 4 5 6 替换成 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)
# 显示柱状图
weekday_counts.plot(kind='bar')
plt.show()


