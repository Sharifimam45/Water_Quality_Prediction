import pandas as pd
import numpy as np 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv('water_quality.csv', sep=';')

# 2. Parse the date column
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')

# 3. Sort the data properly
df = df.sort_values(['id', 'date']).reset_index(drop=True)

# 4. Handle missing values (forward fill method)
df.fillna(method='ffill', inplace=True)

# 5. Add date-based features (seasonality)
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# 6. Create lag features for previous values
lag_days = [1, 2, 3]  # you can increase this
feature_cols = ['NH4', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

for lag in lag_days:
    for col in feature_cols:
        df[f'{col}_lag{lag}'] = df.groupby('id')[col].shift(lag)

# 7. Drop rows with NaN after lagging
df.dropna(inplace=True)

# 8. Prepare features and target
X = df[[f'{col}_lag{lag}' for lag in lag_days for col in feature_cols] + ['id', 'month', 'year']]
y = df['BSK5']

# 9. Train-test split (time-based split to avoid leakage)
train_size = int(len(df) * 0.8)
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# 10. Build and train the model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 11. Predictions
y_pred = model.predict(X_test)

# 12. Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.3f}")
print(f"R2 Score: {r2:.3f}")

# 13. Plot actual vs predicted
plt.figure(figsize=(12, 6))
plt.plot(y_test.values, label='Actual BSK5', color='blue')
plt.plot(y_pred, label='Predicted BSK5', color='red')
plt.xlabel('Test Samples')
plt.ylabel('BSK5')
plt.title('Water Quality Forecasting (BSK5)')
plt.legend()
plt.grid()
plt.show()
