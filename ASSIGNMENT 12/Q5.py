# Write a program which accepts one numbre and prints that many numbers in reverse order
# INPUT : 5
# OUTPUT : 5 4 3 2 1

def ReverseNumbers(No):
    for i in range(No, 0 ,-1):
        print("Reverse output is :",i)

def main():
    No = int(input("Enter a number :"))
    ReverseNumbers(No)

if __name__ == "__main__":
    main()