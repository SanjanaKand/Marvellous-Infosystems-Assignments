# Write a program which accepts a number and checks whether it is prime or not
# INPUT : 11
# OUTPUT : PRIME NUMBER

'''
Algorithm
Accept a number No.
If No <= 1, it is not prime.
Check if No is divisible by any number from 2 to No-1.
If it is divisible, it is not prime.
Otherwise, it is prime.

'''
def PrimeChecking(No):
    if (No <= 1):
        return "is not a prime number"
    for i in range (2, No):
        if No % i == 0:
          return "is not a prime number"
    return "is a prime number"
    

def main():
    No = int(input("Enter a number :"))

    Ret = PrimeChecking(No)

    print(No , Ret)

if __name__ == "__main__":
    main()