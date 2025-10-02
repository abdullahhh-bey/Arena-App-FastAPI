from fastapi import FastAPI
from infrastructure.Db.database import Base, engine
from core.models.models import Arena, Court, CourtRule
from presentation.routes.router import router 
from presentation.routes.courtRouter import Crouter

app = FastAPI()
Base.metadata.create_all(bind=engine)

#register your router with the main app
app.include_router(router)
app.include_router(Crouter)

