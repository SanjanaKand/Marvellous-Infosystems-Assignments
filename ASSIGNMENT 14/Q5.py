# Lambda function which accepts one no and returns True if no is even otherwise False

Checker = lambda No : No % 2 == 0
No =  int(input("Enter a number :"))
Ret = Checker(No)
print(f"{No} is even : {Ret}")
#print(Checker(2))
#print(Checker(15))
