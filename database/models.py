from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RegistroDivisa(Base):
    __tablename__ = "historial_divisas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    divisa = Column(String(3), nullable=False)
    tasa_cambio = Column(Float, nullable=False)  # Cambiado de precio_compra y precio_venta a una sola tasa de cambio
