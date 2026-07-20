'''
Q4) Compare Two Files (Command Line)
Problem Statement:

Write a program which accepts two file names through command line arguments and compares the contents of both files.

If both files contain the same contents, display Success.
Otherwise, display Failure.

Input (Command Line):

Demo.txt Hello.txt

Expected Output:

Success or Failure

'''
import sys 
import os
import hashlib  # functions of checksum calculations present in hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName , "rb") # rb : read binary - binary IO

    hobj = hashlib.md5() # md5 is a class , we hve created a obj named hobj of class md5

    Buffer = fobj.read(1000)

    while len(Buffer) > 0 :
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return  hobj.hexdigest()


def main():
    if len(sys.argv) == 3:
        File1 = sys.argv[1]
        File2 = sys.argv[2]

        if os.path.exists(File1) and os.path.exists(File2):
            Ret1 = CalculateCheckSum(File1)
            Ret2 = CalculateCheckSum(File2)

            if Ret1 == Ret2:
                print("Success")
            else:
                print("Failure")
        else:
            print("Failure")
    else:
        print("Invalid arguments")


if __name__ == "__main__":
    main()