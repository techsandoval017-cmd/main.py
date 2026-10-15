import os

archivo_backend = "backend/main.py"

codigo_fix = """from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os

app = FastAPI()

# Obtener la ruta raiz absoluta del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def montar_ruta(ruta_url, carpeta_local):
    ruta_completa = os.path.join(BASE_DIR, carpeta_local)
    if os.path.exists(ruta_completa):
        app.mount(ruta_url, StaticFiles(directory=ruta_completa, html=True), name=carpeta_local)

# Montar los ecosistemas
montar_ruta('/panel', 'panel_maestro')
montar_ruta('/tier2', 'entregables_reales')
montar_ruta('/tier3', 'entregables_reales/tier3_enterprise')
montar_ruta('/productos', 'productos')

@app.get("/")
def raiz():
    # Redirigir el dominio principal directamente al panel maestro
    return RedirectResponse(url="/panel/")
"""

with open(archivo_backend, "w") as f:
    f.write(codigo_fix)

print("✅ Rutas absolutas inyectadas. Subiendo al servidor...")
os.system("git add . && git commit -m 'fix: rutas absolutas y redireccion al panel' && git push origin main")
