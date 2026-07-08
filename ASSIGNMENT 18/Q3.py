'''
Write a program which accepts N numbers from the user and stores them into a List. Return the minimum number from that List.

Input:

Number of elements: 4
Elements: 13 5 45 7

Output:

5


'''
def Minimum(Numbers):
    return min(Numbers)


def main():
    Max_elements = int(input("Enter the count of total number of elements :"))
    Numbers = list(map(int , input("Enter N numbers :").split(",")))
    print(Numbers)

    Ret = Minimum(Numbers)

    print(f"The minimum number from list {Numbers} is :" ,Ret)

if __name__ == "__main__":
    main()