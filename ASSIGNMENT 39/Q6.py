'''
6. Train three Decision Tree models with:
max_depth = 1
max_depth = 3
max_depth = None

Compare their testing accuracies and write your observations.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-" * 65

    print(Border)
    print("Comparison of Decision Tree Models with Different max_depth")
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

    # Different values of max_depth
    Depths = [1, 3, None]

    print("\nTesting Accuracy")
    print(Border)

    for Depth in Depths:

        # Create model
        Model = DecisionTreeClassifier(
            max_depth=Depth,
            random_state=42
        )

        # Train model
        Model.fit(X_train, Y_train)

        # Predict
        Y_pred = Model.predict(X_test)

        # Accuracy
        Accuracy = accuracy_score(Y_test, Y_pred)

        print("max_depth = {:>4}  -->  {:.2f}%".format(str(Depth), Accuracy * 100))

    print(Border)

    print("\nObservations:")
    print("1. max_depth = 1 creates a simple Decision Tree and usually gives lower accuracy.")
    print("2. max_depth = 3 captures more patterns and generally improves accuracy.")
    print("3. max_depth = None allows the tree to grow completely and often gives the highest training accuracy.")
    print("4. A fully grown tree may overfit the training data.")
    print("5. A moderate depth (such as 3) often provides a better balance between accuracy and generalization.")

if __name__ == "__main__":
    main()