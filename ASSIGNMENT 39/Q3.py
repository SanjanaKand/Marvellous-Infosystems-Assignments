'''
3. Calculate model accuracy using accuracy_score.

Display the result in percentage format.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 60

    print(Border)
    print("Decision Tree Model Accuracy")
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

    # Predict
    Y_pred = Model.predict(X_test)

    # Calculate accuracy
    Accuracy = accuracy_score(Y_test, Y_pred)

    print("\nModel Accuracy : {:.2f}%".format(Accuracy * 100))

    print(Border)

if __name__ == "__main__":
    main()