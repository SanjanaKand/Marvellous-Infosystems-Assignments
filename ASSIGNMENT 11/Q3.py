# Write a program which accepts one number and prints sum of digits
# INPUT : 123
# OUTPUT : 6


def SummationOfDigits(Data):
    Sum = 0
    for i in range(len(Data)):
        Sum = Sum + int(Data[i])
    return Sum

def main():
    No1 = input("Enter a number greater than 1 digit :")
    print(type(No1))
    Ret = SummationOfDigits(No1)
    print("The sum of digits of",No1,"is :", Ret)

if __name__ == "__main__":
    main()