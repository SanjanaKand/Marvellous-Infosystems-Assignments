'''
Write a program which accepts N numbers from the user and stores them into a List. Return the addition of all elements from that List.

Input:

Number of elements: 6
Elements: 13 5 45 7 4 56

Output:

130

'''
def Addition(Numbers):
    Sum = 0
    for i in Numbers:
        Sum = Sum + i  
    return Sum

def main():
    Total_Elements = int(input("Enter the count of total number of elements: "))
    
    
    Numbers = list(map(int, input(f"Enter {Total_Elements} numbers separated by spaces: ").split(",")))
    
    Ret = Addition(Numbers)

    print(f"Addition of {Numbers} is: {Ret}")

if __name__ == "__main__":
    main()

