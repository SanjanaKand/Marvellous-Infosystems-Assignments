'''
Write a program which contains filter(), map(), and reduce() in it. The Python application contains one list of numbers. 
The list contains the numbers accepted from the user.

Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90.
Map function should increase each value by 10.
Reduce will return the product of all those numbers.

Input List : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

List after filter : [76, 89, 86, 90, 70]

List after map : [86, 99, 96, 100, 80]

Output of reduce : 6538752000

'''
from functools import reduce

def FilterX(No):
    return No >= 70 and No <= 90
    

def MapX(No):
    return No + 10

def ReduceX(A,B):
    return A * B


def main():
    No = list(map(int , input("Enter N Numbers :").split(",")))
    print(No)

    filterData = list(filter(FilterX , No))
    print("List after Filter :",filterData)

    mapData = list(map(MapX , filterData))
    print("List after Map :",mapData)

    reduceData = reduce(ReduceX , mapData)
    print("Output of reduc :",reduceData)


if __name__ == "__main__":
    main()