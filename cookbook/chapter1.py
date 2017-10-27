import pandas as pd
import matplotlib.pyplot as plt
# 另一种写法
# from matplotlib import pyplot as plt
import numpy as np

# 设置显示的画图大小
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# print(fixed_df[:3])
# print(fixed_df['Berri 1'])
# fixed_df['Berri 1'].plot(figsize=(15, 10))
fixed_df.plot(figsize=(15, 10))
# 在pycharm中显示的话需要下面的语句 plt.show()
plt.show()

# print(pd.Series([1, 2, 3]))
# print(pd.Series([1, 2, 3]).values)
# arr = np.array([1, 2, 3])
# print(arr)
# print(arr != 2)
# print(arr[arr != 2])



