'''
8. Decision Tree Visualization

Use:

from sklearn.tree import plot_tree

Visualize the trained decision tree.

Which feature appears at the root node?
Why do you think that feature was selected first?
'''
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

def main():

    Border = "-" * 65

    print(Border)
    print("Decision Tree Visualization")
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

    # Create Decision Tree model
    Model = DecisionTreeClassifier(random_state=42)

    # Train model
    Model.fit(X_train, Y_train)

    ######################################################
    # Visualize Decision Tree
    ######################################################

    plt.figure(figsize=(18,10))

    plot_tree(Model,
              feature_names=X.columns,
              class_names=["Fail", "Pass"],
              filled=True,
              rounded=True,
              fontsize=10)

    plt.title("Decision Tree for Student Performance Prediction")

    plt.show()

    print(Border)
    print("Decision Tree displayed successfully.")
    print(Border)

if __name__ == "__main__":
    main()