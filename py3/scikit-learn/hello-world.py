# 来源于 http://www.cnblogs.com/taceywong/p/4568806.html
from sklearn import datasets
# 加载鸢尾花数据集
iris = datasets.load_iris()
# 加载数字图像数据集
digits = datasets.load_digits()
# print(digits.data)
# print(digits.target)
print(digits.images[0])
