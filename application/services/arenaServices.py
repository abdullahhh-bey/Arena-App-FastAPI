from sqlalchemy.orm import Session
from ...presentation.schemas.schemas import AddArena , ArenaInfo
from ...core.models.models import Arena
from typing import List, Optional


class ArenaService:
    def __init__(self, db : Session):
        self.db = db
        
    
    async def create_arena(self, a : AddArena) -> ArenaInfo:
        new_arena = Arena(
            name = a.name,
            email = a.email,
            location = a.location
        )
        
        self.db.add(new_arena)
        self.db.commit()
        self.db.refres(new_arena)
        return new_arena
    
    
    async def getArenasWithCourts(self) -> Optional[List[ArenaInfo]]:
        a = self.db.query(Arena).all()
        return a
    
    
