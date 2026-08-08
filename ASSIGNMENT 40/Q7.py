'''
7. Train model using:
random_state = 0
random_state = 10
random_state = 42

Compare testing accuracy.

Does the result change?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Comparison of Different Random States")
    print(Border)

    # Load Dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Independent variables
    X = df[["StudyHours",
            "Attendance",
            "PreviousScore",
            "AssignmentsCompleted",
            "SleepHours"]]

    # Dependent variable
    Y = df["FinalResult"]

    # Random states to test
    RandomStates = [0, 10, 42]

    print("\nTesting Accuracy")
    print(Border)

    for State in RandomStates:

        # Split dataset
        X_train, X_test, Y_train, Y_test = train_test_split(
            X,
            Y,
            test_size=0.20,
            random_state=State
        )

        # Create model
        Model = DecisionTreeClassifier(random_state=State)

        # Train model
        Model.fit(X_train, Y_train)

        # Predict
        Y_pred = Model.predict(X_test)

        # Accuracy
        Accuracy = accuracy_score(Y_test, Y_pred)

        print("random_state = {:>2} --> {:.2f}%".format(State, Accuracy * 100))

    print(Border)

    print("\nObservation:")
    print("1. Different random_state values create different train-test splits.")
    print("2. As a result, the testing accuracy may change slightly.")
    print("3. The Decision Tree model may also produce a slightly different tree for each random_state.")
    print("4. If the dataset is well balanced, the accuracy usually remains similar.")
    print("5. Therefore, changing random_state may affect the result, but the difference is generally small.")

if __name__ == "__main__":
    main()