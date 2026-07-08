'''
Design a Python application that creates two threads.

Thread 1 should compute the sum of elements from a list.
Thread 2 should compute the product of elements from the same list.
Return the results to the main thread and display them.

'''
import threading

Result = [0,0]

def Summation(Numbers):
    Sum = 0
    for i in Numbers:
        Sum = Sum + i
    Result[0] = Sum

def Multiplication(Numbers):
    Multi = 1
    for i in Numbers:
        Multi = Multi * i
    Result[1] = Multi

def main():
    Numbers = [1,2,3,4]

    Thread1 = threading.Thread(target=Summation , args=(Numbers ,))
    Thread2 = threading.Thread(target=Multiplication , args=(Numbers ,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()


    print(f"Sum of Elements is :",Result[0])
    print(f"Multiplication of Elements is :",Result[1])

if __name__ == "__main__":
    main()