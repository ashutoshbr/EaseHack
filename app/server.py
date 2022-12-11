from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.get("/")
def get_home():
    return {"msg": "Namaste"}


@app.post("/")
def post_home(encoded_data: schemas.PostHome):
    return "Verified"
