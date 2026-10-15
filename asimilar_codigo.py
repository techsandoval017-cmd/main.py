import os
import sqlite3
import re

# Rutas del Imperio
BOVEDA_DIR = "sprime_boveda_codigo/landing_nichos"
PROD_DIR = "productos/nichos"
DB_PATH = "sprime_boveda_codigo/codigo_central.db"
INPUT_FILE = "codigo_claude.html"

os.makedirs(BOVEDA_DIR, exist_ok=True)
os.makedirs(PROD_DIR, exist_ok=True)

def asimilar():
    if not os.path.exists(INPUT_FILE):
        print("❌ [ALERTA] No se encontró el archivo 'codigo_claude.html'.")
        print("Pega el código de Claude primero usando: nano codigo_claude.html")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        codigo = f.read()

    if len(codigo.strip()) == 0:
        print("❌ El archivo está vacío. Pega el código de Claude dentro.")
        return

    # Los Cazadores leen el nicho automáticamente desde el código
    match = re.search(r'<title>(.*?)</title>', codigo, re.IGNORECASE)
    if match:
        nicho = match.group(1).replace(" ", "_").replace("-", "_").replace("|", "").strip().lower()
        nicho = re.sub(r'[^a-z0-9_]', '', nicho)
        nicho = nicho.replace("sprime", "").replace("corp", "").strip("_")
        if not nicho: nicho = "landing_nicho_generico"
    else:
        nicho = "landing_nicho_generico"

    # 1. Bóveda de Seguridad (Backup)
    boveda_path = os.path.join(BOVEDA_DIR, f"{nicho}.html")
    with open(boveda_path, "w", encoding="utf-8") as f:
        f.write(codigo)

    # 2. Despliegue en Vivo a Producción (Puerto 8050)
    prod_path = os.path.join(PROD_DIR, f"{nicho}.html")
    with open(prod_path, "w", encoding="utf-8") as f:
        f.write(codigo)

    # 3. Registro en la Base de Datos Central SQLite
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vault_codigo
                 (id INTEGER PRIMARY KEY, autor_ia TEXT, lenguaje TEXT, categoria TEXT, codigo TEXT, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    c.execute("INSERT INTO vault_codigo (autor_ia, lenguaje, categoria, codigo) VALUES (?, ?, ?, ?)",
              ("Claude 3.5", "HTML/CSS/JS", f"Landing_Shopify_{nicho}", codigo))
    conn.commit()
    conn.close()

    print(f"============================================================")
    print(f"🟢 [SUKUNA / CAZADORES] CÓDIGO ASIMILADO Y DESPLEGADO")
    print(f"============================================================")
    print(f"✔ Nicho detectado y procesado: {nicho.upper()}")
    print(f"✔ Guardado en Bóveda local: {boveda_path}")
    print(f"✔ URL LISTA PARA SHOPIFY: http://127.0.0.1:8050/nichos/{nicho}.html")
    print(f"============================================================")
    print(f"El equipo de marketing tiene luz verde. Rumbo a Rango S.")

    # Limpiamos la boca de entrada para el siguiente código
    os.remove(INPUT_FILE)

if __name__ == "__main__":
    asimilar()
