'''
3. Write a Python program to implement a class named Numbers with the following specifications:
The class should contain one instance variable:
Value
Define a constructor (__init__) that accepts a number from the user and initializes Value.
Implement the following instance methods:
ChkPrime() : returns True if the number is prime, otherwise returns False.
ChkPerfect() : returns True if the number is perfect, otherwise returns False.
Factors() : displays all factors of the number.
SumFactors() : returns the sum of all factors.
Create multiple objects and call all methods.

'''

'''
3. Write a Python program to implement a class named Numbers with the following specifications:

The class should contain one instance variable:
Value

Define a constructor (__init__) that accepts a number from the user and initializes Value.

Implement the following instance methods:

ChkPrime() : returns True if the number is prime, otherwise returns False.

ChkPerfect() : returns True if the number is perfect, otherwise returns False.

Factors() : displays all factors of the number.

SumFactors() : returns the sum of all factors.

Create multiple objects and call all methods.
'''

class Numbers:

    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

       
    def ChkPerfect(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        if Sum == self.Value:
            return True
        else:
            return False
    
    def Factors(self):
        print("Factors are : ", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

obj1 = Numbers(6)
print("First Number :", obj1.Value)
print("Prime :", obj1.ChkPrime())
print("Perfect :", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors :", obj1.SumFactors())

print("----------------------------------")


obj2 = Numbers(15)
print("Second Number :", obj2.Value)
print("Prime :", obj2.ChkPrime())
print("Perfect :", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors :", obj2.SumFactors())