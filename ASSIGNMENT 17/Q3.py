'''
Write a program which accepts one number from the user and returns its factorial.

Input:

5

Output:

120

'''
def Factorial(No):
    Fact = 1
    for i in range(1,No + 1):
        Fact = Fact * i
    return Fact



def main():
    No = int(input("Enter a Number :"))

    Ret = Factorial(No)

    print(f"Factorial of {No} is",Ret)

if __name__ == "__main__":
    main()