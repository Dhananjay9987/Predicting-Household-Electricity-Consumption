#Step 1 : Import libraries & load dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("electricity_data.csv")
print(df.head())

# Step 2 : Select features and target
df['prev_hour'] = df['consumption'].shift(1)
df = df.dropna()
X = df[['hour', 'prev_hour']]
y = df['consumption']

#Step 3 : Split into train & test
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, shuffle=False)

#Step 4 : Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Step 5 : Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error:", mae)
print("R² Score:", r2)

#Step 6 : Visualise predictions
plt.plot(y_test.values, label="Actual")
plt.plot(y_pred, label="Predicted")
plt.legend()
plt.title("Electricity Consumption: Actual vs Predicted")
plt.show()





