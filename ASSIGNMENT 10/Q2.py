# Write a program which accepts one number and prints sum of first N natural numbers
# INPUT : 5
# OUTPUT : 15

# formula = n(n+1)/2
def Function(No1):
    Ans = int(No1 * (No1 + 1) / 2)
    print("Sum of first N natural number of",No1,"is :",Ans)


def main():
    No1 = int(input("Enter a number :"))
    Function(No1)

if __name__ == "__main__":
    main()