# Lambda function using filter() which accepts a list of numbers and returns the count of even numbers

numbers = [2,4,6,8,10,3,5]
Count = list(filter(lambda x : x % 2 == 0 , numbers))
print(len(Count))