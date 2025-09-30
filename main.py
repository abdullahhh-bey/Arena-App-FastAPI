from fastapi import FastAPI , Depends, HTTPException
from infrastructure.Db.database import Base, engine
from core.models.models import Arena, Court, CourtRule


app = FastAPI()


Base.metadata.create_all(bind=engine)
