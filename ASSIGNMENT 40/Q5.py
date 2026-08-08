'''
5. Without using accuracy_score, manually calculate accuracy.

Verify whether it matches sklearn accuracy.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Manual Accuracy Calculation")
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

    # Create and train model
    Model = DecisionTreeClassifier(random_state=42)

    Model.fit(X_train, Y_train)

    # Predict
    Y_pred = Model.predict(X_test)

    ######################################################
    # Manual Accuracy Calculation
    ######################################################

    Correct = 0
    Total = len(Y_test)

    for Actual, Predicted in zip(Y_test.values, Y_pred):

        if Actual == Predicted:
            Correct = Correct + 1

    ManualAccuracy = (Correct / Total) * 100

    ######################################################
    # Accuracy using sklearn
    ######################################################

    SklearnAccuracy = accuracy_score(Y_test, Y_pred) * 100

    ######################################################
    # Display Results
    ######################################################

    print("\nCorrect Predictions :", Correct)
    print("Total Predictions   :", Total)

    print("\nManual Accuracy     : {:.2f}%".format(ManualAccuracy))
    print("Sklearn Accuracy    : {:.2f}%".format(SklearnAccuracy))

    if round(ManualAccuracy, 2) == round(SklearnAccuracy, 2):
        print("\nResult : Both accuracies match.")
    else:
        print("\nResult : The accuracies do not match.")

    print(Border)

if __name__ == "__main__":
    main()