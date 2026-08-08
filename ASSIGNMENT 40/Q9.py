'''
9. Create a new column:
PerformanceIndex = (StudyHours * 2) + Attendance

Train the model including this new feature.

Does accuracy improve?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Effect of Adding PerformanceIndex Feature")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    ######################################################
    # Create New Feature
    ######################################################

    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

    ######################################################
    # Model without PerformanceIndex
    ######################################################

    X = df[["StudyHours",
            "Attendance",
            "PreviousScore",
            "AssignmentsCompleted",
            "SleepHours"]]

    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42
    )

    Model = DecisionTreeClassifier(random_state=42)

    Model.fit(X_train, Y_train)

    Y_pred = Model.predict(X_test)

    Accuracy1 = accuracy_score(Y_test, Y_pred)

    ######################################################
    # Model with PerformanceIndex
    ######################################################

    X_New = df[["StudyHours",
                "Attendance",
                "PreviousScore",
                "AssignmentsCompleted",
                "SleepHours",
                "PerformanceIndex"]]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_New,
        Y,
        test_size=0.20,
        random_state=42
    )

    Model = DecisionTreeClassifier(random_state=42)

    Model.fit(X_train, Y_train)

    Y_pred = Model.predict(X_test)

    Accuracy2 = accuracy_score(Y_test, Y_pred)

    ######################################################
    # Display Results
    ######################################################

    print("\nAccuracy without PerformanceIndex : {:.2f}%".format(Accuracy1 * 100))
    print("Accuracy with PerformanceIndex    : {:.2f}%".format(Accuracy2 * 100))

    print("\nObservation:")

    if Accuracy2 > Accuracy1:
        print("1. The accuracy improved after adding PerformanceIndex.")
        print("2. The new feature provides useful information to the model.")
    elif Accuracy2 < Accuracy1:
        print("1. The accuracy decreased after adding PerformanceIndex.")
        print("2. The new feature did not help the model.")
    else:
        print("1. The accuracy remained the same.")
        print("2. PerformanceIndex did not significantly affect the model.")

    print(Border)

if __name__ == "__main__":
    main()