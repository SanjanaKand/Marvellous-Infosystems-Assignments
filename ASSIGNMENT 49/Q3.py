# 3. Feature Scaling using StandardScaler

import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[25, 20000], 
                 [30, 40000], 
                 [35, 80000]])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("Scaled Dataset:\n", scaled_data)