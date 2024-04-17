import os
from supabase import create_client, Client

# Obtener la URL y la clave de acceso de Supabase desde las variables de entorno
url: str = "https://esacicqflhuqymygrqxa.supabase.co" #os.environ.get("supabaseURL")
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzYWNpY3FmbGh1cXlteWdycXhhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTMzMTYxNDUsImV4cCI6MjAyODg5MjE0NX0.Cgd2RxWg1wsTCpGPOhiKX5S6j7JGs_HTyJ487K7tysw" #os.environ.get("supabaseKEY")

# Crear cliente de Supabase
supabase: Client = create_client(url, key)
