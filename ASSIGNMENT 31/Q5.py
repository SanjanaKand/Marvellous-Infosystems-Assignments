'''
5. Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.

Write the result into:

DirectoryCountLog.txt

Each entry should contain:

Directory path
Number of files
Date and time
'''
import time
import schedule
from datetime import datetime
import os

def Result(DirectoryName):

    if not os.path.isdir(DirectoryName):
        print("Directory does not exist.")
        return

    filecount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:
            filecount = filecount + 1

    fobj = open("DirectoryCountLog.txt", "a")

    CurrentTime = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj.write(f"Directory Path : {DirectoryName}\n")
    fobj.write(f"Number of Files : {filecount}\n")
    fobj.write(f"Date and Time : {CurrentTime}\n")
    fobj.write("--------------------------------------------\n")

    fobj.close()

    print("Log updated successfully.")

def main():

    DirectoryName = input("Enter Directory Name : ")

    schedule.every(5).minutes.do(Result, DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()