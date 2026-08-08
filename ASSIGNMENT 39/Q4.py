'''
4. Generate confusion matrix using sklearn.

Display it using ConfusionMatrixDisplay.

Explain clearly:

True Positive
True Negative
False Positive
False Negative
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def main():

    Border = "-" * 60

    print(Border)
    print("Confusion Matrix using Decision Tree")
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

    # Generate confusion matrix
    CM = confusion_matrix(Y_test, Y_pred)

    # Display confusion matrix
    Display = ConfusionMatrixDisplay(confusion_matrix=CM,
                                     display_labels=["Fail", "Pass"])

    Display.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()

    print("\nConfusion Matrix")
    print(CM)

    print("\nExplanation")
    print("True Positive (TP)  : Student actually passed and the model predicted Pass.")
    print("True Negative (TN)  : Student actually failed and the model predicted Fail.")
    print("False Positive (FP) : Student actually failed but the model predicted Pass.")
    print("False Negative (FN) : Student actually passed but the model predicted Fail.")

    print(Border)

if __name__ == "__main__":
    main()