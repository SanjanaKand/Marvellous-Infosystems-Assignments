# Lambda function which accepts two numbers and returns multiplication

Multi = lambda No1 , No2 : No1 * No2
No1 = int(input("Enter first Number :"))
No2 = int(input("Enter second Number :"))
Ret = Multi(No1 ,No2)
print(f"Multiplication of {No1} and {No2} is : {Ret}")
print(Multi(2,2))
print(Multi(2.2,4.5))