# Write a program which accepts radius of circle and prints area of circle

def Area(radius):
    return 3.14 * radius * radius


def main():
    radius = float(input("Enter Radius of Circle :"))

    Ret = Area(radius)

    print("Area of Circle with Radius",radius,"is :", Ret)


if __name__ == "__main__":
    main()