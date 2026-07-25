'''
3. Write a program that schedules a function to print:

Coding Kar...

every 30 minutes.
'''
import time
import schedule


def DisplayTxt():
     print("Coding Kar...")


def main():
    
    schedule.every(30).minutes.do(DisplayTxt)

    text = "Coding kar..."

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()