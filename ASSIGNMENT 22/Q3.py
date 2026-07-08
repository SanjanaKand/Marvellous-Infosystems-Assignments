'''
For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool. 
Display the total prime count for each number.

'''

import multiprocessing

def IsPrime(No):
    if No <= 1:
        return False
    
    for i in range ( 2, No):
        if No % i == 0:
            return False
    return True

def Prime(Numbers):
    Count = 0
    for i in range (1,Numbers +1):
        if IsPrime(i):
             
             Count = Count + 1
    return Count
        
def main():
    Numbers = list(map(int ,input("Enter N Numbers :").split(",")))
    print(f"Input List is : {Numbers}")

    pobj = multiprocessing.Pool()

    Result = pobj.map(Prime , Numbers)

    pobj.close()
    pobj.join()

    print("Result is :",Result)

if __name__ == "__main__":
    main()
