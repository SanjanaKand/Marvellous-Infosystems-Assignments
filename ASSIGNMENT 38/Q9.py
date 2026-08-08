'''
9. Create a plot showing the relationship between AssignmentsCompleted and FinalResult.

Explain your observation.
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():

    Border = "-" * 60

    print(Border)
    print("AssignmentsCompleted vs FinalResult")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Calculate average assignments completed
    Result = df.groupby("FinalResult")["AssignmentsCompleted"].mean()

    # Labels
    Labels = ["Fail", "Pass"]

    # Bar Plot
    plt.figure(figsize=(6,5))

    plt.bar(Labels,
            Result,
            color=["red", "green"],
            edgecolor="black")

    plt.title("Average Assignments Completed by Final Result")
    plt.xlabel("Final Result")
    plt.ylabel("Average Assignments Completed")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.show()

    print("\nAverage Assignments Completed")
    print("Fail :", round(Result[0], 2))
    print("Pass :", round(Result[1], 2))

    print("\nObservation:")
    print("1. Students who passed completed more assignments on average.")
    print("2. Students who failed completed fewer assignments.")
    print("3. Assignment completion has a positive impact on academic performance.")
    print("4. Completing more assignments increases the likelihood of passing.")

if __name__ == "__main__":
    main()