'''
Create one module named as Arithmetic which 
contains 4 functions as Add() for addition, Sub() for subtraction,
 Mult() for multiplication and Div() for division. All functions accept two parameters as number and perform the operation.
 Write one Python program which calls all the functions from the Arithmetic module by accepting the parameters from the user.
'''


import Arithmetic

def main():
    Num1 = int(input("Enter first Number :"))
    Num2 = int(input("Enter second Number :"))

    print("Addition is :",Arithmetic.Add(Num1 , Num2))
    print("Subtraction is :",Arithmetic.Sub(Num1 , Num2))
    print("Multiplication is :",Arithmetic.Multi(Num1 , Num2))
    print("Division is :",Arithmetic.Div(Num1 , Num2))


if __name__ == "__main__":
    main()

