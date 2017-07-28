from pandas import Series, DataFrame

a = Series([1, -9, 7])
print(a)
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame相当于表格
frame = DataFrame(data)
print(frame)
