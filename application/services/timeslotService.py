from sqlalchemy.orm import Session
from presentation.schemas.schemas import CourtWithRules, CourtRuleInfo, CreateTimeSlots,  AvailableSlots, CourtWithSlots
from core.models.models import Court, CourtRule, TimeSlot
from typing import List, Optional
from fastapi import HTTPException
from datetime import time, datetime, timedelta

class TimeSlotService:
    def __init__(self, db : Session):
        self.db = db
        
    def AddTimeSlotsService(self, slots: CreateTimeSlots) -> List[AvailableSlots]:
        if slots.slot_date < datetime.date():
            raise HTTPException(status_code=400, detail="Date cannot be in the past")

        if slots.start >= slots.end or slots.start < 0 or slots.end > 24:
            raise HTTPException(status_code=400, detail="Invalid start/end time")

        court = self.db.query(Court).filter(Court.id == slots.court_id).first()
        if not court:
            raise HTTPException(status_code=404, detail="Court not found")

        rules = self.db.query(CourtRule).filter(CourtRule.court_id == slots.court_id).first()
        if not rules:
            raise HTTPException(status_code=400, detail="Court rules not defined")

        existing = self.db.query(TimeSlot).filter(
            TimeSlot.court_id == slots.court_id,
            TimeSlot.slot_date == slots.slot_date
        ).all()

        new_slots = []
        start_time = timedelta(hours=slots.start)
        end_time = timedelta(hours=slots.end)

        t = start_time
        while t < end_time:
            slot_end = t + timedelta(minutes=rules.time_interval)
            if slot_end > end_time:
                break

            conflict = any(
                (s.start < (datetime.min + slot_end).time() and s.end > (datetime.min + t).time())
                for s in existing
            )
            
            if conflict:
                raise HTTPException(
                    status_code = 400,
                    detail="There are slots within this time ( Overlappimg )"
                )
            
            if not conflict:
                new_slot = TimeSlot(
                    court_id=slots.court_id,
                    slot_date=slots.slot_date,
                    start=(datetime.min + t).time(),
                    end=(datetime.min + slot_end).time(),
                    price=slots.price,
                    status=True
                )
                new_slots.append(new_slot)

            t = slot_end

        if not new_slots:
            raise HTTPException(status_code=400, detail="No valid slots to add")

        self.db.add_all(new_slots)
        self.db.commit()
        self.db.refresh(new_slots[0])  

        return [
            AvailableSlots(
                id=s.id,
                court_id=s.court_id,
                slot_date=s.slot_date,
                start=str(s.start),
                end=str(s.end),
                price=s.price,
                status=s.status
            )
            for s in new_slots
        ]


    # def GetAvailableSlots(self) -> List[]