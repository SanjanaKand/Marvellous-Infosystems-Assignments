'''
Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

Input: 11
Output: Positive Number

Input: -8
Output: Negative Number

Input: 0
Output: Zero


'''
def Checker(Number):
    if ( Number == 0):
        print("Zero")
    elif ( Number > 0):
        print("Positive Number")
    elif ( Number < 0):
        print("Negative Number")
    else:
        print("Invalid Number")


def main():
    Number = int(input("Enter a Number :"))

    Checker(Number)

   

if __name__ == "__main__":
    main()