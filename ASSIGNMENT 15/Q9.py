# Lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce

numbers = [1,2,3]
Product = reduce(lambda x,y : x*y , numbers)
print(Product)