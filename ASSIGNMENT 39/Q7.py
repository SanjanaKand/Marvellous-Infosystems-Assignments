'''
7. Use the trained model to predict result for a student with:
StudyHours = 6
Attendance = 85
PreviousScore = 66
AssignmentsCompleted = 7
SleepHours = 7

Will the student Pass or Fail?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-" * 60

    print(Border)
    print("Prediction for a New Student")
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
        test_size=0.2,
        random_state=42
    )

    # Create model
    Model = DecisionTreeClassifier(random_state=42)

    # Train model
    Model.fit(X_train, Y_train)

    # New student data
    Student = [[6, 85, 66, 7, 7]]

    # Predict result
    Result = Model.predict(Student)

    print("\nStudent Details")
    print("StudyHours            :", 6)
    print("Attendance            :", 85)
    print("PreviousScore         :", 66)
    print("AssignmentsCompleted  :", 7)
    print("SleepHours            :", 7)

    print("\nPrediction")

    if Result[0] == 1:
        print("The student will Pass.")
    else:
        print("The student will Fail.")

    print(Border)

if __name__ == "__main__":
    main()