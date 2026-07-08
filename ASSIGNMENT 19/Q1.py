'''
Write a program which contains one lambda function which accepts one parameter and returns the power of two.

Input:

4

Output:

16

Input:

6

Output:

64

# Power of 2 : 2 ** x

'''
Number = int(input("Enter a Number :"))
Power = lambda Number : 2 ** Number
print(Power(Number))

