from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristics(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics

cars_liste: List[Car] = []

@app.get("/ping")
def ping():
    return "pong"

@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars_liste.append(car)
    return car