# Write a Python program using multiprocessing Pool to calculate the sum of all odd numbers from 1 to N.

import multiprocessing

def Odd(Numbers):
    Sum = 0
    for i in range(1,Numbers + 1):
        if i % 2 != 0:
            Sum = Sum + i
          
    return Sum
        

def main():
    Numbers = list(map(int , input("Enter N Numbers :").split(",")))
    print(f"Input List : {Numbers}")

    Result = []

    Pobj = multiprocessing.Pool()

    Result = Pobj.map(Odd , Numbers)

    Pobj.close()
    Pobj.join()

    print(f"Result is : {Result}")

if __name__ == "__main__":
    main()