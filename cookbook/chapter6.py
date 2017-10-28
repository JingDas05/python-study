import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 数据的前16行是元数据,Date/Time列是索引列 Quebec天气
# 注意这个地方的编码格式务必为utf-8-sig，这个和需要读取的文件的编码是一致的，如果不一致会出现 keyError错误
url = '../data/eng-hourly-09012017-09302017.csv'
weather_mar201709 = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True, encoding='utf-8-sig')
# print(weather_mar201709)

weather_description = weather_mar201709['Weather']
is_snowing = weather_description.str.contains('Snow')
# 需要过滤掉 NaN的数据项
print(is_snowing[:5])
# is_snowing.plot()
# plt.show()
