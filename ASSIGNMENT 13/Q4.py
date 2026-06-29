# Write a program which accepts one number and prints binary equivalent

'''
Decimal to Binary :
Accept a number.
Divide the number by 2.
Write down the remainder (0 or 1).
Replace the number with the quotient (// 2).
Repeat Steps 2 to 4 until the number becomes 0.
Read the remainders from bottom to top (reverse order).
The result is the binary equivalent.

'''
def Binary(No):
    if No == 0:
        return "0"
    Binary = ""

    while No > 0:
        Digit = No % 2
        Binary = str(Digit) + Binary
        No = No // 2

    return Binary

def main():
    No = int(input("Enter a number: "))

    Ret = Binary(No)

    print("Binary equivalent is:", Ret)

if __name__ == "__main__":
    main()