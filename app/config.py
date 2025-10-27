# Configuración de Supabase
SUPABASE_URL = "https://ucwoxwmiryxnipaxoole.supabase.co/rest/v1/mesa"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVjd294d21pcnl4bmlwYXhvb2xlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEzMTIyOTEsImV4cCI6MjA3Njg4ODI5MX0.zQpc6rVkHU2y0vUy_B5WxV9-XyGiMkdcaxK4LtlEJKw"
HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}
