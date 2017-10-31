from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import os

# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)
# print('Matplotlib version ' + matplotlib.__version__)

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
Location = '../data/births1880.csv'

BabyDataSet = list(zip(names, births))
# print(BabyDataSet)
df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
# print(df)
# df.to_csv(Location, index=False, header=False)

# df = pd.read_csv(Location, header=None)
# print(df)

# 删除csv文件
# os.remove(Location)

# print(df.dtypes)
# print(df.Births.dtypes)

# Sorted = df.sort_values(['Births'], ascending=False)
# print(Sorted.head(1))
# print(df['Births'].max())

df['Births'].plot()
# Create graph

# Maximum value in the data set
MaxValue = df['Births'].max()
# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
# Text to display on graph
Text = str(MaxValue) + " - " + MaxName
# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

# print(df[df['Births'] == df['Births'].max()])
plt.show()








