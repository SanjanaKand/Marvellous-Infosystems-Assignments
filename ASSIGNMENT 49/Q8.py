# 8. Python Program for Confusion Matrix Values

import numpy as np

actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

TP = np.sum((actual == 1) & (predicted == 1))
TN = np.sum((actual == 0) & (predicted == 0))
FP = np.sum((actual == 0) & (predicted == 1))
FN = np.sum((actual == 1) & (predicted == 0))

print(f"True Positive (TP)  : {TP}")
print(f"True Negative (TN)  : {TN}")
print(f"False Positive (FP) : {FP}")
print(f"False Negative (FN) : {FN}")