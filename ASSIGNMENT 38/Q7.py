'''
7. Create a scatter plot of:

StudyHours vs PreviousScore

Use different colors for Pass and Fail students.
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():

    Border = "-" * 55

    print(Border)
    print("Scatter Plot: StudyHours vs PreviousScore")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Separate Pass and Fail students
    Passed = df[df["FinalResult"] == 1]
    Failed = df[df["FinalResult"] == 0]

    # Scatter Plot
    plt.figure(figsize=(8,6))

    plt.scatter(Passed["StudyHours"],
                Passed["PreviousScore"],
                color="green",
                label="Pass",
                alpha=0.7)

    plt.scatter(Failed["StudyHours"],
                Failed["PreviousScore"],
                color="red",
                label="Fail",
                alpha=0.7)

    plt.title("StudyHours vs PreviousScore")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.legend()
    plt.grid(True)

    plt.show()

    print("\nObservation:")
    print("1. Students who passed are mostly clustered in the higher StudyHours and PreviousScore region.")
    print("2. Students who failed generally have lower StudyHours and lower PreviousScore.")
    print("3. There is a positive relationship between StudyHours and PreviousScore.")
    print("4. Higher StudyHours combined with better PreviousScore increases the likelihood of passing.")
    print("5. The scatter plot clearly separates most Pass and Fail students.")

if __name__ == "__main__":
    main()