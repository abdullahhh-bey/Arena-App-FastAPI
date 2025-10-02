from sqlalchemy.orm import Session
from presentation.schemas.schemas import CourtWithRules, CourtRuleInfo, CreateTimeSlots,  AvailableSlots, CourtWithSlots
from core.models.models import Court, CourtRule, TimeSlot
from typing import List, Optional
from fastapi import HTTPException

class TimeSlotService:
    def __init__(self, db : Session):
        self.db = db
        
    def AddTimeSlotsService(self , slots : CreateTimeSlots) -> AvailableSlots:
        return
