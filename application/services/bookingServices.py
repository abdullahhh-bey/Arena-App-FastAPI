from presentation.schemas.schemas import AvailableSlots , CreateBooking , GetBookings, GetBookingsByCourt
from core.models.models import Court, CourtRule, Booking, TimeSlot, SlotsBooking
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import date, time


class BookingService:
    
    def __init__(self, db : Session):
        self.db = db
        
    
    def AddBookingService(self, data : CreateBooking) -> GetBookings:
        court = self.db.query(Court).filter(Court.id == data.court_id).first()
        if not court:
            raise HTTPException(status_code=404, detail="Court not found")

        rules = self.db.query(CourtRule).filter(CourtRule.court_id == data.court_id).first()
        if not rules:
            raise HTTPException(status_code=400, detail="Court rules not defined")

        slots = self.db.query(TimeSlot).filter(
            TimeSlot.id.in_(data.slot_id),
            TimeSlot.court_id == data.court_id,
            TimeSlot.is_available == True
        ).order_by(TimeSlot.start_time).all()

        if not slots or len(slots) == 0:
            raise HTTPException(status_code=400, detail=f"Invalid slots for Court {data.court_id}")

        if len(slots) != len(data.slot_id):
            raise HTTPException(status_code=400, detail="One or more slots are unavailable")

        if len(slots) < rules.minimum_slot_booking:
            raise HTTPException(
                status_code=400,
                detail=f"You must book at least {rules.minimum_slot_booking} slots"
            )

        for i in range(len(slots) - 1):
            if slots[i + 1].start_time != slots[i].end_time:
                raise HTTPException(status_code=400, detail="Slots must be continuous without gaps")

        booking = Booking(
            court_id=data.court_id,
            bookingDate=data.bookingDate,
            bookingStart=slots[0].start_time,
            bookingEnd=slots[-1].end_time,
            bookingStatus=True
        )
        
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        
        

        for slot in slots:
            slot.is_available = False
            sb = SlotsBooking(
                timeslot_id=slot.id, 
                booking_id=booking.id
            )
            self.db.commit()
        

        return GetBookings(
            id=booking.id,
            bookingStart=slots[0].start_time,
            bookingEnd=slots[-1].end_time,
            bookingDate=data.bookingDate,
            bookingAmount=sum(s.price for s in slots),
            bookingStatus=booking.booking_status,
            court_id=data.court_id
        )
        
    def GetBookings(self) -> List[GetBookings]:
        bookings = self.db.query(Booking).all()
        
        result = [ GetBookings(
            id=b.id,
            bookingStart=b.start_time,
            bookingEnd=b.end_time,
            bookingDate=b.bookingDate,
            bookingAmount=b.bookingAmount,
            bookingStatus=b.booking_status,
            court_id=b.court_id
        ) for b in bookings ]
        
        return result
    
    def GetBookingWithCourtIdWithDate(id : int , date : date, self) -> GetBookingsByCourt:
        bookings = self.db.query(Booking).filter(Booking.court_id == id and Booking.bookingDate == date).all()
        
        result = [ GetBookingsByCourt(
            
        ) for b in bookings ]