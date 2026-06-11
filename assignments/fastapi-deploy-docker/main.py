from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Deploy Demo")

class Item(BaseModel):
    id: Optional[int]
    name: str
    price: float

_items: List[Item] = []
_next_id = 1

@app.get("/items", response_model=List[Item])
async def list_items():
    return _items

@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _items.append(item)
    return item
