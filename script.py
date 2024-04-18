import os
import requests
from datetime import date, datetime
from supabase import create_client
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("CURRENCY_API_KEY")
SUPABASE_URL = os.getenv("supabaseURL")
SUPABASE_KEY = os.getenv("supabaseKEY")

# URL de la API de tasas de cambio
API_URL = "https://api.currencyapi.com/v3/latest"

# Monedas deseadas
currencies = ["SVC", "USD", "EUR", "CRC", "GTQ", "NIO", "CNY", "RUB"]

# Parámetros de la solicitud
params = {
    "apikey": API_KEY,
    "currencies": ",".join(currencies),
    "base_currency": "HNL"
}

# Hacer la solicitud a la API
response = requests.get(API_URL, params=params)
data = response.json()

# Conectar con Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Insertar registros en la base de datos
if response.status_code == 200:
    last_updated_at = data["meta"]["last_updated_at"]
    rates_data = data["data"]

    for currency, info in rates_data.items():
        # Convertir fecha a string en formato ISO 8601
        current_date = datetime.now().isoformat()

        # Insertar un registro para cada moneda en la tabla historial_divisas
        supabase.from_("historial_divisas").insert([{
            "fecha": current_date,
            "divisa": info["code"],
            "tasa_cambio": info["value"]
        }]).execute()
    print("Registros insertados correctamente en la base de datos.")
else:
    print("Error al obtener datos de la API.")
