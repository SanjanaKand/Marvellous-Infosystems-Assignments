'''
Q2) Count Words in a File
Problem Statement:

Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:

Demo.txt

Expected Output:

Total number of words in Demo.txt.
'''

def TotalWords(FileName):
    fobj = open(FileName , "r")

    data = fobj.read()

    words = data.split()

    length = len(words)

    fobj.close()

    return length
    

def main():
    FileName = input("Enter file name :")
    
    Ret = TotalWords(FileName)

    print(f"Total no of words in {FileName} are {Ret}")


if __name__ == "__main__":
    main()