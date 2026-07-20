'''
Q2) Display File Contents
Problem Statement:

Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input:

Demo.txt

Expected Output:

Display contents of Demo.txt on console.
'''
def Display(FileName):
    fobj = open(FileName , "r")

    data = fobj.read()

    print("The contents of the file are :")
    print(data)

def main():
    FileName = input("Enter File name :")

    Display(FileName)

if __name__ == "__main__":
    main()