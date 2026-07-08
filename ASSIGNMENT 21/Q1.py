'''
Design a Python application that creates two threads named Prime and NonPrime.

Both threads should accept a list of integers.
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list.
'''

import threading

def IsPrime(No):
    if No <= 1 :
        return False
    
    for i in range(2, No):
        if No % i == 0:
            return False

    return True
    
def Prime(Numbers):
    print("Prime Numbers :")
    for i in Numbers:
        if IsPrime(i):
            print(i, end=" ")

def NonPrime(Numbers):
    print("Non Prime Numbers:")
    for i in Numbers:
        if not IsPrime(i):
            print(i, end=" ")
        
def main():
    Numbers = list(map(int , input("Enter N Numbers :").split(",")))
    print("-"*15)
    print("LIST of Numbers you entered are :",Numbers)

    Thread1 = threading.Thread(target=Prime , args=(Numbers,))
    Thread2 = threading.Thread(target=NonPrime , args=(Numbers,))

    Thread1.start()
    Thread2.start()



    Thread1.join()
    Thread2.join()



if __name__ == "__main__":
    main()

