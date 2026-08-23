'''
Q7 : Export the final DataFrame to a CSV file.
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
    
    # Add Total and Status columns
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    
    # Export to CSV without the DataFrame index
    output_filename = 'student_marks.csv'
    df.to_csv(output_filename, index=False)
    
    print(f"Data successfully exported to '{output_filename}'")

if __name__ == "__main__":
    main()