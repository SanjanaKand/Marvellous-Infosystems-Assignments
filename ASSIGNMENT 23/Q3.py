# Write a program that counts how many even numbers exist between 1 and N using Pool.map()

import multiprocessing

def Even(Numbers):
    Count = 0
    for i in range(1,Numbers + 1):
        if i % 2 == 0:
            Count = Count + 1
    return Count

def main():
    Numbers = list(map(int, input("Enter N Numbers : ").split(",")))
   
    pobj = multiprocessing.Pool()

    Result = pobj.map(Even , Numbers)

    pobj.close()
    pobj.join()

    print(f"Result is : {Result}")

if __name__ == "__main__":
    main()
