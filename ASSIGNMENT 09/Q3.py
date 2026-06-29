# Write a program which accepts one number and prints square of that number
# INPUT : 5
# OUTPUT : 25

def Square(No1):
    return No1 * No1
   
def main():
    No1 = int(input("Enter a number :"))
    Ans = Square(No1)
    print("Square is :",Ans)
    
if __name__=="__main__":
    main()