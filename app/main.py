
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .libros import router as libros_router
from .libros import schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from .auth.routers import router as auth_router
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

# Incluir el router de libros
app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])
app.include_router(libros_router, prefix="/api", tags=["Libros"])
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def leer_frontend():
    return FileResponse("app/templates/index.html")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)
