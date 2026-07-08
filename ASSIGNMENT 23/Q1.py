# Write a Python program using multiprocessing Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.
import multiprocessing
import os
import time

def Summation(Numbers):
    print("Process running with ID :",os.getpid())
    Sum = 0
    for i in range (1 , Numbers + 1):
        if i % 2 == 0:
            Sum = Sum + i
    return Sum
    

def main():
    Numbers = list(map(int , input("Enter N Numbers :").split(",")))
    print(Numbers)
    Result = []

    

    pobj = multiprocessing.Pool()

    Result = pobj.map(Summation ,Numbers)

    pobj.close()
    pobj.join()

   

    print(f"Result is : {Result}")


if __name__ == "__main__":
    main()