'''
6. Identify students where:
y_test != y_pred
Display those rows.
How many students were misclassified?
What common pattern do you observe?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-" * 65

    print(Border)
    print("Misclassified Students")
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
    # Identify Misclassified Students
    ######################################################

    # Convert test data to DataFrame
    TestData = X_test.copy()

    TestData["ActualResult"] = Y_test.values
    TestData["PredictedResult"] = Y_pred

    # Select rows where prediction is incorrect
    Misclassified = TestData[TestData["ActualResult"] != TestData["PredictedResult"]]

    ######################################################
    # Display Results
    ######################################################

    print("\nMisclassified Students")
    print(Border)

    if len(Misclassified) > 0:
        print(Misclassified)
    else:
        print("No misclassified students found.")

    print("\nNumber of Misclassified Students :", len(Misclassified))

    print("\nObservation:")
    print("1. These students were predicted incorrectly by the Decision Tree model.")
    print("2. They usually have feature values close to the decision boundary.")
    print("3. Their StudyHours, Attendance, or PreviousScore may be similar to both Pass and Fail students.")
    print("4. Such cases are difficult for the model to classify correctly.")

    print(Border)

if __name__ == "__main__":
    main()