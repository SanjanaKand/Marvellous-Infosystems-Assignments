# Write a program which accepts marks and displays grade 
'''
>= 75 Distinction
>= 60 First Class
>= 50 Second Class
< 50  Fail

'''
def Grade(marks):
    if (marks >= 75):
        print("CONGRATULATIONS , You have passed with Distinction")
    elif (marks >= 60):
        print("CONGRATULATIONS , You have passed with First Class")
    elif (marks >= 50):
        print("CONGRATULATIONS , You have passed with Second Class")
    else:
        print("Sorry, You have Failed")

def main():
    marks = int(input("Enter Student's Marks :"))

    Ret = Grade(marks)

if __name__ =="__main__":
    main()