import pandas as pd
import sys

# Create a dataframe with dates as your index
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10, freq='MS')
df1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
df1['State'] = States
# print(df1)

# Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States
# print(df2)

# Combine dataframes
df = pd.concat([df1, df2])
# print(df)

# new_df = df.copy()
# new_df['x-Mean'] = abs(new_df['Revenue'] - new_df['Revenue'].mean())
# new_df['1.96*std'] = 1.96 * new_df['Revenue'].std()
# new_df['Outlier'] = abs(new_df['Revenue'] - new_df['Revenue'].mean()) > 1.96 * new_df['Revenue'].std()
# print(new_df)

new_df2 = df.copy()
State = new_df2.groupby('State')
print(State.mean())
new_df2['Outlier'] = State.transform(lambda x: abs(x - x.mean()) > 1.96 * x.std())
new_df2['x-Mean'] = State.transform(lambda x: abs(x - x.mean()))
new_df2['1.96*std'] = State.transform(lambda x: 1.96 * x.std())
print(new_df2)
# 后面看文档吧，还有还有很多
