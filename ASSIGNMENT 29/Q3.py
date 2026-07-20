'''
Q3) Copy File Contents into a New File (Command Line)
Problem Statement:

Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt,
and copies all contents from the given file into Demo.txt.

Input (Command Line):

ABC.txt

Expected Output:

Create Demo.txt and copy contents of ABC.txt into Demo.txt.
'''
import sys

def Display(Filename):
    fobj = open(Filename , "r")
    dobj = open("Demo.txt" , "w")

    data = fobj.read()

    dobj.write(data)

    print("Data successfully written")

    dobj.close()
    fobj.close()

def main():
    if len(sys.argv) > 1:
        FileName = sys.argv[1]
        Display(FileName)

    else:
        print("Give an appropriate file name as an input")

    


if __name__ == "__main__":
    main()
