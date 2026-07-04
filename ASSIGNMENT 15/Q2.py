# Lambda function using filter() which accepts a list of numbers and returns a list of even numbers
'''
filter() selects only those elements that satisfy a condition.

If the condition returns:

True → Keep the element.
False → Remove the element.

'''
numbers = [1,2,3,4,5,6,7,8,9,10]
Even = list(filter(lambda x : x % 2 == 0 , numbers))
print(Even)