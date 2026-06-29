# Write a program which accepts one number and prints all even numbers till that number
# INPUT : 10
# OUTPUT : 2 4 6 8 10

def EvenNumbers(No1):
    for i in range (1, No1 + 1):
        if ( i % 2 == 0):
            print(i)
         
def main():
    No1 = int(input("Enter a Number :"))
    EvenNumbers(No1)

if __name__ == "__main__":
    main()