import numpy as np
import pandas as pd

import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([3, 4, 2, 4, 5])

# 1. Calculate Means
mean_x = np.mean(X)
mean_y = np.mean(Y)

# 2. Calculate Slope (m) and Intercept (c)
m = np.sum((X - mean_x) * (Y - mean_y)) / np.sum((X - mean_x) ** 2)
c = mean_y - (m * mean_x)

# Print Calculated Metrics
print(f"Mean of X = {mean_x:g}")
print(f"Mean of Y = {mean_y:g}")
print(f"\nSlope (m) = {m:.1f}")
print(f"Intercept (c) = {c:.1f}")

# Print Regression Equation
print(f"\nRegression Equation:\nY = {m:.1f}X + {c:.1f}")

# Predict Y for X = 6
x_new = 6
y_pred = (m * x_new) + c
print(f"\nPredicted Y for X = {x_new} : {y_pred:.1f}")