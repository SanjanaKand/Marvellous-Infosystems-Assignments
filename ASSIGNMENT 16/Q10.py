''' Write a program which accepts a name from the user and displays the length of the name.

Input: Marvellous

Output: 10
'''
def Length(Name):
    print(len(Name))


def main():
    Name = input("Enter a Name to check it's length :")
    Length(Name)

if __name__ == "__main__":
    main()