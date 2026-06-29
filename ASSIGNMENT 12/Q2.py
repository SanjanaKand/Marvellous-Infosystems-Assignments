# Write a program which accepts one number and prints its factors
# INPUT : 12
# OUTPUT : 1 2 3 4 6 12

def Factors(No):
    for i in range(1,No+1):
        if No % i == 0:
          print(i)
         
def main():
    No = int(input("Enter a number :"))

    Ret = Factors(No)

if __name__ == "__main__":
    main()

