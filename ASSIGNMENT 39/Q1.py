'''

1. Import DecisionTreeClassifier from sklearn.

Create a model object and train it using fit().

'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-" * 50

    print(Border)
    print("Decision Tree Classifier")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Independent variables
    X = df[["StudyHours",
            "Attendance",
            "PreviousScore",
            "AssignmentsCompleted",
            "SleepHours"]]

    # Dependent variable
    Y = df["FinalResult"]

    # Create Decision Tree model
    Model = DecisionTreeClassifier(random_state=42)

    # Train the model
    Model.fit(X, Y)

    print("Decision Tree model trained successfully.")

    print(Border)

if __name__ == "__main__":
    main()