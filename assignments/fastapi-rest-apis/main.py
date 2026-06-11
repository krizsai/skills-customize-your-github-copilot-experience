from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Items API")

class Item(BaseModel):
    id: Optional[int]
    name: str
    price: float

# In-memory store
_items: List[Item] = []
_next_id = 1

@app.get("/items", response_model=List[Item])
async def list_items():
    return _items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in _items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated: Item):
    for idx, item in enumerate(_items):
        if item.id == item_id:
            updated.id = item_id
            _items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    for idx, item in enumerate(_items):
        if item.id == item_id:
            _items.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")
