'''
1. Write a Python program that prints:

Jay Ganesh...

every two seconds.

Use:

schedule.every(2).seconds.do(...)

Expected Output:

Jay Ganesh...
Jay Ganesh...
Jay Ganesh...

'''
import time
import schedule

def LogicFunction(message):
    print(message)

def main():
    Message = "Jay Ganesh..."

    schedule.every(2).seconds.do(LogicFunction , Message)

    LogicFunction(Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()