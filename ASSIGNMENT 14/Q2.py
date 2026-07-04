# Lambda function which accepts one no and returns cube of that number

Cube = lambda x : x * x * x
No1 = int(input("Enter a Number :"))
Ret = Cube(No1)
print(f"Cube of {No1} is : {Ret}")