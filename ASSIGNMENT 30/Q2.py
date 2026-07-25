'''
2. Write a Python program that displays the current date and time after every one minute.

Use the datetime module.

Expected Output:

Current Date and Time: 25-07-2026 04:30:00 PM
'''

from datetime import datetime
import schedule
import time

def DisplayDateTime():
    currenttime = datetime.now()
    print("Current Date and Time :", currenttime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():

    schedule.every(1).minute.do(DisplayDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

'''
| Format | Meaning         | Example |
| ------ | --------------- | ------- |
| `%d`   | Day             | 25      |
| `%m`   | Month           | 07      |
| `%Y`   | Year (4 digits) | 2026    |
| `%y`   | Year (2 digits) | 26      |
| `%H`   | Hour (24-hour)  | 16      |
| `%I`   | Hour (12-hour)  | 04      |
| `%M`   | Minutes         | 30      |
| `%S`   | Seconds         | 15      |
| `%p`   | AM/PM           | PM      |

'''

