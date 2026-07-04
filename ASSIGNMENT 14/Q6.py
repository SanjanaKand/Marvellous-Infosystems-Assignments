# Lambda function which accepts one number and returns True if number is odd otherwise False

Checker = lambda No : No % 3 == 0
No =  int(input("Enter a number :"))
Ret = Checker(No)
print(f"{No} is odd : {Ret}")
print(Checker(2))
print(Checker(15))
