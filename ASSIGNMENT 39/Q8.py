'''
8. Write a single structured Python program that performs:
Dataset loading
Data analysis
Visualization
Train-test split
Model training
Prediction
Accuracy calculation
Confusion matrix generation
Final conclusion

Your code should include proper comments explaining each step.
'''
######################################################
# Student Performance Prediction using Decision Tree
######################################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

def main():

    Border = "-" * 60

    ######################################################
    # Dataset Loading
    ######################################################

    print(Border)
    print("Dataset Loading...")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("Dataset Loaded Successfully.")
    print(Border)

    ######################################################
    # Data Analysis
    ######################################################

    print("\nData Analysis")
    print(Border)

    print("Columns in Dataset")
    print(df.columns)

    print("\nShape of Dataset :", df.shape)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistical Information")
    print(df.describe())

    ######################################################
    # Visualization
    ######################################################

    print("\nDisplaying Histogram of StudyHours...")

    plt.figure(figsize=(8,5))
    plt.hist(df["StudyHours"],
             bins=10,
             color="skyblue",
             edgecolor="black")

    plt.title("Distribution of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.grid(axis="y")
    plt.show()

    ######################################################
    # Prepare Features and Target
    ######################################################

    X = df[["StudyHours",
            "Attendance",
            "PreviousScore",
            "AssignmentsCompleted",
            "SleepHours"]]

    Y = df["FinalResult"]

    ######################################################
    # Train-Test Split
    ######################################################

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42
    )

    ######################################################
    # Model Training
    ######################################################

    print("\nTraining Decision Tree Model...")

    Model = DecisionTreeClassifier(random_state=42)

    Model.fit(X_train, Y_train)

    print("Model Trained Successfully.")

    ######################################################
    # Prediction
    ######################################################

    Y_pred = Model.predict(X_test)

    print("\nActual\tPredicted")

    for Actual, Predicted in zip(Y_test.values, Y_pred):
        print(Actual, "\t", Predicted)

    ######################################################
    # Predict for New Student
    ######################################################

    Student = [[6,85,66,7,7]]

    Result = Model.predict(Student)

    print("\nPrediction for New Student")

    if Result[0] == 1:
        print("Result : PASS")
    else:
        print("Result : FAIL")

    ######################################################
    # Accuracy Calculation
    ######################################################

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("\nTesting Accuracy : {:.2f}%".format(Accuracy * 100))

    ######################################################
    # Confusion Matrix
    ######################################################

    CM = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix")
    print(CM)

    Display = ConfusionMatrixDisplay(
        confusion_matrix=CM,
        display_labels=["Fail","Pass"]
    )

    Display.plot(cmap="Blues")

    plt.title("Confusion Matrix")

    plt.show()

    ######################################################
    # Final Conclusion
    ######################################################

    print("\nFinal Conclusion")
    print(Border)

    print("1. Dataset loaded successfully.")
    print("2. Data analysis was performed.")
    print("3. Histogram of StudyHours was displayed.")
    print("4. Dataset was divided into training and testing data.")
    print("5. Decision Tree model was trained successfully.")
    print("6. Predictions were generated for test data.")
    print("7. Accuracy of the model was calculated.")
    print("8. Confusion Matrix was displayed.")
    print("9. New student's result was predicted.")
    print("10. The Decision Tree model can effectively predict student performance.")

    print(Border)

if __name__ == "__main__":
    main()