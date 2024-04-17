from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import datetime

from api.models.registro_divisas import RegistroDivisaRequest
from database.db import supabase  # Importar el cliente de Supabase desde db.py


router = APIRouter(tags=["Registro de divisas"])

@router.get("/historial/{divisa}/{fecha_inicio}/{fecha_fin}")
def obtener_historial(divisa: str, fecha_inicio: str, fecha_fin: str):
    try:
        # Consultar el historial de la divisa desde Supabase
        registros = supabase.from_("historial_divisas") \
            .select("*") \
            .eq("divisa", divisa) \
            .gte("fecha", fecha_inicio) \
            .lte("fecha", fecha_fin) \
            .execute().get("data")

        # Devolver la lista de registros
        return registros
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {e}")


@router.get("/historial/{divisa}")
def obtener_historial_por_divisa(divisa: str):
    try:
        # Consultar el historial de la divisa desde Supabase
        registros = supabase.from_("historial_divisas").select("*").eq("divisa", divisa).execute().get("data")

        # Devolver la lista de registros
        return registros

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {e}")