import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Configuración de la base de datos (reemplaza con tu URL de conexión)
current_dir = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{current_dir}\\registro_divisas.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Función para verificar la conexión a la base de datos
def check_db_connection():
    try:
        with engine.connect() as db:
            db.execute("SELECT 1")
        print("La conexión a la base de datos es correcta.")
    except Exception as e:
        print("Error al conectar a la base de datos:", e)

# Función para obtener una sesión de base de datos activa
def get_db():
    with engine.connect() as db:
        yield Session(db)

# Importa los modelos de datos
from .models import RegistroDivisa  # Importar el modelo RegistroDivisa

# Llamada a la función para verificar la conexión al importar este módulo
check_db_connection()
