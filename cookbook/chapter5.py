import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 获取天气数据,加拿大天气网站
# url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?" \
#                "format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
# 年月赋值
# url = url_template.format(month=3, year=2012)

url = '../data/eng-hourly-09012017-09302017.csv'
# 数据的前16行是元数据,Date/Time列是索引列 Quebec天气
# 注意这个地方的编码格式务必为utf-8-sig，这个和需要读取的文件的编码是一致的，如果不一致会出现 keyError错误
weather_mar201709 = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True, encoding='utf-8-sig')
# print(weather_mar201709)

# 取'Temp (°C)'列并且展示
# weather_mar201709['Temp (°C)'].plot(figsize=(15, 6))
# plt.show()

# drop the column if any value is null
weather_mar201709 = weather_mar201709.dropna(axis=1, how='any')
print(weather_mar201709[0:5])

# weather_mar201709 = weather_mar201709.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
# print(weather_mar201709[:5])

# Plotting the temperature by hour of day
# temperatures = weather_mar201709[['Temp (°C)']]
# temperatures['Hour'] = weather_mar201709.index.hour
# temperatures.groupby('Hour').aggregate(np.median).plot()
# plt.show()

# weather_mar201709.to_csv('../data/weather_2012.csv')



