'''
Q6 : Count how many students passed.

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
    
    # Calculate Total Marks and Status
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    
    # Count passed students
    passed_count = (df['Status'] == 'Pass').sum()
    
    print(f"Number of students who passed: {passed_count}")

if __name__ == "__main__":
    main()