import os
from supabase import create_client, Client

# Obtener la URL y la clave de acceso de Supabase desde las variables de entorno
url: str = os.environ.get("supabaseURL")
key: str = os.environ.get("supabaseKEY")

# Crear cliente de Supabase
supabase: Client = create_client(url, key)
