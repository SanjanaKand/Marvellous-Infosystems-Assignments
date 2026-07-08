'''
Design a Python application that creates two threads.

Thread 1 should calculate and display the maximum element from a list.
Thread 2 should calculate and display the minimum element from the same list.
The list should be accepted from the user.

'''
import threading

def Maximum(Numbers):
    for i in (Numbers):
        print(max(i))

def Minimum(Numbers):
    for i in (Numbers):
        print(min(i))

def main():
    Numbers = list(map(int, input("Enter N Numbers :").split(",")))

    Thread1 = threading.Thread(target=Maximum , args=(Numbers , ))
    Thread2 = threading.Thread(target=Minimum , args=(Numbers , ))

    Thread1.start()
    Thread2.start()

if __name__ == "__main__":
    main()



