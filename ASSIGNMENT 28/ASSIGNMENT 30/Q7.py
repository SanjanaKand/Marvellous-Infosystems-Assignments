'''
7. Write a Python program that performs a file backup every hour.

The program should:

Accept the source file path.
Accept the destination directory path.
Copy the source file to the destination directory.
Add the current date and time to the backup filename.
Write the backup operation details into:
backup_log.txt

Example backup filename: Data_25_07_2026_16_30_00.txt
Example log entry: Backup completed successfully at 25-07-2026 04:30:00 PM

Use the shutil module for file copying.
'''
import shutil
import schedule
import time
from datetime import datetime
import os

def BackupFile(Source, Destination):

    CurrentTime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    NewFile = os.path.join(Destination, "Backup_" + CurrentTime + ".txt")

    shutil.copy(Source, NewFile)

    fobj =  open("backup_log.txt", "a")
    fobj.write("Backup completed successfully at : ")
    fobj.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n")

    print("Backup Completed Successfully")

def main():

    Source = input("Enter Source File Path : ")
    Destination = input("Enter Destination Folder Path : ")

    BackupFile(Source, Destination)

    schedule.every(1).hours.do(BackupFile, Source, Destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()