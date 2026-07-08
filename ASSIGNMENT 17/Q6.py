'''
Write a program which accepts one number and displays the below pattern.

Input:

5

Output:

*           *
* *       * *
* * *   * * *
* *       * *
*           *


'''
def Pattern(Num1):
    for i in range(1, Num1 + 1):
        for j in range(1, Num1 + 1):

            if i <= (Num1 + 1) // 2:
                if j <= i or j >= Num1 - i + 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            else:
                if j <= Num1 - i + 1 or j >= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

        print()

def main():
    Num1 = int(input("Enter a Number : "))
    Pattern(Num1)

if __name__ == "__main__":
    main()