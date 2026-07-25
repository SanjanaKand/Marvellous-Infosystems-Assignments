'''
3. Write a program that scans a specified directory every minute.

The task should display:

Directory name
Number of files
Number of subdirectories
Date and time of scanning

Use the os module.

Example Output:
Directory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4
Scan Time: 25-07-2026 04:30:00 PM
'''
import time
import schedule
import os
from datetime import datetime

def LogicFunction(DirectoryName):

    if not os.path.isdir(DirectoryName):
        print("Directory does not exits")
        return

    print("Directory Scanned :", DirectoryName)

    for FolderName , SubFolder , FileName in os.walk(DirectoryName):

        filecount = 0
        for files in FileName:
            filecount = filecount + 1
        
        foldercount = 0
        for subf in SubFolder:
            foldercount =  foldercount + 1
    
    print("Total Files :", filecount)
    print("Total Subdirectories :", foldercount)
    print("Scan Time :" , datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))



def main():
    DirectoryName = input("Enter the  Directory Name :")

    schedule.every(1).minute.do(LogicFunction , DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()