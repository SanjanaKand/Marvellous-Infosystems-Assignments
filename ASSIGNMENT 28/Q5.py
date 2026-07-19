'''
Q5) Search a Word in File
Problem Statement:

Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

Input:

Demo.txt
Marvellous

Expected Output:

Display whether the word Marvellous is found in Demo.txt or not.
'''
def Present(FileName , WordName):
    fobj = open(FileName , "r")
    
    for line in fobj:
        if WordName.lower() in line.lower():
            print(f"{WordName} is present in {FileName}")
            fobj.close()
            return
        
    print(f"{WordName} is not present in {FileName}")
    fobj.close()
        
def main():
    FileName = input("Enter File name :")
    WordName = input("Enter the word to check if it exits in the file or not :")

    Present(FileName , WordName)

if __name__ == "__main__":
    main()