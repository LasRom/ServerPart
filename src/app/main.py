from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Мир!"}