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

@app.get("/cars")
def get_cars():
    return cars_liste

@app.get("/cars/{id}")
def get_car(id: str):
    for car in cars_liste:
        if car.identifier == id:
            return car
    raise HTTPException(status_code=404, detail="Le phone comportant l'id fourni n'existe pas ou n'a pas été trouvé")

@app.put("/cars/{id}/characteristics")
def update_car_characteristics(id: str, characteristics: Characteristics):
    for car in cars_liste:
            return car
