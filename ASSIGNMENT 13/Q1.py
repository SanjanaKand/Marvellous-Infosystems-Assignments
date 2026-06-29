# Write a program which accepts length and width of rectangle and prints area

def Area(length , width):
    Ans = length * width
    return Ans

def main():
    length = int(input("Enter LENGTH of Rectangle :"))
    width = int(input("Enter WIDTH of Rectangle :"))

    Ret = Area(length , width)

    print("Area of Rectangle with length",length,"and width",width,"is :",Ret)

if __name__ == "__main__":
    main()