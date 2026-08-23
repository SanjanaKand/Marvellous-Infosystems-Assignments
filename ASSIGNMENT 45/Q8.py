'''
Q8 : Plot a histogram of Math marks.
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Plotting the histogram for Math marks
    plt.figure(figsize=(6, 4))
    plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
    
    plt.title('Histogram of Math Marks')
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency')
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    main()