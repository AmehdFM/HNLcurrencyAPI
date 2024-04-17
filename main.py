from fastapi import FastAPI
from api.endpoints.divisas import router  # Importar el router de la API

app = FastAPI(
    title="API Historial de Divisas",
    description="API para registrar y consultar el historial de divisas.",
    version="1.0.0",
)

app.include_router(router, tags=["Divisas"])
