# Write a program that calculates factorials of multiple numbers simultaneously using Pool.map()


import multiprocessing

def Factorials(Numbers):
    Fact = 1
    for i in range(1,Numbers+1):
        Fact = Fact * i
    return Fact

def main():
    Numbers = list(map(int ,input("Enter N Numbers :").split(",")))
    print(f"Input List is : {Numbers}")

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorials , Numbers)

    pobj.close()
    pobj.join()

    print(f"Result is : {Result}")

if __name__ == "__main__":
    main()