from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schemas import items as schemas
from ..controllers import items
from ..dependencies.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return items.create(db=db, item=item)


@router.get("/", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    return items.read_all(db)


@router.get("/{item_id}", response_model=schemas.Item)
def read_one_item(item_id: int, db: Session = Depends(get_db)):
    item = items.read_one(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=schemas.Item)
def update_one_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item_db = items.read_one(db, item_id=item_id)
    if item_db is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return items.update(db=db, item=item, item_id=item_id)


@router.delete("/{item_id}")
def delete_one_item(item_id: int, db: Session = Depends(get_db)):
    item = items.read_one(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return items.delete(db=db, item_id=item_id)