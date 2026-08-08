'''
10. Plot SleepHours against FinalResult.

Does sleeping more guarantee success? Explain.
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():

    Border = "-" * 60

    print(Border)
    print("SleepHours vs FinalResult")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Calculate average sleep hours
    Result = df.groupby("FinalResult")["SleepHours"].mean()

    # Labels
    Labels = ["Fail", "Pass"]

    # Bar Plot
    plt.figure(figsize=(6,5))

    plt.bar(Labels,
            Result,
            color=["red", "green"],
            edgecolor="black")

    plt.title("Average Sleep Hours by Final Result")
    plt.xlabel("Final Result")
    plt.ylabel("Average Sleep Hours")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.show()

    print("\nAverage Sleep Hours")
    print("Fail :", round(Result[0], 2))
    print("Pass :", round(Result[1], 2))

    print("\nObservation:")
    print("1. Students who passed and failed have similar average sleep hours.")
    print("2. Sleep is important for health and concentration, but it is not the only factor affecting performance.")
    print("3. Study hours, attendance, previous scores, and assignment completion also influence the final result.")
    print("4. Therefore, sleeping more alone does not guarantee academic success.")

if __name__ == "__main__":
    main()