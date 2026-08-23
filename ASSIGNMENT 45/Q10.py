'''
Q10 : Plot a boxplot for English marks to check distribution and outliers.

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
    
    # Plotting the boxplot for English marks
    plt.figure(figsize=(5, 6))
    plt.boxplot(df['English'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
    
    plt.title("Boxplot of English Marks")
    plt.ylabel("Marks")
    plt.xticks([1], ['English'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    main()