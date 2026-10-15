import os
import sys
import sqlite3
import re
from dotenv import load_dotenv
from google import genai

# 1. RASTREO Y CARGA INVISIBLE DE LLAVES
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    rutas_env = [".env", "/workspaces/main.py/.env", os.path.expanduser("~/.env"), os.path.expanduser("~/jarvis_hub/.env")]
    for ruta in rutas_env:
        if os.path.exists(ruta):
            load_dotenv(ruta)
            api_key = os.environ.get("GEMINI_API_KEY")
            if api_key:
                break

if not api_key:
    print("❌ ERROR ABSOLUTO: No se encontró GEMINI_API_KEY en ninguna parte.")
    sys.exit(1)

# Limpieza estricta de la llave
api_key = api_key.strip("'\" \t\r\n")

# 2. INICIALIZAR EL MOTOR RANGO S
try:
    client = genai.Client(api_key=api_key)
    print("🔓 API Cerebro Jarvis Conectada (Gemini 2.5 Flash).")
except Exception as e:
    print(f"❌ Error crítico de Autenticación: {e}")
    sys.exit(1)

# 3. RUTAS DEL IMPERIO
BOVEDA_DIR = "sprime_boveda_codigo/landing_nichos"
PROD_DIR = "productos/nichos"
DB_PATH = "sprime_boveda_codigo/codigo_central.db"
os.makedirs(BOVEDA_DIR, exist_ok=True)
os.makedirs(PROD_DIR, exist_ok=True)

# 4. MISIONES DE CÓDIGO
MISIONES = {
    "barberia": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS (un archivo) para Landing 'Barbería 0 a 100'. Fondo oscuro, verde neón, Rajdhani. Tarjetas: 'Kit Inicio', 'Golden Suite'. Botón: 'Opciones financiamiento'. Barra: 'Nivel E a S'. CÓDIGO LIMPIO.""",
    "mecanica": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Kinetic Auto: Mecánica'. Gris Asfalto, Naranja, Verde Neón. Tarjetas: 'Manuales 22R/Camry', 'AutoFix Engine'. Botón: 'Crédito Tech'. Barra: Rango E a S. CÓDIGO LIMPIO.""",
    "carpinteria": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Academia Maderera'. Marrón Nogal, Ámbar, Verde Neón. Tarjetas: 'Software Costeo', 'Planos 3D'. Barra Niveles E a S. CÓDIGO LIMPIO.""",
    "electronica": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Micro-Tech S-Prime: Celulares'. Negro, Azul Cian, Verde Neón. Tarjetas: 'Curso Reparación', 'Tech-Manager'. Barra Rango E a S. CÓDIGO LIMPIO.""",
    "reposteria": """Eres Desarrollador Front-End Rango S. Escribe HTML/CSS/JS para 'Culinary S-Prime'. Tonos oscuros, Cobre, Verde Neón. Módulos: 'Panadería', 'Golden Suite Delivery'. Barra Rango E a S. CÓDIGO LIMPIO.""",
    "infantil": """Eres Desarrollador Front-End UX/UI infantil. Escribe HTML/CSS/JS para 'S-Prime Next Gen'. Colores pastel sobre oscuro. Catálogo: 'Vocales/Pony', 'Graba voz'. Barra: 'Explorador E' a 'Héroe Rango S'. CÓDIGO LIMPIO."""
}

def forjar_mision(nombre_nicho):
    prompt = MISIONES.get(nombre_nicho)
    print(f"⏳ Forjando código para: {nombre_nicho.upper()}...")
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt,
        )
        codigo_bruto = response.text
        match = re.search(r'```(?:html)?(.*?)```', codigo_bruto, re.DOTALL | re.IGNORECASE)
        codigo = match.group(1).strip() if match else codigo_bruto.strip()
        
        nicho_limpio = nombre_nicho.lower()
        
        # Guardar Archivos
        with open(os.path.join(BOVEDA_DIR, f"{nicho_limpio}.html"), "w", encoding="utf-8") as f: f.write(codigo)
        with open(os.path.join(PROD_DIR, f"{nicho_limpio}.html"), "w", encoding="utf-8") as f: f.write(codigo)
        
        # Registrar en Jarvis DB
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS vault_codigo (id INTEGER PRIMARY KEY, autor TEXT, categoria TEXT, codigo TEXT)''')
        c.execute("INSERT INTO vault_codigo (autor, categoria, codigo) VALUES (?, ?, ?)", ("Gemini-Jarvis", nicho_limpio, codigo))
        conn.commit()
        conn.close()

        print(f"🟢 [MISIÓN EXITOSA] {nicho_limpio.upper()} FORJADO Y ALMACENADO.")
        print(f"✔ URL: http://127.0.0.1:8050/nichos/{nicho_limpio}.html\n")
    except Exception as e:
        print(f"❌ Error en la forja: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nicho = sys.argv[1].lower()
        if nicho == "todos":
            for n in MISIONES.keys():
                forjar_mision(n)
        elif nicho in MISIONES:
            forjar_mision(nicho)
        else:
            print("❌ Nicho desconocido.")
    else:
        print("Uso: python3 orquestador_maestro.py [barberia|mecanica|todos]")
