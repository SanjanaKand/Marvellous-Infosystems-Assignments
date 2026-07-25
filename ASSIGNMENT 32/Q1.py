'''
1. Write a program that creates a new text file every minute.

The filename should contain the current timestamp.

Example:
File_25_07_2026_16_30_00.txt

Write the following information into the file:

Filename
Creation date
Creation time
'''
import time
import schedule
from datetime import datetime

def Function():
    currenttime = datetime.now()

    filename = "File_" + currenttime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(filename , "w")

    fobj.write(f"Filename : {filename}\n")
    CurrentDate = datetime.now().strftime("%d-%m-%Y")
    CurrentTime = datetime.now().strftime("%I:%M:%S %p")

    fobj.write(f"Date : {CurrentDate} \n")
    fobj.write(f"Time : {CurrentTime} \n")

    fobj.close()

def main():
    schedule.every(1).minute.do(Function)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()