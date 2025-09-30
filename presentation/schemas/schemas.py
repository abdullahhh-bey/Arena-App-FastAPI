from pydantic import Field, EmailStr, BaseModel
from typing import List, Optional
from ...core.models.models import Court, CourtRule, Arena

class AddArena(BaseModel):
    name : str = Field(... , description="Name should be valid")
    email : EmailStr = Field(... , description="Email should be valid")