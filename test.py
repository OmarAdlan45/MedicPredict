import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

data = pd.read_excel('/Users/omarabdelaziz/Desktop/HAP 436/Module 10 Assignment.xlsx', index_col=0)
data1 = data.T
data1.index = data1.index.set_names('TimePeriod')
data1 = data1.reset_index()

data1 = data1.melt(id_vars='TimePeriod', var_name='Category', value_name='Observation_Value')  # different name
print(data1.head())
print(data1.describe())

data1['lower_fourth'] = 84.5
data1['upper_fourth'] = 92.5
data1['fourth_spreads'] = data1['upper_fourth'] - data1['lower_fourth']

print(data1)

data1['UCL'] = data1['upper_fourth'] + 1.5*data1['fourth_spreads']
data1['LCL'] = data1['lower_fourth'] - 1.5*data1['fourth_spreads']
print(data1)

ax = plt.gca()
data1.plot(kind='line', x = 'TimePeriod', y = 'Observation_Value', color='blue', marker='o', ax=ax)
data1.plot(kind='line', x = 'TimePeriod', y = 'LCL', color='red', ax=ax)
data1.plot(kind='line', x = 'TimePeriod', y = 'UCL', color='red', ax=ax)
plt.title('Waiting Time Calculation')
plt.ylabel('Waiting Time')
plt.legend(bbox_to_anchor=(1.3,1), loc='upper right', borderaxespad=0)
plt.show()
