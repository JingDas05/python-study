# Import libraries
import pandas as pd
import sys

# Our small data set
d = {'one': [1, 1], 'two': [2, 2]}
i = ['a', 'b']
# Create dataframe
df = pd.DataFrame(data=d, index=i)
# print(df)
# print(df.index)

# Bring the columns and place them in the index
print(df.stack())
print(df.stack().index)
print(df.unstack())
print(df.unstack().index)

print(df.T)
print(df.T.index)



