'''
Write a program which accepts one number from the user and checks whether the number is prime or not.

Input:

5

Output:

It is Prime Number

'''
def IsPrime(Num1):
    if Num1 <= 1:
        return " It is Not a Prime Number"
    
    for i in range(2,Num1):
        if Num1 % i == 0:
            return "It is not a Prime Number"
    return  "It is a Prime Number"

def Prime(Num1):
    if IsPrime(Num1):
        return "It is a Prime Number"
    else:
        return "It is not a Prime Number"

def main():
    Num1 = int(input("Enter a Number :"))

    Ret = IsPrime(Num1)

    print(Ret)

if __name__ == "__main__":
    main()