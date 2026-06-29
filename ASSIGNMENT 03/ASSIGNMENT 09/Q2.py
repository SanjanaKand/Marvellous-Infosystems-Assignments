# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number
# INPUT : 10 20
# OUTPUT : 20 is greater

#business logic
def ChkGreater(No1 , No2):
    if (No1 > No2):
        print(No1,"is greater")
    else:
        print(No2,"is greater")

# input and print
def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))

    ChkGreater(No1 , No2)
    
if __name__ == "__main__":
    main()