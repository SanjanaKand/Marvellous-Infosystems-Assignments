'''
2. Remove the column SleepHours from the dataset.
Train the model again.
Compare new accuracy with previous accuracy.
Does removing this feature affect performance?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Effect of Removing SleepHours Feature")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    ######################################################
    # Model with all features
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
    # Model after removing SleepHours
    ######################################################

    X_New = df[["StudyHours",
                "Attendance",
                "PreviousScore",
                "AssignmentsCompleted"]]

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

    print("\nAccuracy with SleepHours    : {:.2f}%".format(Accuracy1 * 100))
    print("Accuracy without SleepHours : {:.2f}%".format(Accuracy2 * 100))

    print("\nObservation:")

    if Accuracy2 > Accuracy1:
        print("1. Accuracy increased after removing SleepHours.")
        print("2. SleepHours was not an important feature.")
    elif Accuracy2 < Accuracy1:
        print("1. Accuracy decreased after removing SleepHours.")
        print("2. SleepHours contributed to the prediction.")
    else:
        print("1. Accuracy remained the same.")
        print("2. Removing SleepHours did not affect model performance.")

    print(Border)

if __name__ == "__main__":
    main()