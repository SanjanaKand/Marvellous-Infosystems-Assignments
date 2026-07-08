'''
Write a program which contains one lambda function which accepts two parameters and returns their multiplication.

Input:

4 3

Output:

12

Input:

6 3

Output:

18

'''

Number1 = int(input("Enter first Number :"))
Number2 = int(input("Enter second Number :"))

Multi = lambda Number1 , Number2 : Number1 * Number2
Ret = Multi(Number1 , Number2)

print(f"Multiplication of {Number1} and {Number2} is :",Ret)