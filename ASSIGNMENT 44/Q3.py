'''
Q3:

Add a new column 'Total' to the DataFrame as the sum of all subject marks.

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

print("Total column added in the dataset :")
df["Total"] = df["Math"] + df["Science"] + df["English"]

print(df)

print(Border)