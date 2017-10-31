# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

# Our small data set
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create dataframe
df = pd.DataFrame(d)
print(df)
df.columns = ['Rev']
print(df)
df['NewCol'] = 5
print(df)
# Lets modify our new column
df['NewCol'] += 1
print(df)
del df['NewCol']
print(df)
df['test'] = 3
df['col'] = df['Rev']
print(df)
# If we wanted, we could change the name of the index
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = i
print(df)

print(df.loc['a'])
print(df.loc['a':'d'])

# Note: .iloc is strictly integer position based. It is available from [version 0.11.0]
print(df.iloc[0:3])

# 取df数据集里面 'Rev'列 索引0-3的数据
print(df.loc[df.index[0:3], 'Rev'])
# 取df数据集里面 'col'列 索引5行以后的数据
print(df.loc[df.index[5:], 'col'])
# 取df数据集里面 'col' 'test'列 索引开始导3行以后的数据
print(df.loc[df.index[:3], ['col', 'test']])

# Select top N number of records (default = 5)
print(df.head())
# Select bottom N number of records (default = 5)
print(df.tail())





