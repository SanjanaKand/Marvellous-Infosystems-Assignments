# Lambda function which accepts one no and returns square of that number

# function_name = lambda arguments : expression

Square = lambda x : x * x
No1 = int(input("Enter a Number :"))
Ret = Square(No1)
print(f"Square of {No1} is : {Ret}")