import math



def EuclideanValueCalculation(P1,P2):
    Ans = math.sqrt((P1["X"] - P2["X"])** 2 + (P1["Y"] - P2["Y"])** 2)
    return Ans

def KNNClassifier(K=3):
    Border = "-"*60

    Dataset_Values = [
        {"Point":"A","X":1,"Y":2,"Label":"Red"},
        {"Point":"B","X":2,"Y":3,"Label":"Red"},
        {"Point":"C","X":3,"Y":1,"Label":"Blue"},
        {"Point":"D","X":6,"Y":5,"Label":"Blue"},
    ]
    
    print(Border)
    print("Dataset contains the following contents :\n")
    print(Border)

    for i in Dataset_Values:
        print(i)

    print(Border)
    print("New points for prediction :\n")
    print(Border)
    new_point = {
        "X" : int(input("Enter X coordinate:")) ,
        "Y" : int(input("Enter Y coordinate :"))
    }

    print(Border)
    print("Distance of all values :")
    print(Border)

    for d in Dataset_Values:
        d["Distance"] = EuclideanValueCalculation(d,new_point)

    for d in Dataset_Values:
        print(d)

    print(Border)
    print("Nearest Neighbours :")
    print(Border)

    sorted_data = sorted(Dataset_Values,key= lambda item : item["Distance"])
    print(Border)
    print("Sorted data :")
    print(Border)

    for d in sorted_data:
        print(d)
    print(Border)

    nearest = sorted_data[:K]

    print(Border)
    print("Nearest 3 neighnours are :")
    print(Border)
    
    for d in nearest:
        print(d)

    print(Border)

    # Voting
    votes = {}

    for neighbours in nearest:
        label = neighbours["Label"]
        votes[label] = votes.get(label ,0) + 1

    print(Border)
    print("Voting result is :")
    print(Border)

    for d in votes :
        print("Name : ",d,"Number of votes :",votes[d])

    print(Border)

    iMax = 0
    Name = ""
    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d
    print("Final prediction is :", Name)

def main():
    KNNClassifier()  

if __name__ == "__main__":
    main()