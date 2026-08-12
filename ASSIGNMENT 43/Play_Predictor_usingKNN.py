import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def Play_Predictor_Model(DataPath):
    Border = "-"*60

    ##############################################################
    ## Step 1 : Load the dataset
    ##############################################################

    print(Border)
    print("Step 1 : Load the dataset...")
    print(Border)

    df = pd.read_csv(DataPath)

    df.drop(columns=["Unnamed: 0"], inplace=True)

    print("Dataset loaded successfully...")
    print("Some entries from the dataset are :")
    print(df.head())
    print(Border)

    ###############################################################
    ## Step 2 : Clean , Prepare and Manipulate Data
    ###############################################################

    # Checking for NULL values :
    print("Null values in the datatset :")
    print(df.isnull().sum())

    print(Border)
    # info() :
    print("Information about the dataset :")
    df.info()

    print(Border)
    # describe()
    print("Entire statistics of the dataset :")
    print(df.describe())

    ###################################################################
    ## Step 3 : Convert Categorical values into numerical values
    ###################################################################

    print(Border)
    print("Step 3 : Convert Categorical Data into Numerical Data")
    print(Border)

    print("Following Numerical values represent :\n")
    
    print("Weather Column --> Sunny : 0 , Overcast : 1 , Rainy : 2 ")
    
    print("Temperature Columm --> Hot : 0 , Mild : 1 , Cool : 2")

    print("Play Column --> Yes : 1 , No : 0 ")


    df["Wether"] = df["Wether"].map({
        "Sunny" : 0 ,
        "Overcast" : 1 ,
        "Rainy" : 2
    })

    df["Temperature"] = df["Temperature"].map({
        "Hot" : 0 ,
        "Mild" : 1 ,
        "Cool" : 2
    })

    df["Play"] = df["Play"].map({
        "Yes" : 1,
        "No" : 0
    })

    print(Border)
    print(df.head())
    print(Border)

    print("Mathematical statistics of the dataset after converting categorical variables into numerical values :")
    print(df.describe())

    #################################################################
    ##  Step 4 : Separate Independant & Dependant Variables
    #################################################################

    print(Border)
    print("Step 3 : Separate Independent and Dependent Variables")
    print(Border)

    X = df.drop(columns=["Play"])       # Independant
    Y = df["Play"]                      # Dependant

    print("X Shape :",X.shape)
    print("Y Shape :",Y.shape)

    print(Border)
    print("Input variables :",X.columns.tolist())
    print("Ouput variable : Play")
    print(Border)

    #########################################################
    # Step 5 : Split the dataset for training and testing
    #########################################################

    print(Border)
    print("Step 4 : Split the dataset for training and training...")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("Details of training and testing data :")
    print("X_train :",X_train.shape)
    print("X_test :",X_test.shape)
    print("Y_train :",Y_train.shape)
    print("Y_test :",Y_test.shape)

    #########################################################
    # Step 6 : HyperParameter Tuning
    #########################################################

    print(Border)
    print("Step 6 : HyperParamter Tuning...")
    print(Border)

    accuracy_scores_List = []
    K_values = range(1,23,2)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train , Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_pred , Y_test)
        accuracy_scores_List.append(accuracy)

    print("Accuracy Report :")
    for k,accuracy in zip(K_values,accuracy_scores_List):
        print(f"K --> {k} = Accuracy --> {accuracy * 100:.2f}%")

    Best_Accuracy = max(accuracy_scores_List)
    Best_K = K_values[accuracy_scores_List.index(Best_Accuracy)]

    print(Border)
    print(f"Best K Value : {Best_K}")
    print(f"Best Accuracy : {Best_Accuracy * 100:.2f}%")

    #########################################################
    # Train Final Model
    #########################################################

    print(Border)
    print("Step 7 : Train the model with Best_K Value...")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=Best_K)
    model = model.fit(X_train , Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_pred,Y_test)
    cm = confusion_matrix(Y_test, Y_pred)

    print("Final Confusion Matrix :")
    print(cm)
    print(Border)

    print(f"Final Accuracy with Best K value {Best_K} is : {accuracy * 100:.2f}%")

    print(Border)

    print("Model trained successfully !!!")


def main():
    Play_Predictor_Model("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()