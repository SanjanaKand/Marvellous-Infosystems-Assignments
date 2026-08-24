"""
================================================================================
           
         MACHINE LEARNING ASSIGNMENT : BREAST CANCER DETECTION         
================================================================================
--------------------------------------------------------------------------------
Script Name  : decision_tree_breast_cancer.py
Task         : Breast Cancer Prediction using Decision Tree Classifier
Dataset      : breast_cancer.csv
Author       : Student Assignment
--------------------------------------------------------------------------------
================================================================================
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ==============================================================================
# SECTION 1: DATA LOADING & EXPLORATION
# ==============================================================================
def load_data(filepath="breast_cancer.csv"):
    print("-" * 80)
    print("STEP 1: Loading Dataset")
    print("-" * 80)
    
    df = pd.read_csv(filepath)
    print(f"Shape of dataset : {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nFirst 5 records from the dataset:")
    print(df.head())
    print("-" * 80)
    return df


# ==============================================================================
# SECTION 2: FEATURE EXTRACTION & DATA SPLITTING
# ==============================================================================
def prepare_data(df):
    print("-" * 80)
    print("STEP 2: Separating Features and Labels")
    print("-" * 80)
    
    X = df.drop("target", axis=1)  # Features
    Y = df["target"]               # Labels
    
    print(f"X Shape : {X.shape}")
    print(f"Y Shape : {Y.shape}")

    print("-" * 80)
    print("\nSTEP 3: Splitting Dataset (80% Train, 20% Test)")
    print("-" * 80)
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    print("-" * 80)
    print("STEP 4: Feature Scaling")
    print("-" * 80)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)  # FIXED: transform() instead of fit_transform()
    
    print("Feature scaling successfully applied.\n")
    return X_train, X_test, Y_train, Y_test


# ==============================================================================
# SECTION 3: MODEL TRAINING & EVALUATION
# ==============================================================================
def train_and_evaluate(X_train, X_test, Y_train, Y_test):
    print("-" * 80)
    print("STEP 5 & 6: Building and Training Decision Tree Model")
    print("-" * 80)
    
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, Y_train)
    print("Model training completed.")

    print("-" * 80)
    print("\nSTEP 7 & 8: Predicting and Evaluating Model Performance")
    print("-" * 80)
    
    Y_pred = model.predict(X_test)
    
    acc = accuracy_score(Y_test, Y_pred)
    cm = confusion_matrix(Y_test, Y_pred)
    cr = classification_report(Y_test, Y_pred, target_names=['Malignant (0)', 'Benign (1)'])
    
    print(f"Accuracy Score: {acc * 100:.2f}%\n")
    
    print("Confusion Matrix:")
    cm_df = pd.DataFrame(
        cm, 
        index=['Actual: Malignant', 'Actual: Benign'], 
        columns=['Pred: Malignant', 'Pred: Benign']
    )
    print(cm_df)
    
    print("\nClassification Report:")
    print(cr)
    print("-" * 80)


# ==============================================================================
# MAIN EXECUTION PIPELINE
# ==============================================================================
def main():
    print("#" * 80)
    print("        BREAST CANCER PREDICTION USING DECISION TREE CLASSIFIER        ")
    print("#" * 80)
    
    df = load_data("breast_cancer.csv")
    X_train, X_test, Y_train, Y_test = prepare_data(df)
    train_and_evaluate(X_train, X_test, Y_train, Y_test)
    
    print("#" * 80)
    print("                    EXECUTION COMPLETED SUCCESSFULLY                  ")
    print("#" * 80)


if __name__ == "__main__":
    main()