'''
Q4:

Display students who scored more than 85 in Science.

'''
import pandas as pd

Border = "-"*60

Data = {
    "Name" : ["Pooja" , "Sanjana" , "Dattatraya" , "Aarti"] ,
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

print("Students scored than 85 marks in science :")
marks_than_greater = df[df['Science'] > 85]
print(marks_than_greater)

print(Border)