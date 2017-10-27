import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

complaints = pd.read_csv('../data/311-service-requests.csv')

# noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]

# print(noise_complaints[:3])
# print(complaints['Complaint Type'] == "Noise - Street/Sidewalk")

# is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
# in_brooklyn = complaints['Borough'] == "BROOKLYN"
# print(complaints[is_noise & in_brooklyn][:5])
# print(complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10])

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()
print(noise_complaint_counts / complaint_counts)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')
plt.show()







