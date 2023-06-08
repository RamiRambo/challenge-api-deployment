from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Literal
from model.model import prediction
from preprocessing.cleaning_data import preprocess
import pandas as pd
import uvicorn

app = FastAPI()

class Item(BaseModel):
    living_area: int
    subtype : Literal["Mixed-use-building","Farmhouse","Country-cottage","House","New-real-estate-project-houses","Bungalow","Town-house","Chalet","Villa","Mansion","Manor-house","Castle","Exceptional-property"] 
    property_type: Literal["HOUSE", "APARTMENT"]
    kitchen_type : Literal["Hyper equipped", "USA hyper equipped", "USA installed","Installed", "USA uninstalled", "USA semi equipped", "Not installed", "Semi equipped"]
    rooms_number: Optional[int]
    zipcode: int
    land_area: Optional[int]
    garden: Optional[bool]
    garden_area: Optional[int]
    equipped_kitchen: Optional[bool]
    full_address: Optional[str]
    swimming_pool: Optional[bool]
    furnished: Optional[bool]
    open_fire: Optional[bool]
    terrace: Optional[bool]
    terrace_area: Optional[int]
    facades_number: Optional[int]
    building_state: str = ["NEW","GOOD","TO RENOVATE","JUST RENOVATED"]


@app.get("/")
async def root():
    return {"message": "Alive"}

@app.post("/predict")
async def create_item(item:Item):
    dicty = {"living_area" : item.living_area,"subtype" : item.subtype, "kitchen_type" : item.kitchen_type, "zipcode" : item.zipcode}
    data_prepro = preprocess(dicty)
    predict = prediction(data_prepro)
    return {"prediction is" : predict[0]}
    
# @app.get("/predict")
# async def result(predict:Item):
#     price = 2000 + 10000*predict.living_area + 20000*predict.rooms_number
#     return {"the price for your apartment is " : price}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")