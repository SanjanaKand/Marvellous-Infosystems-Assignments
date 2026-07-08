'''
Write a program which accepts N numbers from the user and stores them into a List. Return the maximum number from that List.

Input:

Number of elements: 7
Elements: 13 5 45 7 4 56 34

Output:

56


'''
def Addition(Numbers):
    return max(Numbers)

def main():
    Max_elements = int(input("Enter the count of total number of elements :"))
    Numbers = list(map(int,input("Enter N Numbers :").split(",")))
    print(Numbers)

    Ret = Addition(Numbers)

    print(F"The maximum number from list {Numbers} is :", Ret)


if __name__ == "__main__":
    main()