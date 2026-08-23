'''
Q9:

Create a DataFrame with missing values and fill them with the column mean.

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}
'''
import pandas as pd
import numpy as np

Border = "-"*60

def main():

    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    df = pd.DataFrame(data2)

    print("Original DataFrame:")
    print(df)

    print(Border)

    # Fill missing values with column mean
    df['Math'] = df['Math'].fillna(df['Math'].mean())
    df['Science'] = df['Science'].fillna(df['Science'].mean())

    print("DataFrame after filling missing values:")
    print(df)

if __name__ == "__main__":
    main()