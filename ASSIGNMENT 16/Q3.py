'''
Write a program which contains one function named as Add() which accepts two numbers from user and returns addition of those two numbers.

Input: 11 5
Output: 16


'''
def Add(No1 , No2):
    return No1 + No2


def main():
    No1 = int(input("Enter first Number :"))
    No2 = int(input("Enter second Number :"))

    Ret = Add(No1,No2)
    print(f"Addition of {No1} and {No2} is :",Ret)

if __name__ == "__main__":
    main()