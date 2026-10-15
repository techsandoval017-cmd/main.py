import os
import sys
import sqlite3
import re
from dotenv import load_dotenv
from google import genai

# 1. RASTREO IMPLACABLE DE TU LLAVE EN TODA LA MÁQUINA
rutas_env = [
    ".env",
    "/workspaces/main.py/.env",
    "/workspaces/main.py/credenciales_maestras.env",
    os.path.expanduser("~/.env"),
    os.path.expanduser("~/jarvis_hub/.env")
]

api_key = None
for ruta in rutas_env:
    if os.path.exists(ruta):
        load_dotenv(ruta)
        key_encontrada = os.environ.get("GEMINI_API_KEY")
        if key_encontrada:
            api_key = key_encontrada.strip("'\" \t\r\n")
            print(f"🔓 Llave Maestra detectada en: {ruta}")
            break

if not api_key:
    print("❌ ERROR: No se encontró tu GEMINI_API_KEY en ninguna bóveda.")
    print("Solución: Corre este comando antes de ejecutar el script:")
    print("echo 'GEMINI_API_KEY=\"TU_CLAVE\"' > .env")
    sys.exit(1)

# Inicializar el cliente con el nuevo motor de Google
client = genai.Client(api_key=api_key)

# Configuración del Imperio S-Prime
BOVEDA_DIR = "sprime_boveda_codigo/landing_nichos"
PROD_DIR = "productos/nichos"
DB_PATH = "sprime_boveda_codigo/codigo_central.db"

os.makedirs(BOVEDA_DIR, exist_ok=True)
os.makedirs(PROD_DIR, exist_ok=True)

# Prompts base (Diccionario de misiones)
MISIONES = {
    "barberia": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS (un solo archivo) para Landing Page 'Barbería 0 a 100'. Fondo oscuro, verde neón, tipografía Rajdhani. Tarjetas: 'Kit de Inicio', 'Golden Suite Software' ('Acceso sujeto a suscripción'). Botón: 'Explora opciones de financiamiento Tech'. Barra lateral: 'Progreso de Estudiante' (Nivel E a S). Código limpio, sin marcadores markdown.""",
    "mecanica": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Kinetic Auto: Mecánica'. Gris Asfalto, Naranja, Verde Neón. Hero Section: video placeholder. Tarjetas: 'Manuales 22R/Camry', 'AutoFix Engine'. Botón: 'Opciones de Crédito Tech'. Barra Lateral: Rango E a S (Obsidian Prime). Código limpio.""",
    "carpinteria": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Academia Maderera'. Marrón Nogal, Ámbar, Verde Neón. Tarjetas: 'Software Costeo', 'Planos 3D'. Barra Lateral Niveles E a S. Código limpio, 100% responsivo.""",
    "electronica": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Micro-Tech S-Prime: Celulares y PC'. Negro absoluto, Azul Cian, Verde Neón. Tarjetas: 'Curso Reparación', 'Sistema Tech-Manager'. Barra Lateral de Rango E a S. Entrégame el código completo.""",
    "reposteria": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Culinary S-Prime: Repostería y Dark Kitchens'. Tonos oscuros, Cobre, Verde Neón. Módulos: 'Panadería Rentable', 'Software Golden Suite Delivery'. Barra de Progresión Rango E a S. Código limpio.""",
    "infantil": """Eres Desarrollador Front-End UX/UI experto infantil. Escribe HTML/CSS/JS para 'S-Prime Next Gen: Apps Infantiles'. Colores pastel vibrantes (Azul, Amarillo) sobre fondo oscuro. Catálogo: 'App Vocales/Pony', 'Opción Premium: Graba voz'. Barra Infantil: 'Explorador E' a 'Héroe Rango S'. Código interactivo."""
}

def invocar_gemini(prompt):
    print("⏳ Conectando con Gemini 2.5 Flash (Nuevo Motor Rango S)...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"❌ Error al contactar a Gemini: {e}")
        return None

def limpiar_y_guardar(codigo_bruto, nombre_nicho):
    # Intentar extraer el código dentro de bloques ```html ... ``` o similar
    match = re.search(r'```(?:html)?(.*?)```', codigo_bruto, re.DOTALL | re.IGNORECASE)
    codigo = match.group(1).strip() if match else codigo_bruto.strip()
    nicho_limpio = nombre_nicho.lower().replace(" ", "_")

    # Bóveda
    with open(os.path.join(BOVEDA_DIR, f"{nicho_limpio}.html"), "w", encoding="utf-8") as f:
        f.write(codigo)
    
    # Producción
    with open(os.path.join(PROD_DIR, f"{nicho_limpio}.html"), "w", encoding="utf-8") as f:
        f.write(codigo)

    # Base de Datos
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vault_codigo
                 (id INTEGER PRIMARY KEY, autor_ia TEXT, lenguaje TEXT, categoria TEXT, codigo TEXT, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute("INSERT INTO vault_codigo (autor_ia, lenguaje, categoria, codigo) VALUES (?, ?, ?, ?)",
              ("Gemini 2.5 Flash", "HTML/CSS/JS", f"Landing_Shopify_{nicho_limpio}", codigo))
    conn.commit()
    conn.close()

    print(f"============================================================")
    print(f"🟢 [SUKUNA / GEMINI] MISIÓN COMPLETADA: {nicho_limpio.upper()}")
    print(f"✔ URL EN VIVO: http://127.0.0.1:8050/nichos/{nicho_limpio}.html")
    print(f"============================================================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 forja_nichos_gemini.py [nicho]")
        print("Disponibles:", ", ".join(MISIONES.keys()))
        sys.exit(1)
    
    nicho = sys.argv[1].lower()
    if nicho not in MISIONES:
        print(f"❌ Nicho '{nicho}' no encontrado.")
        sys.exit(1)
        
    codigo_ia = invocar_gemini(MISIONES[nicho])
    if codigo_ia:
        limpiar_y_guardar(codigo_ia, nicho)
