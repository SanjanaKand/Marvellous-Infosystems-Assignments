'''
10. Train model with:
max_depth = None

Calculate:

Training accuracy
Testing accuracy

If training accuracy is 100% but testing accuracy is lower,
explain why this happens.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Decision Tree with max_depth = None")
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

    ######################################################
    # Create and Train Model
    ######################################################

    Model = DecisionTreeClassifier(
        max_depth=None,
        random_state=42
    )

    Model.fit(X_train, Y_train)

    ######################################################
    # Predictions
    ######################################################

    Train_Pred = Model.predict(X_train)
    Test_Pred = Model.predict(X_test)

    ######################################################
    # Accuracy Calculation
    ######################################################

    TrainAccuracy = accuracy_score(Y_train, Train_Pred)
    TestAccuracy = accuracy_score(Y_test, Test_Pred)

    print("\nTraining Accuracy : {:.2f}%".format(TrainAccuracy * 100))
    print("Testing Accuracy  : {:.2f}%".format(TestAccuracy * 100))

    ######################################################
    # Observation
    ######################################################

    print("\nObservation:")

    if TrainAccuracy == 1.0 and TestAccuracy < TrainAccuracy:
        print("1. Training accuracy is 100%.")
        print("2. Testing accuracy is lower than training accuracy.")
        print("3. The model has overfitted the training data.")
        print("4. It memorized the training samples instead of learning general patterns.")
        print("5. Therefore, its performance decreases on unseen test data.")
    else:
        print("1. Training and testing accuracies are close.")
        print("2. The model generalizes well and does not show significant overfitting.")

    print(Border)

if __name__ == "__main__":
    main()