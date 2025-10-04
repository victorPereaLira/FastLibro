from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String, index=True)
    anio_publicacion = Column(Integer)
    genero = Column(String, index=True)

    user_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="libros")

class Obra(Base):
    __tablename__ ="obras"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    genero = Column(String)
    anyo_publicacion = Column(Integer, nullable=True)

    ediciones = relationship("Edicion", back_populates="obra")
    
    __table_args__ = (
        UniqueConstraint("titulo", "autor", "anyo_publicacion", name="uix_titulo_autor"),
    )

class Edicion(Base):
    __tablename__ ="ediciones"
    id = Column(Integer, primary_key=True, index=True)
    obra_id = Column(Integer, ForeignKey("obras.id"), nullable=False)
    editorial_id = Column(String)
    isbn = Column(String, unique=True, nullable=True)
    anyo_publicacion_origial = Column(Integer, nullable=True)
    obra = relationship("Obra", back_populates="ediciones")
    lecturas = relationship("Lectura", back_populates="edicion")



class Lectura(Base):
    __tablename__ ="lecturas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    edicion_id = Column(Integer, ForeignKey("ediciones.id"), nullable=False)
    """editorial_id = Column(Integer, ForeignKey("editoriales.id"), nullable=False)"""

    anyo_Leido = Column(Integer)
    comentario = Column(String)
    valor_escrito = Column(Integer)

    usuario = relationship("Usuario", back_populates="lecturas")
    edicion = relationship("Edicion", back_populates="lecturas")

    __table_args__ = (
        UniqueConstraint("usuario_id", "edicion_id", name="uix_usuario_edicion"),
    )