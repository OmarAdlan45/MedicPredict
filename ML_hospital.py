import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import  matplotlib.pyplot as plt

data = pd.read_csv("insurance.csv")
data = pd.get_dummies(data, columns= ['sex', 'smoker', 'region'], drop_first=True)
x = data.drop('charges', axis = 1)
y = data['charges']
x_train, x_test , y_train, y_test = train_test_split(x,y, test_size=0.3, random_state= 42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)

print(f"Mean Squared Error (MSE): {mse}")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred_scaled = model.predict(X_test_scaled)

mse_scaled = mean_squared_error(y_test,y_pred_scaled)
r2_scaled = r2_score(y_test,y_pred_scaled)



print(f"Mean Squared Error (MSE) after scaling: {mse_scaled}")
print(f"R-squared (R^2) after scaling: {r2_scaled}")

data['children'].value_counts().plot(kind='pie', title= 'Children # Distribution' ,radius=1.25,  autopct= '%1.1f%%')
plt.title('Children # Distribution', y=1.05)
plt.show()


plt.scatter(y_test, y_pred, alpha = 0.7, color = 'black')
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Charges (Linear Regression)")
plt.show()



