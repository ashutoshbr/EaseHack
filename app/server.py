from fastapi import FastAPI
from main import verify_data

app = FastAPI()


@app.get("/")
def get_home():
    return {"msg": "Namaste"}


@app.post("/")
def post_home(encoded_data: str):
    verified = verify_data(bytes(encoded_data, encoding="ascii"))
    return verified
