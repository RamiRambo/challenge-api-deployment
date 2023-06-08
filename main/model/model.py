import pandas as pd
import numpy as np 
from matplotlib import pyplot as plot
import sklearn
import pickle
import statsmodels.api as sms
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

model_pkl_file = "./main/model/houses_price_prediction.pkl"

with open(model_pkl_file, 'rb') as file:  
    model = pickle.load(file)

# evaluate model 
def prediction(data):
    y_predict = model.predict([[data["living_area"], data["subtype"], data["kitchen_type"], data["zipcode"]]])
    return y_predict
