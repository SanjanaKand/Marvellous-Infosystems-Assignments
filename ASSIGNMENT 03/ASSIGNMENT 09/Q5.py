# Write a program which accepts one number and checks whether it is divisible by 3 and 5 
# INPUT : 15
# OUTPUT : Divisible by 3 and 5 
# Such a number where the remainder is 0

def Function(No1):
    if (No1 % 3 == 0 and No1 % 5 == 0):
        print(No1,"is divisble by 3 and 5 ")
    else:
        print(No1,"is NOT divisible by 3 and 5")
    
def main():
    No1 = int(input("Enter a number :"))
    Function(No1)
    
if __name__ == "__main__":
    main()