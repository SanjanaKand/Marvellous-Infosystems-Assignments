'''
3. Using pandas functions, calculate and display:
Average StudyHours
Average Attendance
Maximum PreviousScore
Minimum SleepHours
'''
import pandas as pd

def main():
    Border = "-"*120

    print(Border)
    print("Using pandas function to calculate Average StudyHours , Average Attendance, Maximum PreviousScore, Minimum SleepHours")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("Dataset read successfully !")
    print()

    # Average StudyHours
    study_hours = (df["StudyHours"]).mean()
    print("Average Study Hours :" , study_hours)
    print()

    # Average Attendance
    avg_attendance = (df["Attendance"]).mean()
    print("Average Attendance :",avg_attendance)
    print()

    # Maximum PreviousScore
    max_prevscore = (df["PreviousScore"]).max()
    print("Maximum Previous Score :",max_prevscore)
    print()

    # Minimum SleepHours
    min_sleephours = (df["SleepHours"]).min()
    print("Minimum Sleep Hours :" ,min_sleephours)
    print()



if __name__ == "__main__":
    main()