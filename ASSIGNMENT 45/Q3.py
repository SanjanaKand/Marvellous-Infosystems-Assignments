'''
Q3 : Group students by gender and calculate average marks.
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
    
    # Add Gender column
    df['Gender'] = ['Male', 'Male', 'Female']
    
    # Group by Gender and calculate mean for numerical subject columns
    subject_cols = ['Math', 'Science', 'English']
    avg_marks = df.groupby('Gender')[subject_cols].mean()
    
    print(avg_marks)

if __name__ == "__main__":
    main()