import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(DataPath):
    Border = "-"*60
    
    # Step 1 : Load the dataset
    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Some entries from the dataset are :")
    print(df.head())

    # Step 2 : Remove unwanted columns
    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print("Entries from data :\n")
    print(df.head())

    # Step 3 : Check missing values
    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Total missing values : \n", df.isnull().sum())

    # Step 4 : Statistical Summary
    print(Border)
    print("Step 4 : Statistical Summary")
    print(Border)

    print("Summary of dataset :")
    print(df.describe())

    # Step 5 : Correlation
    print(Border)
    print("Step 5 : Correlation")
    print(Border)

    print(df.corr())

    # Step 6 : Separate Independent and Dependent Variables
    print(Border)
    print("Step 6 : Separate Independent and Dependent variables")
    print(Border)

    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("Independent Variables :")
    print(X.head())
    
    print("Dependent Variables :")
    print(Y.head())

    # Step 7 : Split the dataset into half (50% Train, 50% Test)
    print(Border)
    print("Step 7 : Split the dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    print("Training Data :", X_train.shape)
    print("Testing Data :", X_test.shape)

    # Step 8 : Create and Train the model
    print(Border)
    print("Step 8 : Create and Train the model")
    print(Border)

    model = LinearRegression()
    model = model.fit(X_train, Y_train)

    print("Model trained successfully...")

    # Step 9 : Test the model
    print(Border)
    print("Step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Expected answers (Actual Sales) :")
    print(Y_test.head().values)

    print(Border)

    print("Predicted answers :")
    print(Y_pred[:5])

    # Step 10 : Evaluate the model
    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)

    print("MSE : MEAN SQUARED ERROR :", MSE)
    print("RMSE : ROOT MEAN SQUARED ERROR :", RMSE)
    print("R2 SCORE :", R2)

    # Step 11 : Display Coefficient
    print(Border)
    print("Step 11 : Display Coefficient")
    print(Border)

    print("TV coefficient :", model.coef_[0])
    print("Radio coefficient :", model.coef_[1])
    print("Newspaper coefficient :", model.coef_[2])
    print("Y Intercept :", model.intercept_)

    print(Border)

def main():
    MarvellousRegression("Advertising (1).csv")

if __name__ == "__main__":
    main()