from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, utils
from ..database import get_db

router = APIRouter(tags=["Autenticación"])

@router.post("/registro", response_model=schemas.UsuarioResponse)
async def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear un nuevo usuario
    hashed_password = utils.hash_password(usuario.password)
    nuevo_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=hashed_password
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario

@router.post("/login", response_model=schemas.Token)
async def login(
    credenciales: schemas.UserLogin,  # Usa el nuevo esquema específico
    db: Session = Depends(get_db)
):
    db_usuario = db.query(models.Usuario).filter(
        models.Usuario.email == credenciales.email
    ).first()
    
    if not db_usuario or not utils.verify_password(
        credenciales.password,
        db_usuario.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = utils.crear_access_token(
        data={"sub": db_usuario.email}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}