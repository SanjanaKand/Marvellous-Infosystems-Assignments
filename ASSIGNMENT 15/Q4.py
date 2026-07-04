# Lambda function using reduce() which accepts a list of numbers and returns addition of all elements
'''
reduce() repeatedly combines the elements of an iterable into one single value.

Unlike map() and filter(), it is not built into Python. You must import it from the functools module.

from functools import reduce
The function passed to reduce() takes two arguments.

'''
from functools import reduce

numbers = [1,2,3,4]
Add = reduce(lambda x,y : x+y , numbers)
print(Add)