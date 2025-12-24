from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

path = Path()

class Item(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.get("/items")
def get_items():
    pass


if __name__ == "__main__":
    pass