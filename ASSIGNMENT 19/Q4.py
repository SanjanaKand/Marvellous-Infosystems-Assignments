'''
Write a program which contains filter(), map(), and reduce() in it. The Python application contains one list of numbers. The list contains the numbers accepted from the user.

Filter should filter out all even numbers.
Map function will calculate the square of each number.
Reduce will return the addition of all those numbers.

Input List : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

List after filter : [2, 4, 4, 2, 8, 10]

List after map : [4, 16, 16, 4, 64, 100]

Output of reduce : 204

'''
from functools import reduce

def FilterX(Numbers):
    return Numbers % 2 == 0
    

def MapX(Numbers):
    return Numbers ** 2
    
def ReduceX(A,B):
    return A + B

def main():
    Numbers = list(map(int , input ("Enter N Numbers :").split(",")))
    print(f"Input List : {Numbers}")

    filterData = list(filter(FilterX , Numbers))
    print(f"List after filter : {filterData}")

    mapData = list(map(MapX , filterData))
    print(f"List after map : {mapData}")

    reduceData = reduce(ReduceX,mapData)
    print(f"Output of reduce : {reduceData}")

if __name__ == "__main__":
    main()