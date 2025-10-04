from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List , Optional
from presentation.schemas.schemas import   AvailableSlots, GetBookings, CreateBooking, GetBookingsByCourt
from infrastructure.Db.database import get_db
from application.services.bookingServices import BookingService
from datetime import time, date

Brouter = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@Brouter.post("/" , response_model=GetBookings)
def CreateBooking( b : CreateBooking ,db : Session = Depends(get_db)) -> GetBookings:
    service = BookingService(db)
    booking = service.AddBookingService(b)
    return booking

@Brouter.get("/", response_model=List[GetBookings])
def GetBookingsAll(db : Session = Depends(get_db)) -> List[GetBookings]:
    service = BookingService(db)
    bookings = service.GetBookings()
    return bookings

@Brouter.get("/{id}", response_model=list[GetBookingsByCourt])
def GetBookingByCourtId(id : int , date : date = date.today(), db : Session = Depends(get_db)):
    service = BookingService(db)
    b = service.GetBookingWithCourtIdWithDate(id , date)
    return b
    