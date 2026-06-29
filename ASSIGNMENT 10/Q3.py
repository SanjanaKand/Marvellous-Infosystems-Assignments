# Write a program which accepts one number and prints factorial of that number
# INPUT : 5
# OUTPUT : 120

# LOGIC : 5! = 5*4*3*2*1

def Factorial(No1):
    Fact = 1
    while ( No1 > 0):
        Fact = Fact * No1
        No1 = No1 - 1

    print("Factorial is:", Fact)


def main():
    No1 = int(input("Enter a number :"))
    Factorial(No1)

if __name__ == "__main__":
    main()



    