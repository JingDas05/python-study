import pandas as pd
import sys

# Create DataFrame
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
df = pd.DataFrame(d, columns=['Number'])
# print(df)

Location = '../data/Lesson10.xlsx'
Location_json = '../data/Lesson10.json'
# df.to_excel(Location, sheet_name='testing', index=False)

# Parse the excel file
# read_df = pd.read_excel(Location, 0)
# print(read_df.head())
# print(read_df.dtypes)

# df.to_json(Location_json)

read_json = pd.read_json(Location_json)
print(read_json)
print(read_json.dtypes)






