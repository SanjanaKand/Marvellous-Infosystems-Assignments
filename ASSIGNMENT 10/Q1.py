# Write a program which accepts one number and prints multiplication table of that number
# INPUT : 4
# OUTPUT : 4 8 12 16 20 24 28 32 36 40

def Multiplication(No1):
    for i in range(1,11):
        #print(No1 * i)
        print(No1 * i, end=" ")

def main():
    No1 = int(input("Enter a number :"))
    Ans = Multiplication(No1)
    print(Ans)


if __name__=="__main__":
    main()