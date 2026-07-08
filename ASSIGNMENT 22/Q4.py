'''
Write a program that calculates:

1^2+2^2+3^2+4^2+⋯+N^2
for multiple values of N simultaneously using Pool. Measure the total execution time.

'''

import multiprocessing
import time

def SumSquares(Number):
    Sum = 0
    for i in range(1, Number + 1):
        Sum = Sum + (i * i)
    return Sum

def main():
    Numbers = list(map(int, input("Enter N Numbers : ").split(",")))
    print("Input List :", Numbers)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquares, Numbers)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result :", Result)
    print(f"Execution Time : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()