from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List , Optional
from presentation.schemas.schemas import  CourtInfo , CreateTimeSlots, CourtWithSlots, AvailableSlots
from infrastructure.Db.database import get_db
from application.services.timeslotService import TimeSlotService

Trouter = APIRouter(
    prefix="/timeslots",
    tags=["TimeSlotis"]
)

@Trouter.post("/", response_model=List[AvailableSlots])
async def CreateSlots(t : CreateTimeSlots, db : Session = Depends(get_db)) -> List[AvailableSlots]:
    service = TimeSlotService(db)
    slots = await service.AddTimeSlotsService(t)
    return slots


@Trouter.get("/", response_model=List[AvailableSlots])
async def GetAvailableSlot(db : Session = Depends(get_db)) -> List[AvailableSlots]:
    service = TimeSlotService(db)
    slots = await service.GetAvailableSlots()
    return slots

@Trouter.get("/courts/{id}" , response_model=CourtWithSlots)
async def GetCourtWithSlots(id : int , db : Session = Depends(get_db)) -> CourtWithSlots:
    service = TimeSlotService(db)
    courtSlots = service.GetCourtWithSlots(id)
    return courtSlots