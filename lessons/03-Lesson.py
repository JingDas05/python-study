# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

# set seed
np.seed(111)


# Function to generate test data
def create_data_set(number=1):
    output = []
    for i in range(number):
        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        # Create random data,
        data = np.randint(low=25, high=1000, size=len(rng))
        # Status pool
        status = [1, 2, 3]
        # Make a random list of statuses,random_status 的 size 为 len(rng)
        random_status = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]
        # State pool
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']
        # Make a random list of states
        random_states = [states[np.randint(low=0, high=len(states))] for j in range(len(rng))]
        output.extend(zip(random_states, random_status, data, rng))
    return output

dataSet = create_data_set(4)
df = pd.DataFrame(data=dataSet, columns=['State', 'Status', 'CustomerCount', 'StatusDate'])
# print(df.info())
# print(df.head())

Location = '../data/Lesson3.xlsx'
# df.to_excel(Location, index=False)

excel_df = pd.read_excel(Location, 0, index_col='StatusDate')
# print(excel_df.dtypes)
# print(excel_df.head())

# print(excel_df['State'].unique())

# Clean State Column, convert to upper case, state apply 会形成一个新的数组，需要重新赋值才可以
excel_df['State'] = excel_df.State.apply(lambda x: x.upper())
# print(excel_df['State'].unique())

# Convert NJ to NY，把所有等于NJ的替换成NY
# 判断 state等于 NJ的条件，mask为过滤条件
# mask = excel_df.State == 'NJ'
# excel_df['State'][mask] = 'NY'

# excel_df['CustomerCount'].plot(figsize=(15, 5))
# plt.show()

# Group by State and StatusDate
Daily = excel_df.reset_index().groupby(['State', 'StatusDate']).sum()
print(Daily.head())





