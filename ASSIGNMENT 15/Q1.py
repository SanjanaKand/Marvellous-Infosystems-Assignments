# Lambda function using map() which accepts a list of numbers and returns a list of squares of each numbers

# map() applies a function to every element of an iterable and returns a map object (which can be converted to a list, tuple, etc.).

numbers = [1,2,3,4]
Square = list(map(lambda x : x*x,numbers))
print(Square)