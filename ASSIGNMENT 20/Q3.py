'''
Design a Python application that creates two threads named EvenList and OddList.

Both threads should accept a list of integers as input.
The EvenList thread should:
Extract all even elements from the list.
Calculate and display their sum.
The OddList thread should:
Extract all odd elements from the list.
Calculate and display their sum.
Threads should run concurrently.

'''
import threading


def EvenList(Numbers):
    Sum = 0
    for i in Numbers:
        if i % 2 == 0:
            Sum = Sum + i
            print(i , end=" ")
    print()
    print(f"Sum of Even Numbers is :",Sum)


def OddList(Numbers):
    Sum = 0
    for i in Numbers:
        if i % 2 != 0:
            Sum = Sum + i
            print(i , end=" ")
    print()
    print(f"Sum of Odd Numbers is :",Sum)


def main():
    Numbers = list(map(int , input("Enter a list of numbers :").split(",")))
    print(Numbers)

    Thread1 = threading.Thread(target=EvenList , args=(Numbers,))
    Thread2 = threading.Thread(target=OddList , args=(Numbers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()


if __name__ == "__main__":
    main()