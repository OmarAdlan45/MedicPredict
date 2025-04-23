'''import pandas as pd

data = pd.read_csv('fetal_health.csv')
print(data.head(6))
print(data['fetal_health'].value_counts())'''

'''import pandas as pd
data = pd.read_csv('data1.csv')
avg_age = data['Age'].mean()
data.loc[data['Name'] == 'Bob', 'Age'] =  avg_age


median_salary = data['Salary'].median()
data.loc[data['Name'] == 'Eve', 'Salary'] = median_salary

data['Salary After Tax'] = data['Salary'] * 0.7

print(data)'''

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data1.csv')
avg_salary = data['Salary'].mean()
median_age = data['Age'].median()
highest = data['Salary'].max()
lowest = data['Salary'].min()
it_dep = data.loc[data['Department'] == 'IT']
over_50k = data.loc[data['Salary'] >= 50000]
data['Salary After Bonus'] = data['Salary'] * 1.1
print(avg_salary, median_age, highest, lowest,it_dep,over_50k, data['Salary After Bonus'])

data['Salary'].plot(kind= 'bar', title='Salary Distribution', ylabel = 'Salary', xlabel = 'Employee Index')
plt.show()
data['Department'].value_counts().plot(kind= 'pie', title='Employees by Department', autopct= '%1.1f%%')
plt.show()