from typing import Optional
from pydantic import PROYECTO_API_PELICULA

class User(PROYECTO_API_PELICULA):
    id:Optional[int]
    username:str
    nombre:str
    rol:str
    estado:int

    class Config:
        orm_mode =True

class UserUpdate(PROYECTO_API_PELICULA):   
    nombre:str
   

    class Config:
        orm_mode =True

class Respuesta(PROYECTO_API_PELICULA):   
    mensaje:str