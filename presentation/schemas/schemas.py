from pydantic import Field, EmailStr, BaseModel
from typing import List, Optional
from datetime import time, date

class AddArena(BaseModel):
    name : str = Field(... , description="Name should be valid")
    email : EmailStr = Field(... , description="Email should be valid")
    location : str = Field(... , description="Location should be entered")

    
class AddCourt(BaseModel):
    name : str = Field(... , description="Name should be valid")
    type : str = Field(... , description="type should be entered")
    arena_id : int = Field(..., description="Enter Arena Id")
    
    
class AddCourtRule(BaseModel):
    court_id : int = Field(... )
    time_interval : int = Field(...)
    minimum_slot_booking : int = Field(...)
    

class CourtInfo(BaseModel):
    id : int
    name : str
    type : str
    arena_id : int
    
    class Config:
        from_attributes=True
    
    
class ArenaInfo(BaseModel):
    id : int
    name : str
    email : str
    location : str
    courts : Optional[List[CourtInfo]] = []
    
    class Config:
        from_attributes=True
        

class CourtRuleInfo(BaseModel):
    id : int
    time_interval : int
    minimum_slot_booking : int
    court_id : int
    
    class Config:
        from_attributes=True



class CourtWithRules(CourtInfo):
    courtRule : Optional[CourtRuleInfo] = None
    
    class Config:
        from_attributes=True
        
        
class CreateTimeSlots(BaseModel):
    court_id : int = Field(...)
    slot_date : date = Field(...)
    start : int = Field(...)
    end : int = Field(...)
    price : int = Field(...)
    status : bool = Field(...)
    
class AvailableSlots(BaseModel):
    id : int
    court_id : int 
    slot_date : date 
    start : str
    end : str 
    price : int 
    status : bool 
    
    class Config:
        from_attributes=True

class CourtWithSlots(CourtInfo):
    slots : List[AvailableSlots] = None
    
    class Config:
        from_attributes=True
        

class CreateBooking(BaseModel):
    court_id : int
    user_id : int
    slot_id : List[int]
    bookingDate : date
    
class GetBookings(BaseModel):
    id : int
    bookingStart : time
    bookingEnd  : time
    bookingDate : date
    bookingAmount : int
    bookingStatus : bool
    
    court_id : int
    
    class Config:
        from_attributes=True
        
        
class GetBookingsByCourt(GetBookings):
    booked_slots : List[AvailableSlots]  
    
    class Config:
        from_attributes=True