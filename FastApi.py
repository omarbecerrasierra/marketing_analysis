import pickle
import numpy as np
import pandas as pd
import uvicorn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

def data_preprocessing(X, y, test_size=0.2):
    # Apply the normal train_test_split to the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    # making oversampling
    ros = RandomOverSampler(random_state=42)
    X_train, y_train = ros.fit_resample(X_train , y_train)
    return (X_train, X_test, y_train, y_test)

def train(X,y):

    X_train, X_test, y_train, y_test = data_preprocessing(X, y, test_size=0.15)

    fr = RandomForestClassifier(n_estimators= 800, max_depth = 5 , random_state=42)

    # fit the model
    fr.fit(X_train, y_train)
    preds = fr.predict(X_test)

    # Show clasification report
    print(classification_report(y_test, preds))

    return fr

# Rest API

app = FastAPI()

class Answer(BaseModel):
    Income : int 
    Kidhome : int 
    Teenhome : int 
    Recency : int 
    MntWines : int 
    MntFruits : int 
    MntMeatProducts : int 
    MntFishProducts : int 
    MntSweetProducts : int 
    MntGoldProds : int 
    NumDealsPurchases : int 
    NumWebPurchases : int 
    NumCatalogPurchases : int 
    NumStorePurchases : int 
    NumWebVisitsMonth : int 
    AcceptedCmp3 : int 
    AcceptedCmp4 : int 
    AcceptedCmp5 : int 
    AcceptedCmp1 : int 
    AcceptedCmp2 : int 
    Complain : int 
    Age : int 
    Customer_Days : int 
    Second_Cycle : int 
    Basic : int 
    Graduation : int 
    Master : int 
    PhD : int 
    Divorced : int 
    Married : int 
    Single : int 
    Together : int 
    Widow : int 
    MntTotal : int 
    MntRegularProds : int 
    AcceptedCmpOverall : int 


@app.get("/")
async def root():
    return {"message": """ Welcome to the Customer Campain API """}

@app.post("/predict")
async def predict_campain(answer: Answer):
    answer_dict = jsonable_encoder(answer)
    for key, value in answer_dict.items():
        answer_dict[key] = [value]
    single_instance = pd.DataFrame.from_dict(answer_dict)
    prediction = model.predict(single_instance)
    return prediction[0]


if __name__ == '__main__':

    data = pd.read_csv("traindata.csv")

    # Split dataset into features and labels
    features = data.drop('Response', axis =1)
    labels = data.Response

    # rename integer labels to actual
    names = {0 : 'No Acepta la campaña',
              1 : 'Acepta la campaña'}

    labels = np.vectorize(names.__getitem__)(labels)

    mdl = train(features, labels)

    # serialize model
    pickle.dump(mdl, open('model.mo', "wb"))
    with open("model.mo", "rb") as f:
        model = pickle.load(f)
    uvicorn.run(app, port=8000, host = "0.0.0.0", debug='true')
