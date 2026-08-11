import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousWinePredictor(DataPath):
    Border = "-" * 50

    ###################################################
    # Step 1 : Load the dataset
    ###################################################

    print(Border)
    print("Step 1 : Load the dataset...")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully...")
    print(Border)

    print("Some entries from the dataset are :")
    print(df.head())

    #####################################################
    # Step 2 : Clean , Prepare and Manipulate Data
    #####################################################

    df.dropna(inplace=True)

    print(Border)
    print("Step 2 : Clean , Prepare and Manipulate Data")
    print(Border)

    print("Shape of dataset :", df.shape)
    print("Total records :", df.shape[0])
    print("Total columns :", df.shape[1])
    print("Total columns in the dataset :", df.columns.tolist())

    print(Border)
    print("Info of the dataset :")
    df.info()

    print(Border)
    print("DataTypes :")
    print(df.dtypes)

    print(Border)
    print("Information of numerical columns :")
    print(df.describe())

    print(Border)
    print("Missing values :")
    print(df.isnull().sum())

    print(Border)
    print("Duplicate Records :", df.duplicated().sum())

    ###########################################################
    # Step 3 : Separate Independent and Dependent Variables
    ###########################################################

    print(Border)
    print("Step 3 : Separate Independent and Dependent Variables")
    print(Border)

    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print(Border)
    print("Input variables :", X.columns.tolist())
    print("Output variable : Class")

    #########################################################
    # Step 4 : Split the dataset for training and testing
    #########################################################

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Details of training and testing data")
    print(Border)

    print("Shape of X_train :", X_train.shape)
    print("Shape of X_test :", X_test.shape)
    print("Shape of Y_train :", Y_train.shape)
    print("Shape of Y_test :", Y_test.shape)

    #########################################################
    # Step 5 : Feature Scaling
    #########################################################

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature Scaling done...")

    #########################################################
    # Step 6 : HyperParameter Tuning
    #########################################################

    print(Border)
    print("Step 6 : HyperParameter Tuning...")
    print(Border)

    accuracy_scoresList = []
    k_values = range(1, 21, 2)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scoresList.append(accuracy)

    print("Accuracy Report :")

    for k, accuracy in zip(k_values, accuracy_scoresList):
        print(f"K = {k} --> Accuracy = {accuracy * 100:.2f}%")

    BestAccuracy = max(accuracy_scoresList)
    BestK = k_values[accuracy_scoresList.index(BestAccuracy)]

    print(Border)
    print(f"Best K Value : {BestK}")
    print(f"Best Accuracy : {BestAccuracy * 100:.2f}%")

    #########################################################
    # Train Final Model
    #########################################################

    model = KNeighborsClassifier(n_neighbors=BestK)
    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    print(Border)
    print("Confusion Matrix :")
    CM = confusion_matrix(Y_test, Y_pred)
    print(CM)

    FinalAccuracy = accuracy_score(Y_test, Y_pred)

    print(Border)
    print(f"Final Accuracy : {FinalAccuracy * 100:.2f}%")
    print(Border)


def main():
    MarvellousWinePredictor("WinePredictor.csv")


if __name__ == "__main__":
    main()