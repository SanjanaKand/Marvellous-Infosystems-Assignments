import math

def EuclideanValueCalculation(P1, P2):
    Ans = math.sqrt((P1["X"] - P2["X"])**2 + (P1["Y"] - P2["Y"])**2)
    return Ans

def main():

    Border = "-" * 60

    Dataset_Values = [
        {"point" : "A" , "X" : 1 , "Y" : 2 , "Label" : "Red"},
        {"point" : "B" , "X" : 2 , "Y" : 3 , "Label" : "Red"},
        {"point" : "C" , "X" : 3 , "Y" : 1 , "Label" : "Blue"},
        {"point" : "D" , "X" : 5 , "Y" : 6 , "Label" : "Blue"},
        {"point" : "E" , "X" : 6 , "Y" : 6 , "Label" : "Blue"},
        {"point" : "F" , "X" : 3 , "Y" : 4 , "Label" : "Red"},
        {"point" : "G" , "X" : 3 , "Y" : 2 , "Label" : "Red"}
        ]

    print(Border)
    print("Dataset")
    print(Border)

    for d in Dataset_Values:
        print(d)

    new_point = {
        "X": int(input("\nEnter X Coordinate : ")),
        "Y": int(input("Enter Y Coordinate : "))
    }

    # Calculate distance only once
    for d in Dataset_Values:
        d["Distance"] = EuclideanValueCalculation(d, new_point)

    sorted_data = sorted(Dataset_Values, key=lambda item: item["Distance"])

    print(Border)
    print("Sorted Data")
    print(Border)

    for d in sorted_data:
        print(d)

    # Loop for K = 1 , K = 2 & K = 3
    for K in range(1, 6, 2):

        print(Border)
        print("Prediction for K =", K)
        print(Border)

        nearest = sorted_data[:K]

        print("Nearest Neighbours :")
        for d in nearest:
            print(d)

        votes = {}

        for neighbour in nearest:
            label = neighbour["Label"]
            votes[label] = votes.get(label, 0) + 1

        print("\nVoting Result :")
        for key, value in votes.items():
            print(key, ":", value)

        prediction = max(votes, key=votes.get)

        print("\nPredicted Class :", prediction)
        print(Border)

    print("The prediction changes when the value of K changes because K determines how many nearest neighbors are considered during classification.\n" 
    " With a small K (such as K = 1), the prediction depends only on the closest data point, making it sensitive to noise or outliers.\n" 
    " As K increases (such as K = 3 or K = 5), more neighboring points participate in voting, so the prediction is based on the majority class. \n" 
    "This makes the classifier more stable and less affected by a single point. Therefore, changing K can change the majority vote and result in a different predicted class.")

if __name__ == "__main__":
    main()