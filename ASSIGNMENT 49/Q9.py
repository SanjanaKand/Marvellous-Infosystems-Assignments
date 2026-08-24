# 9. Python Program for Scikit-Learn Classification Report

from sklearn.metrics import classification_report

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(actual, predicted, target_names=['Class 0', 'Class 1'])
print(report)