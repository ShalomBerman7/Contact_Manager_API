from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel
import uvicorn
from data_interactor import Contact

app = FastAPI()

path = Path()


class Items(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.get("/contacts")
def get_contacts():
    contacts = Contact.get_all_contacts()
    return contacts


@app.post("/contacts")
def create_contact(contacts: Items):
    contact = Contact.create_contact(contacts.first_name, contacts.last_name, contacts.phone_number)
    return contact


@app.put("/contacts{id}")
def update_contact(id, contacts: Items):
    contact = Contact.update_contact(id, contacts.first_name, contacts.last_name, contacts.phone_number)
    return contact


@app.delete("/contacts{id}")
def delete_contact(id):
    contact = Contact.delete_contact(id)
    return contact


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
