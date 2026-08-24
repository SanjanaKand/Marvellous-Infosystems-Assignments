'''
Using the regression model created in the previous question, 
write a Python program to predict marks for 6 study hours and
display the predicted value.
'''

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    data = {
        'StudyHours': [1, 2, 3, 4, 5],
        'Marks': [50, 55, 60, 65, 70]
    }
    df = pd.DataFrame(data)
    
    X = df[['StudyHours']]
    y = df['Marks']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict for 6 study hours
    hours = np.array([[6]])
    predicted_marks = model.predict(hours)
    
    print(f"Predicted Marks for 6 Study Hours : {predicted_marks[0]}")

if __name__ == "__main__":
    main()