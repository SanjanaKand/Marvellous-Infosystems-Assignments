# Write a program which accepts one number and checks whether it is palindrome or not
# INPUT : 121
# OUTPUT : PALINDROME

'''
Accept a number.
Store it in another variable (Temp).
Reverse the number.
Compare the original number with the reversed number.
If both are equal → Palindrome.
Otherwise → Not a Palindrome

'''
def Palindrome(No):
    temp = No
    Reverse = temp [::-1]
    if ( temp == Reverse ):
        return "is a Palindrome"
    else:
        return "is not a Palindrome"

def main():
    No = input("Enter a number :")

    Ret = Palindrome(No)

    print(No , Ret)
    
if __name__ == "__main__":
    main()

