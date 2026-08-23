'''
Q1:

Create a DataFrame for student marks and print basic information like shape, columns, and data types.

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
'''
import pandas as pd

Border = "-"*50

Data = {
    "Name" : ["Amit" , "Sanjana" , "Dattatraya" , "Aarti"] ,
    "Math" : [85,90,67,89] ,
    "Science" : [93,45,67,89] ,
    "English" : [23,45,78,66]
}

print(Border)
print("Normal printing without dataframe :\n")
print(Border)
print(Data)

print("----------------------------------------------------------")

print("DataFrame printing :\n")
df = pd.DataFrame(Data)
print(df)


print(Border)
print(f"Shape of the dataset :")
print(df.shape)
print(Border)

print(f"Columns present in the dataset : {df.columns}")
print(Border)

print(f"Data types of the dataset :")
print(df.dtypes)

print(Border)
