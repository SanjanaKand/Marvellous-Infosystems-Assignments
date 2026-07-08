# Write a program that counts how many odd numbers exist between 1 and N.

import multiprocessing

def Odd(Number):
    Count = 0
    for i in range ( 1 , Number + 1):
        if i % 2 != 0:
            Count = Count + 1
    return Count

def main():
    Number = int(input("Enter a Number :"))

    pobj = multiprocessing.Pool()

    Result = pobj.apply(Odd , (Number,))

    print(Result)
    

if __name__ == "__main__":
    main()