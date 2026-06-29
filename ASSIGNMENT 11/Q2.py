# Write a program which accepts one number and print count of digits in that number
# INPUT : 7521
# OUTPUT : 4


def TotalNumberCount(No1):
    return (len(No1))
        

def main():
    No1 = input("Enter a number of 2 digits or more :") # 3456
    Ret = TotalNumberCount(No1)
    print("Total number of digits in",No1,"is :", Ret)

if __name__ == "__main__":
    main()