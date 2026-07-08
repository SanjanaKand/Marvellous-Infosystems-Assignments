'''
Design a Python application that creates two threads named EvenFactor and OddFactor.

Both threads should accept one integer number as a parameter.
The EvenFactor thread should:
Identify all even factors of the given number.
Calculate and display the sum of even factors.
The OddFactor thread should:
Identify all odd factors of the given number.
Calculate and display the sum of odd factors.
After both threads complete execution, the main thread should display the message:
Exit from main


'''
import threading

def EvenFactor(Number):
    print("--------------------------------")

    Sum = 0
    for i in range (1 , Number + 1):
        if (Number % i == 0 and i % 2 == 0):
            Sum = Sum + i
            print(i, end=" ")
    print(f"Sum of Even Factors :",Sum)

def OddFactor(Number):
    print("--------------------------------")

    Sum = 0
    for i in range (1 , Number + 1):
        if (Number % i == 0 and i % 2 != 0):
            Sum = Sum + i
            print(i  , end=" ")
    print(f"Sum of Odd Factors :",Sum)


def main():
    Number = int(input("Enter a Number :"))

    EvenNumbers = threading.Thread(target=EvenFactor , args=(Number,))
    OddNumbers = threading.Thread(target=OddFactor , args=(Number,))

    EvenNumbers.start()
    OddNumbers.start()

    EvenNumbers.join()
    OddNumbers.join()

    print("Exit from Main")

if __name__ == "__main__":
    main()