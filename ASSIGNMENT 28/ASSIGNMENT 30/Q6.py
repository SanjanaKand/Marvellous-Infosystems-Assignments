'''
6. Write a script that schedules the following tasks:
Print Lunch Time! every day at 1:00 PM.
Print Wrap up work every day at 6:00 PM.

Both tasks should be handled by separate functions.
'''
import time
import schedule
from datetime import datetime

def Task1():
    print(f"Lunch Time! every day at 1:00 PM.")

def Task2():
    print(f"Wrap up work every day at 6:00 PM.")

def main():
    schedule.every().day.at("13:00").do(Task1)
    schedule.every().day.at("18:00").do(Task2)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()