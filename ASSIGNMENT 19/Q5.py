'''
Write a program which contains filter(), map(), and reduce() in it. The Python application contains one list of numbers. 
The list contains the numbers accepted from the user.

Filter should filter out all prime numbers.
Map function will multiply each number by 2.
Reduce will return the maximum number from those numbers.

(You can also use normal functions instead of lambda functions.)

Input List : [2, 70, 11, 10, 17, 23, 31, 77]
List after filter : [2, 11, 17, 23, 31]
List after map : [4, 22, 34, 46, 62]
Output of reduce : 62

'''
from functools import reduce

def IsPrime(No):
    if No <= 1 :
        return False
    for i in range(2 , No):
        if No % i == 0:
            return False
    return True


def FilterX(Numbers):
    if IsPrime(Numbers):
        return True

def MapX(Numbers):
    return  Numbers * 2

def ReduceX(A, B):
    return max(A, B)



def main():
    Numbers = list(map(int, input("Enter N Numbers :").split(",")))
    print(f"Input List : {Numbers}")

    filterData = list(filter(FilterX , Numbers))
    print(f"List after filter : {filterData}")

    mapData = list(map(MapX , filterData))
    print(f"List after map : {mapData}")

    reduceData = reduce(ReduceX, mapData)
    print("Output of reduce :", reduceData)





if __name__ == "__main__":
    main()

