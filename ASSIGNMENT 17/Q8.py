'''
Write a program which accepts one number and displays the below pattern.

Input:

5

Output:

1
1   2
1   2   3
1   2   3   4
1   2   3   4   5


'''

def Pattern(Num):
    for i in range(1 , Num + 1):
        print()
        for j in range(1 , i + 1):
            print(j , end=" ")


def main():
    Num = int(input("Enter a Number :"))

    Pattern(Num)




if __name__ == "__main__":
    main()