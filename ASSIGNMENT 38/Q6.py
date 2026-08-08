'''
6. Plot a histogram of StudyHours.

Explain what the distribution tells you.
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():

    Border = "-" * 50

    print(Border)
    print("Histogram of StudyHours")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Plot Histogram
    plt.figure(figsize=(8,5))
    plt.hist(
        df["StudyHours"], 
        bins=10, 
        color="skyblue",
        edgecolor="black"
        )

    plt.title("Distribution of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.show()

    print("\nObservation:")
    print("1. Most students study around 4 to 8 hours.")
    print("2. Very few students study extremely low or extremely high hours.")
    print("3. The distribution is fairly balanced with no major outliers.")
    print("4. Students with moderate to high study hours are more common.")
    print("5. Overall, the StudyHours data appears reasonably well distributed.")

if __name__ == "__main__":
    main()