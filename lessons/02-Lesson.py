import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys  # only needed to determine Python version number
import matplotlib  # only needed to determine Matplotlib version number

# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)
# print('Matplotlib version ' + matplotlib.__version__)

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']

# seed(500) - Create seed
# randint(low=0,high=len(names)) - Generate a random integer between zero and the length of the list "names".
# names[n] - Select the name where its index is equal to n.
# for i in range(n) - Loop until i is equal to n, i.e. 1,2,3,....n.
# random_names = Select a random name from the name list and do this n times.
random.seed(500)
random_names = [names[random.randint(low=0, high=len(names))] for i in range(1000)]
# Print first 10 records
# print(random_names[:10])

# The number of births per name for the year 1880
births = [random.randint(low=0, high=1000) for j in range(1000)]
# print(births[:10])

BabyDataSet = list(zip(random_names, births))
# print(BabyDataSet[:10])

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
# print(df[:10])

Location = '../data/births1880.txt'
# df.to_csv(Location, index=False, header=False)

# df = pd.read_csv(Location)
# print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 999 entries, 0 to 998
# Data columns (total 2 columns):
# Mary    999 non-null object
# 968     999 non-null int64
# dtypes: int64(1), object(1)
# memory usage: 15.7+ KB
# Info says:
#     There are 999 records in the data set
#     There is a column named Mary with 999 values
#     There is a column named 968 with 999 values
#     Out of the two columns, one is numeric, the other is non numeric
# print(df.head())

df = pd.read_csv(Location, header=None)
print(df.info())
print(df.tail())

df = pd.read_csv(Location, names=['Names', 'Births'])
print(df.head(5))

# 一
# df['Names'].unique()
# for x in df['Names'].unique():
#     print(x)
# 二
# print(df['Names'].describe())
# 三
# name = df.groupby('Names')
# df = name.sum()

# Method 1:
# Sorted = df.sort_values(['Births'], ascending=False)
# Sorted.head(1)

# Method 2:
# df['Births'].max()

# Create graph
df['Births'].plot.bar()
print("The most popular name")
df.sort_values(by='Births', ascending=False)
plt.show()

