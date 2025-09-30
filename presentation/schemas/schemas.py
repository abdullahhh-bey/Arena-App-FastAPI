from pydantic import Field, EmailStr, BaseModel
from typing import List, Optional

class AddArena(BaseModel):
    name : str = Field(... , description="Name should be valid")
    email : EmailStr = Field(... , description="Email should be valid")
    location : str = Field(... , description="Location should be entered")

    
class AddCourt(BaseModel):
    name : str = Field(... , description="Name should be valid")
    type : str = Field(... , description="type should be entered")
    arena_id : int = Field(..., description="Enter Arena Id")
    
    
class AddCourtRule(BaseModel):
    court_id : int = Field(... , description="Court Id should be enterd")
    time_interval : int = Field(...)
    minimum_slot_booking : int = Field(...)
    

class CourtInfo(BaseModel):
    id : int
    name : str
    type : str
    
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
    
    class Config:
        from_attributes=True



class CourtWithRules(BaseModel):
    id : int
    name : str
    type : str
    courtRule : Optional[CourtRuleInfo] = None
    
    class Config:
        from_attributes=True