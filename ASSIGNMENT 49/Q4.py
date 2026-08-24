# 4. Euclidean Distance Before and After Feature Scaling

import numpy as np
from sklearn.preprocessing import StandardScaler

# Points: P1 = [25, 20000], P2 = [30, 40000]
data = np.array([[25, 20000], [30, 40000], [35, 80000]])

# 1. Distance before scaling
dist_before = np.linalg.norm(data[0] - data[1])

# 2. Distance after scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
dist_after = np.linalg.norm(scaled_data[0] - scaled_data[1])

print(f"Euclidean Distance Before Scaling: {dist_before:.2f}")
print(f"Euclidean Distance After Scaling:  {dist_after:.4f}")