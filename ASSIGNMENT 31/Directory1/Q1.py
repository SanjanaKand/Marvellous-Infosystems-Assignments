'''
1. Write a program that accepts:
A message from the user
A time interval in seconds

Schedule the program to display the message repeatedly after the specified interval.

Example Input:
Enter message: Jay Ganesh
Enter interval in seconds: 5
Expected Output:
Jay Ganesh
every five seconds.

Validate that the interval is greater than zero.
'''
import time
import schedule

def Display(message ):
    print(message)

def main():
    Message = input("Enter message :")
    Interval = int(input("Enter interval :"))

    if Interval > 0:
        schedule.every(Interval).seconds.do(Display , Message)
    else:
        print("Invalid Interval : The interval must be greater than 0 .")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()