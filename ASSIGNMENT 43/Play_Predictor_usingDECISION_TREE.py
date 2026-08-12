import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

def Play_Predictor_using_DecisionTree(DataPath):
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

    print(Border)

    print("Some entries from the dataset are :\n")
    print()
    print(df.head())

    print(Border)

    ###############################################################
    ## Step 2 : Clean , Prepare and Manipulate Data
    ###############################################################

    print("Any missing values in the dataset :",df.isnull().sum())
    print("\n")
    print(Border)

    print("Overall information of the dataset :")
    df.info()
    print("\n")
    print(Border)

    print("Summary of the entire dataset :")
    print(df.describe())
    print("\n")  
    print(Border)  

    print(df["Play"].value_counts())
    print(Border)

    print(df["Wether"].unique())
    print(df["Temperature"].unique())
    print(df["Play"].unique())
    print(Border)

    print("Null Values :",df.isnull().sum())


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
    print("Step 5 : Split the dataset for training and training...")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,random_state=42,test_size=0.2,stratify=Y)

    print("Details of training and testing data :")
    print("X_train :",X_train.shape)
    print("X_test :",X_test.shape)
    print("Y_train :",Y_train.shape)
    print("Y_test :",Y_test.shape)

    #########################################################
    # Train Final Model
    #########################################################


    print(Border)
    print("Step 6 : Train the model...")
    print(Border)

    model = DecisionTreeClassifier(random_state=42)
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,Y_pred)
    cm = confusion_matrix(Y_test,Y_pred)

    print("Confusion Matrix : \n")
    print(cm)

    print(f"Accuracy score obtained : {accuracy * 100:.2f}")

    print(Border)

def main():
    Play_Predictor_using_DecisionTree("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()