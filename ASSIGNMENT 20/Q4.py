'''
Design a Python application that creates three threads named Small, Capital, and Digits. : Done

All threads should accept a string as input.
The Small thread should count and display the number of lowercase characters.
The Capital thread should count and display the number of uppercase characters.
The Digits thread should count and display the number of numeric digits.

Each thread must also display:

Thread ID
Thread Name

'''
import threading
import os
import sys


def SmallLetters(String):
    print("Small Thread Name :",threading.current_thread().name)
    print("Small Thread ID :",threading.get_ident())
    Count = 0
    for ch in String:
        if ch.islower():
            Count = Count + 1
    print(f"Count of LowerCase Letters is :",Count)

def CapitalLetters(String):
    print("Capital Thread Name :",threading.current_thread().name)
    print("Capital Thread ID :",threading.get_ident())
    Count = 0
    for ch in String:
        if ch.isupper():
            Count = Count + 1
    print(f"Count of UppperCase Letters is :",Count)

def DigitsCounting(String):
    print("Digits Thread Name :",threading.current_thread().name)
    print("Digits Thread ID :",threading.get_ident())
    Count = 0
    for ch in String:
        if ch.isdigit():
            Count = Count + 1
    print(f"Count of Digits is :",Count)


def main():
    String = input("Enter a word containing lowercase, uppercase letters and digits in it :")

    Small = threading.Thread(target=SmallLetters , args=(String,))
    Capital = threading.Thread(target=CapitalLetters , args=(String,))
    Digits = threading.Thread(target=DigitsCounting, args=(String,))

    Small.start()
    Capital.start()
    Digits.start()




if __name__ == "__main__":
    main()