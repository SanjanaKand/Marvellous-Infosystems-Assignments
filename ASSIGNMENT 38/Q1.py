'''
1. Write a Python program to load the file student_performance_ml.csv using pandas.
Display:
First 5 records
Last 5 records
Total number of rows and columns
List of column names
Data types of each column
'''
# 0 : Fail
# 1 : Pass

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def main():
    Border = "-"*45
    print(Border)
    print(f"Student Performance ML Dataset")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("File read successfully")

    # First 5 records
    print("First 5 records from the dataset are :")
    first = df.head(5)
    print(first)

    # Last 5 records
    print("Last 5 records from the dataset are :")
    last = df.tail(5)
    print(last)   

    # Total number of rows and columns
    print("Total number of rows and columns are :")
    total_row_column = df.shape
    print(total_row_column)

    # List of column names
    print("List of column names from the dataset are :")
    cols_name = df.columns
    print(cols_name)

    # Data types of each column
    print("Data types of each column :")
    for cols in df.columns:
        print(f"Data type of {cols} is {df[cols].dtype} ")

    
if __name__ == "__main__":
    main()