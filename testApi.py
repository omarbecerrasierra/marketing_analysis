import requests

url = 'http://0.0.0.0:8000/predict'  # localhost and the defined port + endpoint
body = {
    'Income' : 46344,
    'Kidhome' : 1,
    'Teenhome' : 1,
    'Recency' : 38,
    'MntWines' : 11,
    'MntFruits' : 1,
    'MntMeatProducts' : 6,
    'MntFishProducts' : 2,
    'MntSweetProducts' : 1,
    'MntGoldProds' : 6,
    'NumDealsPurchases' : 2,
    'NumWebPurchases' : 1,
    'NumCatalogPurchases' : 1,
    'NumStorePurchases' : 2,
    'NumWebVisitsMonth' : 5,
    'AcceptedCmp3' : 0,
    'AcceptedCmp4' : 0,
    'AcceptedCmp5' : 0,
    'AcceptedCmp1' : 0,
    'AcceptedCmp2' : 0,
    'Complain' : 0,
    'Age' : 67,
    'Customer_Days' : 2674,
    'Second_Cycle' : 0,
    'Basic' : 0,
    'Graduation' : 1,
    'Master' : 0,
    'PhD' : 0,
    'Divorced' : 0,
    'Married' : 0,
    'Single' : 1,
    'Together' : 0,
    'Widow' : 0,
    'MntTotal' : 21,
    'MntRegularProds' : 15,
    'AcceptedCmpOverall' : 0
}
response = requests.post(url, json=body)
print(response.json())