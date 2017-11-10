import numpy as np

# 注意下面的两种写法意义是不同的
# 这个是1x5,看来如果是一个参数默认都是扩充列
print(np.zeros(5))
# 这个是5x1
print(np.zeros((5, 1)))

print(np.zeros((5,), dtype=np.int))
print(np.zeros((2, 1)))
print(np.zeros((1, 2)))
print(np.zeros((2, 2)))
print(np.zeros(5))
# 自定义类型
print(np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]))
