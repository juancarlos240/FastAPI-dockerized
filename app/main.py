from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages:int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message":"Hola, FastAPI"}

@app.get("/book/{id}")
def show_book(id: int):
    return {"data": id}

@app.post("/book")
def add_book(book:Book):
    return {"message": f"Book {book.title} added."}