from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import datetime

from api.models.registro_divisas import RegistroDivisaRequest
from database.db import get_db
from database.models import RegistroDivisa

router = APIRouter(tags=["Registro de divisas"])

@router.post("/registros")
def agregar_registro(registro: RegistroDivisaRequest, db: Session = Depends(get_db)):
    try:
        fecha_objeto = datetime.datetime.strptime(registro.fecha, "%Y-%m-%d").date()
        # Crear un nuevo objeto RegistroDivisa a partir del request
        registro_db = RegistroDivisa(
            fecha=fecha_objeto,
            divisa=registro.divisa,
            tasa_cambio=registro.tasa_cambio  # Cambiar a tasa_cambio en lugar de precio_compra y precio_venta
        )

        # Agregar el registro a la base de datos
        db.add(registro_db)
        db.commit()

        # Devolver el registro creado
        return registro_db
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar registro: {e}")

@router.get("/historial/{divisa}/{fecha_inicio}/{fecha_fin}")
def obtener_historial(divisa: str, fecha_inicio: str, fecha_fin: str, db: Session = Depends(get_db)):
    try:
        # Consultar el historial de la divisa en el rango de fechas especificado
        registros = db.query(RegistroDivisa) \
            .filter(RegistroDivisa.divisa == divisa) \
            .filter(RegistroDivisa.fecha >= fecha_inicio) \
            .filter(RegistroDivisa.fecha <= fecha_fin) \
            .all()

        # Devolver la lista de registros
        return registros
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {e}")

@router.get("/historial/{divisa}")
def obtener_historial_por_divisa(divisa: str, db: Session = Depends(get_db)):
    try:
        # Consultar el historial de la divisa
        registros = db.query(RegistroDivisa) \
            .filter(RegistroDivisa.divisa == divisa) \
            .all()

        # Devolver la lista de registros
        return registros

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {e}")
