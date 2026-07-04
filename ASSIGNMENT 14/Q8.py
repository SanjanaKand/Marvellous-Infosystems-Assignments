# Lambda function which accepts two numbers and returns addition

Add = lambda No1 , No2 : No1 + No2
No1 = int(input("Enter first Number :"))
No2 = int(input("Enter second Number :"))
Ret = Add(No1 ,No2)
print(f"Addition of {No1} and  {No2} is : {Ret}")
print(Add(2,2))
print(Add(2.2,4.5))