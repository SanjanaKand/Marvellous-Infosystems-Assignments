'''
5. Schedule a task that executes every five minutes.

The task should write the current date and time into a file named:

Marvellous.txt

New entries should be appended without removing previous entries.

Example file content:

Task executed at: 25-07-2026 04:30:00 PM
Task executed at: 25-07-2026 04:35:00 PM
'''
import schedule
import time
from datetime import datetime


def Display(timedate):
    File = open("Marvellous.txt" , "a")
    File.write("Task executed at :")
    File.write(timedate.strftime("%d-%m-%Y %I:%M:%S %p"))
    print()

    File.close()

def main():
    timedate = datetime.now()
    schedule.every(5).minutes.do(Display , timedate)
    
    Display(timedate)
    #  print("Current Date and Time :", currenttime.strftime("%d-%m-%Y %I:%M:%S %p"))

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()