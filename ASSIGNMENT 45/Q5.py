'''
Q5 : Add a new column 'Status' where students with Total >= 250 are 'Pass', else 'Fail'.
'''
import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Calculate Total Marks across Math, Science, and English
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    
    # Assign 'Status' based on condition: Pass if Total >= 250, else Fail
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    
    print(df)

if __name__ == "__main__":
    main()