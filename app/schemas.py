from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    genero: str
    anio_publicacion: int
    

class LibroResponse(LibroCreate):
    id: int

    class Config:
        from_attributes = True