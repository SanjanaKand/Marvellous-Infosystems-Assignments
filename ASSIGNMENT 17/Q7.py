'''
Write a program which accepts one number and displays the below pattern.

Input:

5

Output:

1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5


'''
def Pattern(Num1):
    for i in range (1 , Num1 + 1):
        print()
        for i in range(1 , Num1 +1):
            print(i , end=" ")
            
def main():
    Num1 = int(input("Enter a Number :"))

    Pattern(Num1)


if __name__ == "__main__":
    main()