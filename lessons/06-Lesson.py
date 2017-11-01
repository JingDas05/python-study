# Import libraries
import pandas as pd
import sys

# Our small data set
d = {'one': [1, 1, 1, 1, 1],
     'two': [2, 2, 2, 2, 2],
     'letter': ['a', 'a', 'b', 'b', 'c']}

# Create dataframe
df = pd.DataFrame(d)
# print(df)

# Create group object
# one = df.groupby('letter')
# print(one.sum())

letter_one = df.groupby(['letter', 'one']).sum()
print(letter_one)
letter_two = df.groupby(['letter', 'one'], as_index=False).sum()
print(letter_two)

