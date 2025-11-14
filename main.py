from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI deployment successful!"}

@app.post("/predict")
def predict(data: dict):
    num = data.get("num", 0)
    return {"square": num * num}
