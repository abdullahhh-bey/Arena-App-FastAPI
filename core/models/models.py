from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.Db.database import Base, engine

class Arena(Base):
    
    __tablename__ = "arenas"
    
    id = Column(Integer , primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255), nullable=False)
    email = Column(String(255) , nullable=False , index=True)
    
    courts = relationship("Court" , back_populates="arena")
    
    
    
class Court(Base):
    
    __tablename__ = "courts"
    
    id = Column(Integer , primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String(255) , nullable=False , index=True)
    
    arena_id = Column(Integer , ForeignKey("arenas.id"))
    arena = relationship("Arena" , back_populates="courts")
    
    courtRule = relationship("CourtRule" , back_populates="court", uselist=False)
    
    
    
    
class CourtRule(Base):
    
    __tablename__ = "courtRules"
    
    id = Column(Integer , primary_key=True, index=True)
    time_interval = Column(Integer, nullable=False)
    minimum_slot_booking = Column(Integer, nullable=False)
    
    court_id = Column(Integer, ForeignKey("courts.id"))
    court = relationship("Court" , back_populates="courtRule")
    
    
#for creating tables according to the models
Base.metadata.create_all(bind=engine)
