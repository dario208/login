from typing import List, Optional

from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# Simple in-memory store for demo purposes only.
FAKE_DB: List[Item] = [
    Item(id=1, name="Sample item", description="Seed item to start with"),
]


@router.get("", response_model=List[Item], summary="List items")
def list_items() -> List[Item]:
    return FAKE_DB


@router.post("", response_model=Item, status_code=201, summary="Create item")
def create_item(item: Item = Body(...)) -> Item:
    FAKE_DB.append(item)
    return item
