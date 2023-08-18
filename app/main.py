from fastapi import FastAPI,Request
import pickle
import numpy as np
from app.code import predict_car
import os


m = pickle.load(open(os.getcwd()+r'/model/model.pkl', 'rb'))

app = FastAPI()

@app.get("/")
def root():
    return {"message": "This is my api"}



@app.post("/api/carbrand")
async def read_str(data : Request):
    json=await data.json()
    img_string=json["img"]
    car = predict_car(m,img_string)
    return {"brand":car}