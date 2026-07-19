'''
Q4) Copy File Contents into Another File
Problem Statement:

Write a program which accepts two file names from the user.

First file is an existing file
Second file is a new file

Copy all contents from the first file into the second file.

Input:

ABC.txt
Demo.txt

Expected Output:

Contents of ABC.txt copied into Demo.txt.
'''
def Copy(File1 , File2):
    fobj1 = open(File1 , "r")
    fobj2 = open(File2 , "w")

    fobj = fobj1.read()
   

    fobj2.write(fobj)

    fobj1.close()
    fobj2.close()

    print(f"Contents of {File1} copied into {File2}")
    


def main():
    File1 = input("Enter the name of existing file :")
    File2 = input("Enter a new file name in which you want to copy the contents :")
   
    Copy(File1 , File2)
if __name__ == "__main__":
    main()