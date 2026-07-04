# Lambda function which accepts two numbers and returns maximum number

Maximum = lambda No1 , No2 : max(No1 , No2)
No1 = int(input("Enter first Number :"))
No2 = int(input("Enter second Number :"))
Ret = Maximum(No1 , No2)
print(f"Maximum number between {No1} and {No2} is : {Ret}")