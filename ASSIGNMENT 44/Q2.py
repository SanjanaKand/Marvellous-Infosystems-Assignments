'''
Q2:

Use the DataFrame from Q1 and print descriptive statistics using .describe().
'''
import pandas as pd

Border = "-"*60

Data = {
    "Name" : ["Amit" , "Sanjana" , "Dattatraya" , "Aarti"] ,
    "Math" : [85,90,67,89] ,
    "Science" : [93,45,67,89] ,
    "English" : [23,45,78,66]
}

print("Normal printing without dataframe :\n")
print(Data)

print(Border)

print("DataFrame printing :\n")
df = pd.DataFrame(Data)
print(df)

print(Border)

print("Descriptive statistics of the Dataset :\n")
print(df.describe())

print(Border)

