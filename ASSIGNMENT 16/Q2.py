''' Write a program which contains one function named as ChkNum() which accepts one parameter as number. If the number is even then it should display "Even number" otherwise display "Odd number" on console.

Input: 11
Output: Odd Number

Input: 8
Output: Even Number
'''
def ChkNum(No):
    if (No % 2 == 0):
        print(f"{No} is even")
    else:
        print(f"{No} is odd")
    

def main():
    No = int(input("Enter a number :"))
    ChkNum(No)

if __name__ == "__main__":
    main()