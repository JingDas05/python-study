# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
print(df)
# Operation	                           Syntax	        Result
# Select column	                      df[col]	        Series
# Select row by label	             df.loc[label]    	Series
# Select row by integer location	  df.iloc[loc]	    Series
# Slice rows	                      df[5:10]	        DataFrame
# Select rows by boolean vector	      df[bool_vec]	    DataFrame
print(df.loc['b'])
print(df.iloc[1])


# print(pd.DataFrame(d)['one']['a'])
# print(pd.DataFrame(d, index=['d', 'b', 'a']))
# print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))
# print(pd.DataFrame(d).index)
# print(pd.DataFrame(d).columns)

# d2 = {'one': [1., 2., 3., 4.],
#       'two': [4., 3., 2., 1.]}
# print(pd.DataFrame(d2))
# print(pd.DataFrame(d2, index=['a', 'b', 'c', 'd']))

# d3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# print(pd.DataFrame(d3))
# print(pd.DataFrame(d3, index=['first', 'second']))
# print(pd.DataFrame(d3, columns=['a', 'b']))

# 这个结构很重要
# print(pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
#                     ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
#                     ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
#                     ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
#                     ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
#       )

# orient='index 属性
# print(pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])]))

# d4 = [('A', [1, 2, 3]), ('B', [4, 5, 6])]
# df_4 = pd.DataFrame.from_items(d4, orient='index', columns=['one', 'two', 'three'])
# print(df_4)
# print(df_4['one'])
# df_4['three'] = df_4['one'] * df_4['two']
# df_4['flag'] = df_4['one'] > 2
# print(df_4)
# del df_4['two']
# three = df_4.pop('three')
# print(df_4)
# df_4['foo'] = 'bar'
# df_4['one_trunc'] = df_4['one'][:2]
# # 在第一列的后面插入一列，名字是bar,数据时 one的行
# df_4.insert(1, 'bar', df_4['one'])

# Location = '../data/iris.data'
# iris = pd.read_csv(Location)
# print(iris.head())
# print(iris.assign(sepal_ratio=iris['SepalWidth'] / iris['SepalLength']).head())
# print(iris.assign(sepal_ratio=lambda x: (x['SepalWidth'] / x['SepalLength'])).head())
#
# # assign添加数据
# (iris.query('SepalLength > 5')
#  .assign(SepalRatio=lambda x: x.SepalWidth / x.SepalLength,
#          PetalRatio=lambda x: x.PetalWidth / x.PetalLength)
#  .plot(kind='scatter', x='SepalRatio', y='PetalRatio'))
# plt.show()