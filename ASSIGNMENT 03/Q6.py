# Display data type, memory address and size in bytes of variable entered by user :

import sys

def main():
    number = int(input("Enter a number: "))

    print("Value :", number)
    print("Data Type :", type(number))
    print("Memory Address :", id(number))
    print("Size in Bytes :", sys.getsizeof(number))

if __name__ == "__main__":
    main()

