'''
3. Train the model using only:
StudyHours
Attendance

Compare the accuracy with the full-feature model.

Is the model still performing well?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Comparison of Full Feature Model and Two Feature Model")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Dependent variable
    Y = df["FinalResult"]

    ######################################################
    # Model using all features
    ######################################################

    X_Full = df[["StudyHours",
                 "Attendance",
                 "PreviousScore",
                 "AssignmentsCompleted",
                 "SleepHours"]]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_Full,
        Y,
        test_size=0.20,
        random_state=42
    )

    Model = DecisionTreeClassifier(random_state=42)

    Model.fit(X_train, Y_train)

    Y_pred = Model.predict(X_test)

    FullAccuracy = accuracy_score(Y_test, Y_pred)

    ######################################################
    # Model using only StudyHours and Attendance
    ######################################################

    X_New = df[["StudyHours",
                "Attendance"]]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_New,
        Y,
        test_size=0.20,
        random_state=42
    )

    Model = DecisionTreeClassifier(random_state=42)

    Model.fit(X_train, Y_train)

    Y_pred = Model.predict(X_test)

    NewAccuracy = accuracy_score(Y_test, Y_pred)

    ######################################################
    # Display Results
    ######################################################

    print("\nAccuracy using All Features       : {:.2f}%".format(FullAccuracy * 100))
    print("Accuracy using Two Features Only  : {:.2f}%".format(NewAccuracy * 100))

    print("\nObservation:")

    if NewAccuracy >= FullAccuracy:
        print("1. The model performs almost the same using only StudyHours and Attendance.")
        print("2. These two features are highly informative.")
    elif FullAccuracy - NewAccuracy <= 0.05:
        print("1. The accuracy decreased slightly.")
        print("2. The model is still performing well with only two features.")
    else:
        print("1. The accuracy decreased significantly.")
        print("2. The removed features contain important information.")
        print("3. The model does not perform as well using only two features.")

    print(Border)

if __name__ == "__main__":
    main()