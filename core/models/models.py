from sqlalchemy import Column, Integer, String, ForeignKey, Time , Date , Boolean
from sqlalchemy.orm import relationship
from infrastructure.Db.database import Base, engine
from datetime import time, date

class Arena(Base):
    
    __tablename__ = "arenas"
    
    id = Column(Integer , primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255), nullable=False)
    email = Column(String(255) , nullable=False , unique=True, index=True)
    
    courts = relationship("Court" , back_populates="arena")
    
    
    
class Court(Base):
    
    __tablename__ = "courts"
    
    id = Column(Integer , primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String(255) , nullable=False , index=True)
    
    arena_id = Column(Integer , ForeignKey("arenas.id"))
    arena = relationship("Arena" , back_populates="courts")
    
    bookings = relationship("Booking", back_populates="court")
    
    courtRule = relationship("CourtRule" , back_populates="court", uselist=False, lazy="joined")
    
    slots = relationship("TimeSlot" , back_populates="court")
    
    
    
class CourtRule(Base):
    
    __tablename__ = "courtRules"
    
    id = Column(Integer , primary_key=True, index=True)
    time_interval = Column(Integer, nullable=False)
    minimum_slot_booking = Column(Integer, nullable=False)
    
    court_id = Column(Integer, ForeignKey("courts.id"))
    court = relationship("Court" , back_populates="courtRule")
    
    
class TimeSlot(Base):
    
    __tablename__ = "timeslots"
    
    id = Column(Integer , primary_key=True, index=True)
    start = Column(Time , nullable=False)
    end  = Column(Time  , nullable=False)
    date = Column(Date , nullable=False)
    price = Column(Integer , nullable=False)
    status = Column(Boolean , nullable=False, default=True)
        
    court_id = Column(Integer, ForeignKey("courts.id"))
    court = relationship("Court" , back_populates="slots")
    
    slot_booking = relationship("SlotsBooking" , back_populates="slot", uselist=False)
    
    
    
class SlotsBooking(Base):
    
    __tablename__ = "slotsbooking"

    id = Column(Integer , primary_key=True, index=True)
    
    timeslot_id = Column(Integer , ForeignKey("timeslots.id"), unique=True)
    
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    booking = relationship("Booking" , back_populates="booked_slots")
    
    slot = relationship("TimeSlot" , back_populates="slot_booking" , uselist=False)
    

class Booking(Base):
    
    __tablename__ = "bookings"
    
    id = Column(Integer , primary_key=True, index=True)
    bookingStart = Column(Time , nullable=False)
    bookingEnd  = Column(Time  , nullable=False)
    bookingDate = Column(Date , nullable=False)
    bookingAmount = Column(Integer , nullable=False)
    bookingStatus = Column(Boolean , nullable=False, default=True)
    
    booked_slots = relationship("SlotsBooking" , back_populates="booking", cascade="all, delete-orphan")
    
    court_id = Column(Integer, ForeignKey("courts.id"))
    court = relationship("Court" , back_populates="bookings")
    
    
    
#for creating tables according to the models
Base.metadata.create_all(bind=engine)
