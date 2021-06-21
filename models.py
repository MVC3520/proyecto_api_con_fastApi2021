from sqlalchemy import Column, Integer, String
from PROYECTO_API_PELICULA import Base

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    nombre = Column(String(200))
    rol = Column(String(20))
    estado = Column(Integer)