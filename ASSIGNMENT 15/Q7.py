# Lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5

numbers = [1,2,3,5,6,7,8,34,56,67]
Num_Greater = list(filter(lambda x : x >5 , numbers))
print(Num_Greater)