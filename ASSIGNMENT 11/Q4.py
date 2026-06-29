# Write a program which accepts one number and prints reverse of that number
# INPUT : 123
# OUTPUT : 321

def Reverse(No):
    return No[::-1]

def main():
    No = input("Enter a number more than 2 digit :")

    Ret = Reverse(No)

    print("Reverse of the number is :",Ret)

if __name__ == "__main__":
    main()