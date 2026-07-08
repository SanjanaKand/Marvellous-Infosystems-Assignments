'''
Write a program which accepts one number and displays the below pattern.

Input:

5

Output:

*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *


'''
def Pattern(Num1):
    for i in range(1, Num1 + 1):      # Rows
        for j in range(1, Num1 + 1):  # Columns
            print("*", end=" ")
        print()                      


def main():
    Num1 = int(input("Enter a Number :"))

    Pattern(Num1)

if __name__ == "__main__":
    main()

