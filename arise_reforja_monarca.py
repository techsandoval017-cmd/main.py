import os
import sqlite3
import time
import shutil

# 1. CONEXIÓN A LA MEMORIA CENTRAL DEL GREMIO
conn = sqlite3.connect('sprime_academia/memoria_cursos.db')
c = conn.cursor()

# Purgar la debilidad (Borrar los nombres genéricos viejos)
c.execute('DROP TABLE IF EXISTS software_laboratorio')
c.execute('''CREATE TABLE software_laboratorio
             (id INTEGER PRIMARY KEY, nombre_saas TEXT, nicho_objetivo TEXT, descripcion TEXT, curso_gancho TEXT, estado TEXT)''')
conn.commit()

# 2. EL VERDADERO ARSENAL DE S-PRIME CORP
arsenal_saas = [
    {
        "id_folder": "obsidian_oracle",
        "nombre": "Obsidian Oracle",
        "nicho": "Data Science / Power BI / Excel",
        "desc": "El Ojo Absoluto. Limpia datos caóticos y proyecta la verdad financiera en dashboards corporativos oscuros de S-Prime.",
        "curso_gancho": "Curso: Excel Profesional y Power BI desde Cero."
    },
    {
        "id_folder": "shadow_legion_forge",
        "nombre": "Shadow Legion Forge",
        "nicho": "Inteligencia Artificial / Automatización",
        "desc": "La forja del ejército. Creador visual de agentes de ventas y bots de sombra para WhatsApp.",
        "curso_gancho": "Curso: Creación de Agentes IA y Automatización sin Código."
    },
    {
        "id_folder": "vortex_citadel",
        "nombre": "VORTEX Citadel",
        "nicho": "Ciberseguridad / Hacking Ético",
        "desc": "La fortaleza impenetrable. Auditor de ciberseguridad corporativo con generación de reportes ejecutivos.",
        "curso_gancho": "Curso: Ciberseguridad Defensiva y Análisis de Redes."
    },
    {
        "id_folder": "sprime_guild_master",
        "nombre": "S-Prime Guild Master",
        "nicho": "Project Management / Scrum",
        "desc": "El gestor de gremios. Asigna misiones a empleados (Cazadores) según su rango y mide el progreso del equipo con IA.",
        "curso_gancho": "Curso: Certificación Ágil, Scrum y Productividad Empresarial."
    },
    {
        "id_folder": "monarch_quant_terminal",
        "nombre": "Monarch Quant Terminal",
        "nicho": "Trading / Mercados Financieros",
        "desc": "El trono financiero. Terminal de operación algorítmica HFT con protocolos de preservación Rango S.",
        "curso_gancho": "Curso: Trading Institucional y Algorítmico."
    }
]

print("=== [S-PRIME AI] PURGANDO VESTIGIOS Y FORJANDO EL ARSENAL RANGO S ===")
BASE_DIR = "laboratorio_software"

# Limpieza de las carpetas viejas si existen
if os.path.exists(BASE_DIR):
    shutil.rmtree(BASE_DIR)
os.makedirs(BASE_DIR, exist_ok=True)

for saas in arsenal_saas:
    print(f"➜ Grabando en la memoria del Gremio: {saas['nombre']}...")
    
    # Inyectar en la base de datos
    c.execute("INSERT INTO software_laboratorio (nombre_saas, nicho_objetivo, descripcion, curso_gancho, estado) VALUES (?, ?, ?, ?, ?)",
              (saas['nombre'], saas['nicho'], saas['desc'], saas['curso_gancho'], 'FASE 1: Arquitectura Base'))
    conn.commit()
    
    # Crear estructura física de directorios
    prod_dir = os.path.join(BASE_DIR, saas["id_folder"])
    os.makedirs(prod_dir, exist_ok=True)
    os.makedirs(os.path.join(prod_dir, "backend"), exist_ok=True)
    os.makedirs(os.path.join(prod_dir, "frontend"), exist_ok=True)
    
    # Crear Código Backend Base con la identidad correcta
    codigo_main = f"""from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="{saas['nombre']} | S-Prime Corp", version="1.0")

class OrdenDirector(BaseModel):
    comando: str
    parametros: dict

@app.get("/")
def estado_sistema():
    return {{"status": "online", "sistema": "{saas['nombre']}", "dominio": "{saas['nicho']}"}}

@app.post("/ejecutar")
def ejecutar_orden(req: OrdenDirector):
    # TODO: Lógica de ejecución de sombras (Goku / Arquitecto)
    return {{"status": "success", "mensaje": f"Orden '{{req.comando}}' asimilada por {saas['nombre']}."}}
"""
    with open(os.path.join(prod_dir, "backend", "main.py"), "w") as f:
        f.write(codigo_main)
        
    # Crear Documentación de Guerra (Readme)
    codigo_readme = f"""# {saas['nombre']}
## Identidad y Propósito
{saas['desc']}

## Doctrina del Caballo de Troya
- **Mercado de Infiltración:** Udemy / Hotmart
- **Curso Gancho:** {saas['curso_gancho']}
- **Objetivo:** Educar al prospecto en la versión manual de este nicho, arrastrarlo al ecosistema S-Prime, y venderle esta infraestructura corporativa.

## Stack de Forja
- Servidor: FastAPI (Python)
- Interfaz: React / S-Prime Dark UI
- Base de Datos: Arquitectura Relacional y Vectorial
"""
    with open(os.path.join(prod_dir, "README.md"), "w") as f:
        f.write(codigo_readme)
        
    time.sleep(0.3)

print("\n✔ Código Rango S estructurado en 'laboratorio_software/'.")
print("✔ Base de datos local reescrita. Los agentes ahora responden a los nombres de Obsidian y S-Prime.")
print("=== [S-PRIME AI] OPERACIÓN DE REFORJA COMPLETADA ===")

conn.close()
