'''
3. Write a Python program to implement a class named Arithmetic with the following characteristics:
The class should contain two instance variables:
Value1
Value2
Define a constructor (__init__) that initializes all instance variables to 0.
Implement the following instance methods:
Accept() : accepts values for Value1 and Value2 from the user.
Addition() : returns the addition of Value1 and Value2.
Subtraction() : returns the subtraction of Value1 and Value2.
Multiplication() : returns the multiplication of Value1 and Value2.
Division() : returns the division of Value1 and Value2 (handle division by zero properly).
Create multiple objects of the Arithmetic class and invoke all the instance methods.

'''
class Arithmetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value1 = 0

    def Accept(self):
        self.Value1 = float(input("Enter first number :"))
        self.Value2 = float(input("Enter second number :"))

    def Addition(self):
        Add = self.Value1 + self.Value2
        print(f"Addition is : {Add}")

    def Subtraction(self):
        Sub = self.Value1 - self.Value2
        print(f"Subtraction is :{Sub}")

    def Multiplication(self):
        Mul = self.Value1 * self.Value2
        print(f"Multiplication is : {Mul}")

    def Division(self):
        try:
            Div = self.Value1 / self.Value2
            print(f"Division is : {Div}")
        except ZeroDivisionError as zobj:
            print("Division by zero is not possible ",zobj)
        
cobj1 = Arithmetic()
cobj2 = Arithmetic()

print("First Solving :")
cobj1.Accept()
cobj1.Addition()
cobj1.Subtraction()
cobj1.Multiplication()
cobj1.Division()

print("----------------------")

print("Second Solving :")
cobj2.Accept()
cobj2.Addition()
cobj2.Subtraction()
cobj2.Multiplication()
cobj2.Division()
          