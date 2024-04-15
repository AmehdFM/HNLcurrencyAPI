from fastapi import FastAPI
from database.db import get_db, engine
from api.endpoints.divisas import router  # Importar el router de la API

app = FastAPI(
    title="API Historial de Divisas",
    description="API para registrar y consultar el historial de divisas.",
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    await create_tables()

@app.on_event("shutdown")
async def shutdown_event():
    await close_connection()

async def create_tables():
    from database.models import Base  # Importar la base de modelos
    Base.metadata.create_all(engine)

async def close_connection():
    db = SessionLocal()
    try:
        await db.close()
    except Exception as e:
        raise e

app.include_router(router, tags=["Divisas"])
