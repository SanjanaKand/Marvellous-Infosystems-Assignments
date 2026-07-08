'''
Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5, otherwise returns False.

Input: 8
Output: False

Input: 25
Output: True


'''
def Divisible(Number):
    if ( Number % 5 == 0 ):
        print("True")
    else:
        print("False")

def main():
    Number = int(input("Enter a Number :"))

    Divisible(Number)

if __name__ == "__main__":
    main()