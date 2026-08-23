'''
Q6:

Sort the DataFrame by 'Total' marks in descending order.

'''
import pandas as pd

def main():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    print(df)

    # Add Total column
    df['Total'] = df['Math'] + df['Science'] + df['English']

    # Sort by Total marks in descending order
    df = df.sort_values(by='Total', ascending=False)

    print(df)

if __name__ == "__main__":
    main()