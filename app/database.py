#database.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

DATABASE_URL = "postgresql://appbiblio:Eq_NdS2025@192.168.1.130:5432/biblioteca"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""try:
    # Intentar conectar y ejecutar una consulta simple
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexión OK:", result.scalar())
except Exception as e:
    print("Error en la conexión:", e)"""
