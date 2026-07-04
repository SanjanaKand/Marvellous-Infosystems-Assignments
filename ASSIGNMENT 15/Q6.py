# Lambda function using reduce() which accepts a list of numbers and returns minimum number

from functools import reduce

numbers = [1,2,3,4,6,7,89]
Minimum = reduce(lambda x,y : min(x,y) , numbers)
print(Minimum)