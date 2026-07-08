'''
Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

'''

import multiprocessing

def Squares(Numbers):
    Sum = 0
    for i in range ( 1 , Numbers + 1):
        Sum = Sum + (i * i)
    return Sum

def main():
    Numbers = list(map(int,input("Enter N Numbers :").split(",")))

    pobj = multiprocessing.Pool()

    Result = pobj.map(Squares , Numbers)

    pobj.close()
    pobj.join()

    print(Result)

if __name__ == "__main__":
    main()