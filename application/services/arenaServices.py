from sqlalchemy.orm import Session
from ...presentation.schemas.schemas import AddArena , ArenaInfo
from ...core.models.models import Arena

class ArenaService:
    def __init__(self, db : Session):
        self.db = db
        

