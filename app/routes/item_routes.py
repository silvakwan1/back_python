from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.item_schema import ItemCreate, ItemResponse
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()

async def get_item_by_id(db: AsyncIOMotorClient, item_id: str):
    return await db.items.find_one({"_id": ObjectId(item_id)})

@router.get("/", response_model=list[ItemResponse])
async def get_items(db=Depends(get_db)):
    items = []
    cursor = db.items.find({})
    async for item in cursor:
        items.append(ItemResponse(**item))
    return items

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str, db=Depends(get_db)):
    item = await get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return ItemResponse(**item)

# POST - Criar um novo item
@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db=Depends(get_db)):
    new_item = {
        "name": item.name,
        "description": item.description,
        "start_date": item.start_date,
        "end_date": item.end_date,
        "image_url": item.image_url
    }
    result = await db.items.insert_one(new_item)
    new_item["id"] = str(result.inserted_id)
    return ItemResponse(**new_item)
