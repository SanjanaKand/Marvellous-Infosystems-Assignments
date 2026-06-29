# Write a program which accepts two numbers and prints ADDITION , SUBTRACTION , MULTIPLICATION and DIVISION

def Calculator(No1,No2):
    Addition = No1 + No2
    Subtraction = No1 - No2
    Multiplication = No1 * No2
    Division = No1 / No2
    
    print("Addition is :",Addition)
    print("Subtraction is :",Subtraction)
    print("Multiplication is :",Multiplication)
    print("Division is :",Division)

def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))
    Ret =  Calculator(No1 , No2)
    

if __name__ == "__main__":
    main()