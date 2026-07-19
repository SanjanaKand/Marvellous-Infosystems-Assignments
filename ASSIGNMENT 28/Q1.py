'''
Q1) Count Lines in a File
Problem Statement:

Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:

Demo.txt

Expected Output:

Total number of lines in Demo.txt.

'''

def main():

    FileName = input("Enter file name :")
    fobj = open(FileName , "r")

    count = 0
    for i in fobj:
        count = count + 1
    
    print(f"Total no of lines are : {count}")


if __name__ == "__main__":
    main()