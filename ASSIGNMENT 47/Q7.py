'''
Question 7Write a Python program using LinearRegression to train a regression model using the dataset below.
Your program should:
Train the regression model
Print the coefficient
Print the intercept
'''
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

def main():
    # Dataset
    data = {
        'StudyHours': [1, 2, 3, 4, 5],
        'Marks': [50, 55, 60, 65, 70]
    }
    df = pd.DataFrame(data)
    
    X = df[['StudyHours']]
    y = df['Marks']
    
    # Train model
    model = LinearRegression()
    model.fit(X, y)
    
    print("Coefficient :", model.coef_[0])
    print("Intercept   :", model.intercept_)

if __name__ == "__main__":
    main()