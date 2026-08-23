'''
Q1 : Normalize the 'Math' scores using Min-Max scaling.

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
    
    # (x - min) / (max - min)
    min_math = df['Math'].min()
    max_math = df['Math'].max()
    
    df['Math_Normalized'] = (df['Math'] - min_math) / (max_math - min_math)
    
    print(df)

if __name__ == "__main__":
    main()