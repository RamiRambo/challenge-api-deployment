import pandas as pd
urban_cities = pd.read_csv("./main/preprocessing/Urbain.csv")

apartments = ["Service-flat", "Apartment","Ground-floor", "New-real-estate-project-apartments", "Duplex"]
kots = ["Flat-studio", "Kot"]
lofts = ["Loft", "Triplex", "Apartment-block", "Penthouse"]
houses = ["Mixed-use-building", "Farmhouse","Country-cottage", "House", "New-real-estate-project-houses","Bungalow", "Town-house", "Chalet"]
villa = ["Villa","Mansion","Manor-house"]
hyper_equipped = ["Hyper equipped", "USA hyper equipped"]
installed = ["USA installed","Installed", "USA uninstalled", "USA semi equipped"]
not_equipped = ["Not installed", "Semi equipped"]

def preprocess(data):
    if data["subtype"] in apartments:
        data["subtype"] = 2
    elif data["subtype"] in lofts :
        data["subtype"] = 0
    elif data["subtype"] in kots :
        data["subtype"] = 1
    elif data["subtype"] in houses:
        data["subtype"] = 0
    elif data["subtype"] in villa :
        data["subtype"] = 2

    if data["kitchen_type"] in hyper_equipped	:
        data["kitchen_type"] = 1
    elif data["kitchen_type"] in installed :
        data["kitchen_type"] = 0
    elif data["kitchen_type"] in not_equipped :
        data["kitchen_type"] = 2
    
    if data["zipcode"] in urban_cities["Postcode"]:
        data["zipcode"] = 1
    elif not data["zipcode"] in urban_cities["Postcode"]:
        data["zipcode"] = 0


    return data