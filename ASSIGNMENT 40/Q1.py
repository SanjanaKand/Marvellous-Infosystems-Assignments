'''
1. After training the Decision Tree model, use:
model.feature_importances_
Display importance score of each feature.
Which feature contributes the most in predicting FinalResult?
Which feature contributes the least?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-" * 65

    print(Border)
    print("Feature Importance using Decision Tree")
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

    # Split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42
    )

    # Create model
    Model = DecisionTreeClassifier(random_state=42)

    # Train model
    Model.fit(X_train, Y_train)

    # Feature Importance
    Importance = Model.feature_importances_

    print("\nFeature Importance Scores")
    print(Border)

    for Feature, Score in zip(X.columns, Importance):
        print("{:<25} {:.4f}".format(Feature, Score))

    # Most Important Feature
    MaxIndex = Importance.argmax()

    # Least Important Feature
    MinIndex = Importance.argmin()

    print(Border)
    print("Most Important Feature  :", X.columns[MaxIndex])
    print("Least Important Feature :", X.columns[MinIndex])
    print(Border)

if __name__ == "__main__":
    main()