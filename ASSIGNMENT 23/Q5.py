# Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing Pool.



import multiprocessing
import os

def Factorial(Numbers):
    print(f"Process ID : {os.getpid()}")
    Fact = 1
    for i in range(1,Numbers + 1):
        Fact = Fact * i
    return Fact

def main():
    Numbers = list(map(int , input("Enter N Numbers :").split(",")))
    print(f"Input numbers are : {Numbers}")

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial , Numbers)

    print("Factorial :",Result)



if __name__ == "__main__":
    main()