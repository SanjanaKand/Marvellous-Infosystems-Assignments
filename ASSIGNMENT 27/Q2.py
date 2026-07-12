'''
2. Write a Python program to implement a class named BankAccount with the following requirements:
The class should contain two instance variables:
Name (Account holder name)
Amount (Account balance)
The class should contain one class variable:
ROI (Rate of Interest), initialized to 10.5
Define a constructor (__init__) that accepts Name and initial Amount.
Implement the following instance methods:
Display() : displays account holder name and current balance.
Deposit() : accepts an amount from the user and adds it to the balance.
Withdraw() : accepts an amount from the user and subtracts it from the balance.
(Ensure withdrawal is allowed only if sufficient balance exists.)
CalculateInterest() : calculates and returns interest using the formula:
Interest = (Amount * ROI) / 100
Create multiple objects and demonstrate all methods.

'''
class BankAccount:

    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self):
        deposit = float(input("Enter deposit amount : "))
        self.Amount += deposit
        print("Updated Balance :", self.Amount)

    def Withdraw(self):
        withdraw = float(input("Enter withdrawal amount : "))

        if withdraw <= self.Amount:
            self.Amount -= withdraw
            print("Updated Balance :", self.Amount)
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest :", Interest)



dobj1 = BankAccount("Sanjana", 10000)

print("First Account")
dobj1.Display()
dobj1.Deposit()
dobj1.Withdraw()
dobj1.CalculateInterest()

print("--------------------------------")


dobj2 = BankAccount("Rahul", 5000)

print("Second Account")
dobj2.Display()
dobj2.Deposit()
dobj2.Withdraw()
dobj2.CalculateInterest()