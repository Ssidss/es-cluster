from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定義 JSON 結構
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int

# POST API 接收 JSON
@app.post("/items/")
async def create_item(item: dict):
    print(item)
    return {
        "message": "Item received",
        "item": item
    }
