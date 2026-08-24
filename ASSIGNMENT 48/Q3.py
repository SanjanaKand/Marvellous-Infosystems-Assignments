# Experience vs. Salary Task

import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([1, 2, 3, 4, 5])  # Experience
Y = np.array([20000, 25000, 30000, 35000, 40000])  # Salary

# 1. Train linear regression model (Calculate m and c)
mean_x = np.mean(X)
mean_y = np.mean(Y)

m = np.sum((X - mean_x) * (Y - mean_y)) / np.sum((X - mean_x) ** 2)
c = mean_y - (m * mean_x)

# 2. Predict salary for 6 years of experience
x_target = 6
y_pred_6 = (m * x_target) + c
print(f"Predicted Salary for 6 Years Experience: ₹{int(y_pred_6)}")

# 3. Plot regression line using matplotlib
plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, m * X + c, color='red', label='Regression line')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary (₹)')
plt.title('Salary vs Experience')
plt.legend()
plt.grid(True)
plt.show()