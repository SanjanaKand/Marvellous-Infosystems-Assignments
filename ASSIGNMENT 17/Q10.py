'''
Write a program which accepts a number from the user and returns the addition of digits in that number.

Input:

5187934

Output:

37

'''

def Addition(Number):
    Sum = 0
    for i in Number:
        Sum = Sum + int(i)
    return Sum

def main():
    Number = input("Enter a Number :")

    Ret = Addition(Number)

    print(f"Addition of {Number} is :", Ret)

if __name__ == "__main__":
    main()
'''
from functools import reduce

Numbers = list(map(int, input("Enter a number: ")))

addition = reduce(lambda x ,y : x+y ,Numbers)
print(addition)
'''


