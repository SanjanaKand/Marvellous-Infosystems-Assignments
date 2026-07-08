'''
Write a program which accepts a number from the user and returns the number of digits in that number.

Input:

5187934

Output:

7


'''

def Length(Number):
    String = str(Number)
    return len(String)
    

def main():
    Number = int(input("Enter a Number more than 2 digits :"))

    Ret = Length(Number)

    print(f"The number of digits in { Number} is :" , Ret)


if __name__ == "__main__":
    main()