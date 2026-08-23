'''
Q10 : Drop the 'English' column from the original DataFrame
'''
import pandas as pd

Border = "-"*60

def main():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    df = df.drop('English', axis=1)

    print(Border)

    print("DataFrame after dropping 'English' column:")
    print(df)

if __name__ == "__main__":
    main()