from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API FastAPI fonctionne!"}

@app.get("/ping")
def ping():
    return {"message": "pong", "status": "OK"}