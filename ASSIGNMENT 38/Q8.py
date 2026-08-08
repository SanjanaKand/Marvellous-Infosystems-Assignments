'''
8. Draw a boxplot for Attendance.

Identify if any outliers are present.
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():

    Border = "-" * 50

    print(Border)
    print("Boxplot of Attendance")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Draw Boxplot
    plt.figure(figsize=(6,6))

    plt.boxplot(df["Attendance"],
                patch_artist=True,
                boxprops=dict(facecolor="lightblue"),
                medianprops=dict(color="red", linewidth=2))

    plt.title("Boxplot of Attendance")
    plt.ylabel("Attendance (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.show()

    # Detect Outliers using IQR Method
    Q1 = df["Attendance"].quantile(0.25)
    Q3 = df["Attendance"].quantile(0.75)
    IQR = Q3 - Q1

    LowerLimit = Q1 - 1.5 * IQR
    UpperLimit = Q3 + 1.5 * IQR

    Outliers = df[(df["Attendance"] < LowerLimit) |
                  (df["Attendance"] > UpperLimit)]

    print("\nNumber of Outliers :", len(Outliers))

    if len(Outliers) > 0:
        print("\nAttendance Outlier Values")
        print(Outliers["Attendance"].values)
    else:
        print("\nNo Outliers Found.")

    print("\nObservation:")
    if len(Outliers) > 0:
        print("1. The boxplot shows a few attendance values outside the whiskers.")
        print("2. These values are considered outliers.")
        print("3. Most attendance values lie within the normal range.")
        print("4. The distribution is concentrated around the median attendance.")
    else:
        print("1. The boxplot does not show any significant outliers.")
        print("2. Most attendance values are within the expected range.")
        print("3. The attendance distribution is fairly consistent.")
        print("4. The dataset does not contain unusual attendance values.")

if __name__ == "__main__":
    main()