'''
2. Write a Python program that monitors the size of a specified file every 30 seconds.

Write the following details into:

FileSizeLog.txt

Include:

File path
File size in bytes
Date and time

Handle the situation where the file does not exist.
'''
import time
import schedule
from datetime import datetime
import os


def LogicFunction(filename):

    if not os.path.isfile(filename):
        print("File does not exists...")
        return

    size = os.path.getsize(filename)
    date = datetime.now().strftime("%d:%m:%Y ")
    timevar =  datetime.now().strftime("%I:%M:%S %p")
    filepath = os.path.abspath(filename)

    fobj = open("FileSizeLog.txt" , "a")

    fobj.write("\n------------------------------------\n")

    fobj.write(f"File name is {filename}""\n")
    fobj.write(f"File Path : {filepath}""\n")
    fobj.write(f"Fize size in bytes is {size}""\n")
    fobj.write(f"Current date : {date}""\n")
    fobj.write(f"Current time : {timevar}""\n")


    fobj.close()

def main():
    Filename = input("Enter File name :")

    schedule.every(30).seconds.do(LogicFunction , Filename)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()

'''
| Function                    | Purpose                               |
| --------------------------- | ------------------------------------- |
| `os.path.abspath(filename)` | Returns the absolute path of the file |
| `os.path.dirname(path)`     | Returns the directory path            |
| `os.path.basename(path)`    | Returns only the filename             |
| `os.path.split(path)`       | Returns `(directory, filename)`       |

'''