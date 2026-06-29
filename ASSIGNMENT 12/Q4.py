# Write a program which accepts one number and prints that many numbers starting from 1 
# INPUT : 5
# OUTPUT : 1 2 3 4 5

def Numbers(No):
    for i in range(1,No + 1):
        print(i)
     
def main():
    No = int(input("Enter a number :"))
    Numbers(No)
   
if __name__ == "__main__":
    main()