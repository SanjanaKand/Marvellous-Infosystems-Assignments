# Lambda function which accepts two numbers and returns minimum number

Minimum = lambda No1 , No2 : min(No1 , No2)
No1 = int(input("Enter first Number :"))
No2 = int(input("Enter second Number :"))
Ret = Minimum(No1 , No2)
print(f"Minimum number between {No1} and {No2} is : {Ret}")