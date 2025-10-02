from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from presentation.schemas.schemas import AddArena, ArenaInfo
from core.models.models import Arena 
from infrastructure.Db.database import get_db
from application.services.arenaServices import ArenaService


router = APIRouter(
    prefix="/arenas",
    tags=["Arena & Court"]
)


@router.get("/", response_model=List[ArenaInfo])
async def get_arenas(db: Session = Depends(get_db)) -> List[ArenaInfo]:
    service = ArenaService(db)
    arenas = await service.getArenasWithCourts()
    if not arenas:
        raise HTTPException(status_code=404, detail="No Arenas yet")
    return arenas


@router.post("/", response_model=ArenaInfo)
async def create_arena(arena: AddArena, db: Session = Depends(get_db)) -> ArenaInfo:
    service = ArenaService(db)
    created = await service.create_arena(arena)
    return created
