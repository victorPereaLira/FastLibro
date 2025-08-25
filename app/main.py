
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .libros import router as libros_router
from .libros import schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from .auth.routers import router as auth_router
from .database import engine, Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI()
# Configurar Jinja2 para plantillas
templates = Jinja2Templates(directory="app/templates") 


# Incluir el router de libros y autenticación. Permite organizar la aplicación en módulos.
app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])
app.include_router(libros_router, prefix="/api", tags=["Libros"])

# Montar archivos estáticos nos permite servir archivos como CSS, JS, imágenes, etc.
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Acceso principal a la aplicacion FastAPI, sirve el archivo HTML principal
@app.get("/")
async def leer_frontend():
    return FileResponse("app/templates/index.html")

# Configurar CORS (Cross-Origin Resource Sharing) permite controloar que dominios pueden acceder a la api.
# Interesante volver a revisar con mas detelle en un futuro.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)
