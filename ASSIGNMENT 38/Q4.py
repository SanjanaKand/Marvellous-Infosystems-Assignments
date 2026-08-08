'''
4. Use value_counts() to analyze the distribution of FinalResult.

Calculate the percentage of Pass and Fail students.

Is the dataset balanced? Justify your answer.
'''

import pandas as pd

def main():

    Border = "-" * 45

    print(Border)
    print("Distribution of FinalResult")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("Dataset read successfully!")

    # Distribution of FinalResult
    result = df["FinalResult"].value_counts()

    print("Distribution of FinalResult:")
    print(result)

    # Total students
    total_students = len(df)

    # Calculate the percentage of Pass and Fail students.
    pass_count = result[1]
    fail_count = result[0]

    pass_percentage = (pass_count / total_students) * 100
    fail_percentage = (fail_count / total_students) * 100

    print(f"Pass Percentage : {pass_percentage:.2f}%")
    print(f"Fail Percentage : {fail_percentage:.2f}%")

    # Check whether dataset is balanced
    if abs(pass_percentage - fail_percentage) <= 10:
        print("\nThe dataset is balanced.")
    else:
        print("\nThe dataset is not balanced.")

if __name__ == "__main__":
    main()