'''
4. Create a new DataFrame with details of 5 new students.

Use the trained model to predict their results.

Display predictions clearly.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-" * 65

    print(Border)
    print("Prediction for 5 New Students")
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

    ######################################################
    # New Students Data
    ######################################################

    Students = pd.DataFrame({

        "StudyHours":[6, 2, 8, 5, 3],
        "Attendance":[85, 60, 95, 75, 68],
        "PreviousScore":[66, 45, 90, 70, 55],
        "AssignmentsCompleted":[7, 3, 10, 6, 4],
        "SleepHours":[7, 6, 8, 7, 5]

    })

    ######################################################
    # Predict Results
    ######################################################

    Predictions = Model.predict(Students)

    Students["PredictedResult"] = Predictions

    # Convert 0 and 1 into Fail and Pass
    Students["PredictedResult"] = Students["PredictedResult"].replace({
        0: "Fail",
        1: "Pass"
    })

    ######################################################
    # Display Results
    ######################################################

    print("\nPrediction of New Students")
    print(Border)

    print(Students)

    print(Border)

if __name__ == "__main__":
    main()