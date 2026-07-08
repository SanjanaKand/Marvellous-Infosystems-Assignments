'''
Write a program which accepts a number from the user and prints that number of "*" on the screen.

Input: 5

Output:

* * * * *


'''

def Pattern(Number):
    for i in range(1,Number + 1):
        print("*" , end="")

def main():
    Number = int(input("Enter a Number :"))

    Pattern(Number)

if __name__ == "__main__":
    main()