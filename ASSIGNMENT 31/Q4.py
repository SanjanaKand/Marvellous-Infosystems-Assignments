'''
4. Write a program that creates a new log file after every ten minutes.

The filename should contain the current date and time.

Example:
MarvellousLog_25_07_2026_16_30_00.txt

The file should contain:

Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM
'''
import time
import schedule
from datetime import datetime

def LogicFuntion():
    currenttime = datetime.now()

    filename = "MarvellousLog_" + currenttime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(filename , "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : " + currenttime.strftime("%d-%m-%Y %I:%M:%S %p"))

    fobj.close()

    print(filename, "created successfully.")

def main():

    schedule.every(10).minutes.do(LogicFuntion)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
