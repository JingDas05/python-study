import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# requests = pd.read_csv('../data/311-service-requests.csv')
# print(requests)
# print(requests['Incident Zip'].unique())

# 过滤na_values中的数值
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('../data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})
# print(requests['Incident Zip'].unique())

# rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
# print(len(requests[rows_with_dashes]))
# print(requests[rows_with_dashes])

long_zip_codes = requests['Incident Zip'].str.len() > 5
print(requests['Incident Zip'][long_zip_codes].unique())

# Incident Zip字段进行剪切0-5,之后重新复制
requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
print(requests[requests['Incident Zip'] == '00000'])






