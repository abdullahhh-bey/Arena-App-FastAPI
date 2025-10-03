from fastapi import FastAPI
from infrastructure.Db.database import Base, engine
from core.models.models import Arena, Court, CourtRule
from presentation.routes.router import router 
from presentation.routes.courtRouter import Crouter
from presentation.routes.timeslotRouter import Trouter
from presentation.routes.bookingRouter import Brouter
from core.models.models import TimeSlot

app = FastAPI()
 

#register your router with the main app
app.include_router(router)
app.include_router(Trouter)
app.include_router(Crouter)
app.include_router(Brouter)


