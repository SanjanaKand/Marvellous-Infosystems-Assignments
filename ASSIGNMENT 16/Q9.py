'''
Write a program which displays the first 10 even numbers on the screen.

Output:

2 4 6 8 10 12 14 16 18 20


'''

def Even():
    for i in range(2,21,2):
        print(i, end=" ")

def main():
    Even()

if __name__ == "__main__":
    main()