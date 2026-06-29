# Write a program which accepts one number and checks whether it is perfect number or not
# INPUT : 6
# OUTPUT : PERFECT NUMBER
'''
Accept a number No.
Initialize Sum = 0.
Start a loop from 1 to No - 1.
Check if i is a factor of No.
If No % i == 0, add i to Sum.
After the loop, compare Sum with No.
If Sum == No, the number is Perfect.
Otherwise, it is Not Perfect.

'''
def PerfectNo(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
    
    if Sum == No:
        return "is a Perfect Number"
    else:
        return "is Not a Perfect Number"


def main():
    No = int(input("Enter a number :"))

    Ret = PerfectNo(No)

    print(No,Ret)

if __name__ == "__main__":
    main()