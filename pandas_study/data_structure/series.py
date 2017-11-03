import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print(s.index)

# d = {'a': 0., 'b': 1., 'c': 2.}
# print(pd.Series(d))
# print(pd.Series(d, index=['b', 'c', 'd', 'a']))
# print(pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))

# print(s[0])
# print(s[:3])
# print(s[s > s.median()])
# print([[4, 3, 1]])
# 对矩阵中的每个数取指数函数
# print(np.exp(s))

# print(s['a'])
# s['e'] = 12
# print(s)
# print('e' in s)
# print('f' in s)
# print(s.get('f'))
# print(s.get('f', np.nan))

# print(s + s)
# print(s * 2)
# print(np.exp(s))
# -1 是指最后一个元素不要
# print(s[1:] + s[:-1])

s_name = pd.Series(np.random.randn(5), name='something')
print(s_name)
print(s_name.name)
s_name.rename('different')
print(s_name.name)

