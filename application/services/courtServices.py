from sqlalchemy.orm import Session
from presentation.schemas.schemas import AddCourt , AddCourtRule , CourtWithRules, CourtRuleInfo
from core.models.models import Court, CourtRule, Arena
from typing import List, Optional
from fastapi import HTTPException


class CourtService:
    def __init__(self , db : Session):
        self.db = db
        
        
    def AddCourt(self, c: AddCourt) -> CourtWithRules:
        checkArena = self.db.query(Arena).filter(Arena.id == c.arena_id).first()
        if not checkArena:
            raise HTTPException(status_code=404, detail="No arena")

        check = self.db.query(Court).filter(Court.name == c.name).first()
        if check:
            raise HTTPException(status_code=400, detail="Same name already exists")

        new_court = Court(
            name=c.name,
            type=c.type,
            arena_id=c.arena_id
        )

        self.db.add(new_court)
        self.db.commit()
        self.db.refresh(new_court)
        return new_court


    async def get_court(self) -> Optional[List[CourtWithRules]]:
        c = self.db.query(Court).all()
        return c
    
    
    async def AddCourtRule(self , c : AddCourtRule) -> CourtRuleInfo:
        checkCourt = self.db.query(Court).filter(Court.id == c.court_id).first()
        if checkCourt is None:
            raise HTTPException(
                status_code=400,
                detail="No Court"
            )
        
        new_rule = CourtRule(
            time_interval = c.time_interval,
            minimum_slot_booking = c.minimum_slot_booking,
            court_id = c.court_id
        )
        
        self.db.add(new_rule)
        self.db.commit()
        self.db.refresh(new_rule)
        return new_rule