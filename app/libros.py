from fastapi import APIRouter,Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=schemas.LibroResponse)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    nuevo_libro = models.Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        genero=libro.genero,
        anio_publicacion=libro.anio_publicacion
    )
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

@router.get("/", response_model=list[schemas.LibroResponse])  # <-- Añade este endpoint
async def listar_libros(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()

@router.get("/{libro_id}", response_model=schemas.LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.delete("/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    db.delete(libro)
    db.commit()
    return {"detail": "Libro eliminado exitosamente"}

    # hacer un get de buscar para buscar los libros por titulo, autor, genero o anio_publicacion
