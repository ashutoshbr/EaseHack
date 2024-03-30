from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utils.transcoder import verify_data

app = FastAPI()


@app.get("/")
def get_home():
    return HTMLResponse(
        """<h3>Version 1 of API is available at:<br>https://easehack.azurewebsites.net/api/v1/<h3>"""
    )


@app.post("/api/v1/")
def post_home(encoded_data: str):
    verified = verify_data(bytes(encoded_data, encoding="utf-8"))
    return verified
