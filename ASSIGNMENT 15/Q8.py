# Lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by 3 and 5

numbers = [1,2,3,4,5,6,7,8,9,10,15]
Div_Numbs = list(filter(lambda x : x % 3 == 0 and x % 5 == 0 , numbers))
print(Div_Numbs)