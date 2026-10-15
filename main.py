from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os

app = FastAPI()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def montar(ruta, carpeta):
    # Intenta en el directorio actual
    path = os.path.join(BASE_DIR, carpeta)
    if os.path.exists(path):
        app.mount(ruta, StaticFiles(directory=path, html=True), name=carpeta)
        return True
    # Intenta un nivel arriba (por si Railway ejecuta desde otra carpeta)
    path_up = os.path.join(os.path.dirname(BASE_DIR), carpeta)
    if os.path.exists(path_up):
        app.mount(ruta, StaticFiles(directory=path_up, html=True), name=carpeta)
        return True
    return False

panel_ok = montar('/panel', 'panel_maestro')
montar('/tier2', 'entregables_reales')
montar('/tier3', 'entregables_reales/tier3_enterprise')
montar('/productos', 'productos')

@app.get("/")
def raiz():
    if panel_ok:
        return RedirectResponse(url="/panel/")
    return {
        "estado": "ALERTA: Carpetas no encontradas",
        "directorio_base": BASE_DIR,
        "archivos_detectados": os.listdir(BASE_DIR)
    }
