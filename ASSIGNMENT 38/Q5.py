'''
5. Based on the dataset values, analyze whether:
Higher StudyHours increase the chance of passing.
Higher Attendance improves FinalResult.

Write your observations in 4-5 lines.
'''
import pandas as pd

def main():

    Border = "-" * 60

    print(Border)
    print("Analysis of StudyHours and Attendance")
    print(Border)

    # Load dataset
    df = pd.read_csv("student_performance_ml.csv")

    # Average StudyHours based on FinalResult
    StudyHours = df.groupby("FinalResult")["StudyHours"].mean()

    # Average Attendance based on FinalResult
    Attendance = df.groupby("FinalResult")["Attendance"].mean()

    print("\nAverage Study Hours")
    print("Fail (0) :", round(StudyHours[0], 2))
    print("Pass (1) :", round(StudyHours[1], 2))

    print("\nAverage Attendance")
    print("Fail (0) :", round(Attendance[0], 2))
    print("Pass (1) :", round(Attendance[1], 2))

    print("\nObservations")
    print("1. Students who passed studied more hours on average than those who failed.")
    print("2. Students who passed also had higher attendance.")
    print("3. Higher StudyHours increase the chance of passing.")
    print("4. Higher Attendance improves the FinalResult.")
    print("5. Both StudyHours and Attendance positively influence student performance.")

    print(Border)

if __name__ == "__main__":
    main()