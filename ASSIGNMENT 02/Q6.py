# Write a program that accepts two numbers from user and prints their :

print("Enter first number:")
num1 = float(input())
print("Enter second number:")
num2 = float(input())

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2



print("Addition :", addition)
print("Subtraction :", subtraction)
print("Multiplication :", multiplication) 

if (num2 != 0):
    division = num1 / num2
    print("Division :", division)
else:
    print("Division not possible (cannot divide by zero)")