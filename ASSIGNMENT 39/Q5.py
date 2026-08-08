'''
5. Calculate:
Training accuracy
Testing accuracy

Compare both and comment whether the model is overfitting or underfitting.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 60

    print(Border)
    print("Training Accuracy and Testing Accuracy")
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

    # Create Decision Tree model
    Model = DecisionTreeClassifier(random_state=42)

    # Train model
    Model.fit(X_train, Y_train)

    # Predictions
    Train_Pred = Model.predict(X_train)
    Test_Pred = Model.predict(X_test)

    # Accuracy
    Train_Accuracy = accuracy_score(Y_train, Train_Pred)
    Test_Accuracy = accuracy_score(Y_test, Test_Pred)

    print("\nTraining Accuracy : {:.2f}%".format(Train_Accuracy * 100))
    print("Testing Accuracy  : {:.2f}%".format(Test_Accuracy * 100))

    print("\nObservation:")

    if Train_Accuracy > Test_Accuracy + 0.05:
        print("The training accuracy is significantly higher than the testing accuracy.")
        print("This indicates that the model is overfitting.")
    elif Test_Accuracy > Train_Accuracy:
        print("The testing accuracy is higher than the training accuracy.")
        print("The model may be underfitting or the difference is due to data variation.")
    else:
        print("The training and testing accuracies are very close.")
        print("The model is well-fitted and generalizes well on unseen data.")

    print(Border)

if __name__ == "__main__":
    main()