'''
Q5) Frequency of a String in File
Problem Statement:

Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input:

Demo.txt
Marvellous

Expected Output:

Count how many times "Marvellous" appears in Demo.txt.
'''
def Checking(filename , stringname):
    fobj = open(filename , "r")

    count = 0

    for line in fobj:
        
        if stringname.lower() in line.lower():
            count = count + line.lower().count(stringname.lower())
    print(f"Frequency is {count}")

def main():
    FileName = input("Enter file name :")

    StringName = input("Enter one word to check the frequency of that word :")

    Checking(FileName , StringName)
if __name__ == "__main__":
    main()