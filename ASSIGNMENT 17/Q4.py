'''
Write a program which accepts one number from the user and returns the addition of its factors.

Input:

12

Output:

16
(1 + 2 + 3 + 4 + 6)


'''
# factor of a number is a number that divides the given number exactly, leaving a remainder of 0.

def Addition(Num1):
    Sum = 0
    for i in range (1, Num1):
        if Num1 % i == 0:
          Sum = Sum + i
          print(f"Factors of {Num1} are :",i)
          
    return Sum
    
def main():
    Num1 = int(input("Enter a Number :"))

    Ret = Addition(Num1)

    print(f"Addition of factors of number {Num1} is : {Ret}")

if __name__ == "__main__":
    main()