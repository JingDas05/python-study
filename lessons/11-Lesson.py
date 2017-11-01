import pandas as pd
import matplotlib
import os
import sys

d = {'Channel': [1], 'Number': [255]}
df = pd.DataFrame(d)
print(df)

df.to_excel('../data/test1.xlsx', sheet_name='test1', index=False)
df.to_excel('../data/test2.xlsx', sheet_name='test2', index=False)
df.to_excel('../data/test3.xlsx', sheet_name='test3', index=False)

FileNames = []
# Your path will be different, please modify the path below.
os.chdir(r"../data")

# Find any file that ends with ".xlsx"
for files in os.listdir("."):
    if files.startswith("test"):
        FileNames.append(files)
print(FileNames)


def get_file(file_name):
    # Path to excel file
    location = r'../data/' + file_name
    # Parse the excel file, 0 = first sheet
    inner_df = pd.read_excel(location, 0)
    # Tag record to file name
    inner_df['File'] = file_name
    # Make the "File" column the index of the df
    return inner_df.set_index(['File'])

df_list = [get_file(file_name) for file_name in FileNames]
print(df_list)




