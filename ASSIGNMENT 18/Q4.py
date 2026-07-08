'''
Write a program which accepts N numbers from the user and stores them into a List. Accept one another number from the user and return the frequency of that number from the List.

Input:

Number of elements: 11
Elements: 13 5 45 7 4 56 5 34 2 5 65
Element to search: 5

Output:

3

'''
def Frequency(Numbers , Search):
    Count = 0
    
    for i in Numbers:
        
        if Search == i:
            Count = Count  + 1
    return Count


def main():
    max_elements = int(input("Enter count of total number of elements :"))
    Numbers = list(map(int , input("Enter the numbers :").split(",")))
    print(Numbers)
    Search = int(input("Enter the element you want to search :"))
    
    Ret = Frequency(Numbers , Search)

    print(f"Frequency of {Search} in list {Numbers} is :" , Ret)

if __name__ == "__main__":
    main()