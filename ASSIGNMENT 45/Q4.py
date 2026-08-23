'''
Q4 : Plot a pie chart of subject marks for 'Sagar'.
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
    
    # Extract row corresponding to 'Sagar'
    sagar_data = df[df['Name'] == 'Sagar'].iloc[0]
    
    # Extract subjects and their scores
    subjects = ['Math', 'Science', 'English']
    scores = [sagar_data[subject] for subject in subjects]
    
    # Plotting the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(
        scores, 
        labels=subjects, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=['#155dfc', '#6395e8', '#e8f0fe']
    )
    plt.title("Subject Marks for Sagar")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()