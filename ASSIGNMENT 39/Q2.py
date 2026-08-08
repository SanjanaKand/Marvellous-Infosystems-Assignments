'''
2. Use the trained model to predict results for X_test.

Display predicted values along with actual values.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-" * 60

    print(Border)
    print("Decision Tree Prediction")
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

    # Predict on test data
    Y_pred = Model.predict(X_test)

    print("\nActual Value\tPredicted Value")
    print(Border)

    for Actual, Predicted in zip(Y_test.values, Y_pred):
        print(f"{Actual}\t\t{Predicted}")

    print(Border)

if __name__ == "__main__":
    main()