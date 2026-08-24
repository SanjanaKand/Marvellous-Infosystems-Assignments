# Model Performance Calculations

import numpy as np

# Original dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([3, 4, 2, 4, 5])

# Line parameters from Question 1 (Y = 0.4X + 2.4)
m, c = 0.4, 2.4

# 1. Predict all Y values using the regression equation
Y_pred = m * X + c
print("Predicted Y values:", Y_pred)

# 2. Intermediate calculations
errors = Y - Y_pred
squared_errors = errors ** 2

# Mean Squared Error (MSE)
mse = np.mean(squared_errors)

# R^2 Score
ss_tot = np.sum((Y - np.mean(Y)) ** 2)  # Total Sum of Squares
ss_res = np.sum(squared_errors)         # Residual Sum of Squares
r2_score = 1 - (ss_res / ss_tot)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2_score:.2f}")