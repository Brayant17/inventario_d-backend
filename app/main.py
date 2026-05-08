from fastapi import FastAPI
from app.core.config import APP_NAME
from app.core.config import APP_NAME
from app.routers import users

app = FastAPI(
    title=APP_NAME,
    version="1.0.0"
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/items")
def read_items():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}