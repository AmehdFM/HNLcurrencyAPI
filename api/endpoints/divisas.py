from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
import datetime

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
            .execute()

        # Devolver la lista de registros
        return registros
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {e}")


@router.get("/historial/{divisa}")
def obtener_historial_por_divisa(divisa: str):
    try:
        # Consultar el historial de la divisa desde Supabase
        response = supabase.from_("historial_divisas").select("*").eq("divisa", divisa).execute()
        registros = response.data
        # Devolver la lista de registros
        return registros

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {e}")

@router.get("/datos")
def obtener_datos():
    try:
        # Consultar todos los datos de la tabla historial_divisas en Supabase
        response = supabase.from_("historial_divisas").select("*").execute()
        
        # Obtener los datos de la respuesta
        datos = response.data
        
        # Devolver los datos obtenidos
        return datos
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener datos: {e}")

@router.get("/convertir")
def convertir_monedas(moneda_origen: str, moneda_destino: str, cantidad: float):
    try:
        # Verificar si la moneda de origen es Lempiras y la de destino es otra divisa
        if moneda_origen.upper() == "HNL" and moneda_destino.upper() != "HNL":
            # Consultar la tasa de cambio más reciente de la moneda de destino desde Supabase
            response = supabase.from_("historial_divisas").select("tasa_cambio").eq("divisa", moneda_destino.upper()).order("fecha",).limit(1).execute()
            tasa_cambio = response.data[0]["tasa_cambio"]

            # Calcular la cantidad de la moneda de destino que se puede comprar con la cantidad de lempiras ingresada
            cantidad_moneda_destino = cantidad * tasa_cambio
        # Verificar si la moneda de destino es Lempiras y la de origen es otra divisa
        elif moneda_destino.upper() == "HNL" and moneda_origen.upper() != "HNL":
            # Consultar la tasa de cambio más reciente de la moneda de destino desde Supabase
            response = supabase.from_("historial_divisas").select("tasa_cambio").eq("divisa", moneda_destino.upper()).order("fecha",).limit(1).execute()
            tasa_cambio = response.data[0]["tasa_cambio"]

            # Calcular la cantidad de lempiras que se pueden obtener con la cantidad de la moneda de origen ingresada
            cantidad_lempiras = cantidad / tasa_cambio
            cantidad_moneda_destino = cantidad_lempiras
        else:
            raise HTTPException(status_code=400, detail="La conversión solo es válida entre lempiras y otras divisas.")

        # Devolver la cantidad de la moneda de destino que se puede comprar con la cantidad ingresada de la moneda de origen
        return {"moneda_destino": moneda_destino.upper(), "cantidad": cantidad_moneda_destino}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la conversión: {e}")