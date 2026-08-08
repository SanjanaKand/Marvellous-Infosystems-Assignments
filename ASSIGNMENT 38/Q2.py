'''
2. Write a program to:
Display total number of students in the dataset.
Count how many students Passed (FinalResult = 1).
Count how many students Failed (FinalResult = 0).
'''
import pandas as pd

def main():
    Border = "-"*45

    print(Border)
    print("Displaying total number of students in the dataset.")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("Dataset read successfully !")

    print("Total number of students in the dataset are :")
    print(len(df))

    print("FinalResult = 0 : FAIL")
    print("FinalResult = 1 : PASS")

    # Count how many students Passed (FinalResult = 1).
    passed = (df["FinalResult"] == 1).sum()
    print(f"Total number of students passed : {passed}")

    # Count how many students Failed (FinalResult = 0)
    failed = (df["FinalResult"] == 0).sum()
    print(f"Total number of students failed : {failed}")

if __name__ == "__main__":
    main()