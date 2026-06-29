# Write a program which accepts one number and prints all odd numbers till that number

def OddNumbers(No1):
    for i in range(1 , No1 + 1):
        if (i % 3 == 0):
            print(i)

def main():
    No1 = int(input("Enter a number :"))
    OddNumbers(No1)

if __name__ == "__main__":
    main()