import pandas as pd
import matplotlib.pyplot as plt

complaints = pd.read_csv('../data/311-service-requests.csv')
# print(complaints)
# print(complaints[:5])

# print(complaints['Complaint Type'][:5])
# print(complaints[:5]['Complaint Type'])

# print(complaints[['Complaint Type', 'Borough']])

print(complaints['Complaint Type'].value_counts())

complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10].plot(kind='bar')
plt.show()

# print(complaints['Complaint Type'])


