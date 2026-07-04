# Lambda function using reduce() which accepts a list of numbers and returns maximum number

from functools import reduce
numbers = [1,2,3,4,6,7,89]
Maximum = reduce(lambda x,y : max(x,y) , numbers)
print(Maximum)