from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel
import uvicorn
from data_interactor import Contact

app = FastAPI()

path = Path()


class Item(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.get("/items")
def get_items():
    items = Contact.get_all_contacts()
    return items


@app.post("/items")
def post_item(first_name, last_name, phone_number):
    pass


@app.put("/items{id}")
def put_item(id, first_name, last_name, phone_number):
    pass

@app.delete("/items{id}")
def delete_item(id):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
