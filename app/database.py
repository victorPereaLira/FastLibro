#database.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()  

# Obtener las variables de entorno necesarias para la conexión a la base de datos del fichero .env PostgreSQL
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Comprobacion de que las varaibles de enentorno se han cargado correctamente.
if not all( [DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME] ):
    raise ValueError("Faltan variables de entorno necesarias para la conexión a la base de datos.")


DATABASE_URL = f"postgresql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



