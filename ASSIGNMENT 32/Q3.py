'''
3. Write a program that reads and displays the contents of a specified text file every minute.

Handle the following conditions:

File does not exist
File is empty
Permission is denied
File cannot be opened
'''
import schedule
import time
import os

def LogicFunction(filename):

    try:

        if not os.path.isfile(filename):
            print("File does not exist.")
            return

        if os.path.getsize(filename) == 0:
            print("File is empty.")
            return

        fobj = open(filename, "r")

        print("\nContents of the file:\n")
        print(fobj.read())

        fobj.close()

    except PermissionError:
        print("Permission is denied.")

    except FileNotFoundError:
        print("File cannot be opened.")

    except Exception as e:
        print("Error :", e)

def main():

    filename = input("Enter file name : ")

    schedule.every(1).minutes.do(LogicFunction, filename)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()