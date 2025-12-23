from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

path = Path()

class Item(BaseModel):
    first_name: str
    last_name: str
    phone_number: int


@app.get("/items")
def get_items():
    return