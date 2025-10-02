from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List , Optional
from presentation.schemas.schemas import AddCourt, CourtInfo, CourtRuleInfo, AddCourtRule, CourtWithRules
from core.models.models import Arena , Court, CourtRule
from infrastructure.Db.database import get_db
from application.services.courtServices import CourtService

Crouter = APIRouter(
    prefix="/courts",
    tags=["Courts"]
)

@Crouter.post("/" , response_model=CourtWithRules)
def CreateCourt( c : AddCourt ,db: Session = Depends(get_db)) -> CourtWithRules:
    service = CourtService(db)
    c =  service.AddCourt(c)
    return c


@Crouter.get("/" , response_model=Optional[List[CourtWithRules]])
async def GetCourt( db: Session = Depends(get_db)) -> Optional[List[CourtWithRules]]:
    service = CourtService(db)
    c = await service.get_court()
    return c


@Crouter.post("/rule" , response_model=CourtRuleInfo)
async def CreateCourt( c : AddCourtRule ,db: Session = Depends(get_db)) -> CourtRuleInfo:
    service = CourtService(db)
    c = await service.AddCourtRule(c)
    return c

